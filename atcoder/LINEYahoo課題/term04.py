import sys
import math
from datetime import datetime, timedelta

def parse_datetime(s):
    return datetime.strptime(s, "%Y/%m/%d-%H:%M:%S")

def get_cycles(duration_sec, interval_min):
    """
    1秒後に1回目、以降 interval_min ごとに加算される回数を計算。
    """
    if duration_sec <= 0:
        return 0
    interval_sec = interval_min * 60
    # 秒に変化し計算
    return 1 + (duration_sec - 1) // interval_sec


class Seat:
    def __init__(self, seat_id, type_id):
        self.id = seat_id
        self.type_id = type_id
        self.current_user_id = None
        self.available_at = datetime(2000, 1, 1)

    def is_vacant(self, current_time):
        return self.current_user_id is None and self.available_at <= current_time

    def start_use(self, user_id):
        self.current_user_id = user_id

    def end_use(self, clean_duration_min, current_time):
        self.current_user_id = None
        self.available_at = current_time + timedelta(minutes=clean_duration_min)

class Shower:
    def __init__(self, shower_id):
        self.id = shower_id
        self.current_user_id = None
        self.available_at = datetime(2000, 1, 1)

    def is_available(self, current_time):
        return self.current_user_id is None and self.available_at <= current_time

    def start_use(self, user_id):
        self.current_user_id = user_id

    def end_use(self, clean_duration_min, current_time):
        self.current_user_id = None
        self.available_at = current_time + timedelta(minutes=clean_duration_min)

class User:
    def __init__(self, user_id, seat_id, checkin_time):
        self.id = user_id
        self.seat_id = seat_id
        self.checkin_time = checkin_time
        self.ordered_food_ids = []
        self.shower_total_fee = 0
        # 値がNoneでない場合使用している
        self.current_shower_start = None
        self.is_checked_out = False

    def get_duration_sec(self, current_time):
        return int((current_time - self.checkin_time).total_seconds())


class InternetCafeSystem:
    def __init__(self):
        # 初期設定の読み込み
        self.load_data()
        # クエリ実行
        self.users = {}
        self.next_user_id = 1

    def load_data(self):
        input_data = sys.stdin.read().splitlines()
        if not input_data: return
        
        line1 = input_data[0].split()
        self.n, self.m, self.clean_seat_dur = map(int, line1)
        
        # 座席の初期化
        seat_types = list(map(int, input_data[1].split()))
        self.seats = {i + 1: Seat(i + 1, seat_types[i]) for i in range(self.n)}
        
        # 料金設定の読み込み
        self.price_configs = {}
        idx = 2
        for i in range(1, self.m + 1):
            basic_info = list(map(int, input_data[idx].split()))
            basic_price, p_count = basic_info[0], basic_info[1]
            idx += 1
            packs = []
            for _ in range(p_count):
                packs.append(list(map(int, input_data[idx].split())))
                idx += 1
            self.price_configs[i] = {"basic": basic_price, "packs": packs}
            
        # フード情報の読み込み
        self.f_count = int(input_data[idx])
        idx += 1
        self.food_prices = list(map(int, input_data[idx].split()))
        idx += 1
        
        # クーポン情報の読み込み
        self.c_count = int(input_data[idx])
        idx += 1
        self.coupons = {}
        for i in range(1, self.c_count + 1):
            target, disc = map(int, input_data[idx].split())
            self.coupons[i] = {"target": target, "discount": disc}
            idx += 1
            
        # シャワー情報の読み込み
        s_line = input_data[idx].split()
        idx += 1
        self.s_count, self.s_charge, self.s_clean_dur = map(int, s_line)
        self.showers = {i + 1: Shower(i + 1) for i in range(self.s_count)}
        
        # クエリ情報の読み込み
        self.queries = input_data[idx+1:]

    def calculate_total_bill(self, user, coupon_ids, current_time):
        # 1. 座席料金の計算
        seat = self.seats[user.seat_id]
        conf = self.price_configs[seat.type_id]
        duration_sec = user.get_duration_sec(current_time)
        duration_min = math.ceil(duration_sec / 60)
        
        seat_options = []
        # 通常料金
        seat_options.append(get_cycles(duration_sec, 10) * conf["basic"])
        # パック料金
        for p_time, p_price in conf["packs"]:
            price = p_price
            # パック設定よりも時間がオーバーした場合，オーバーしている分を基本料金として計算
            if duration_sec > p_time * 60:
                over_sec = duration_sec - (p_time * 60)
                price += get_cycles(over_sec, 10) * conf["basic"]
            seat_options.append(price)
        # 基本料金と，すべてのパック料金を使用した内，最安値を料金として選択
        final_seat_price = min(seat_options)

        # 2. フード料金の計算（クーポン適用）
        food_counts = {}
        for fid in user.ordered_food_ids:
            food_counts[fid] = food_counts.get(fid, 0) + 1
        
        base_food_total = sum(self.food_prices[fid-1] for fid in user.ordered_food_ids)
        
        discount_total = 0
        if coupon_ids:
            max_discounts_per_food = {}
            for cid in coupon_ids:
                c = self.coupons[cid]
                max_discounts_per_food[c["target"]] = max(max_discounts_per_food.get(c["target"], 0), c["discount"])
            
            for fid, disc in max_discounts_per_food.items():
                discount_total += disc * food_counts.get(fid, 0)

        # 全額合計
        return final_seat_price + (base_food_total - discount_total) + user.shower_total_fee

    def run(self):
        for q in self.queries:
            parts = q.split()
            if not parts: continue
            cmd, curr_time = parts[0], parse_datetime(parts[1])

            # 受付クエリ
            if cmd == "checkin:":
                tid = int(parts[2])
                # 条件に合致する利用可能なシートがあるか確認
                target_seat = next((s for s in self.seats.values() if s.type_id == tid and s.is_vacant(curr_time)), None)
                if target_seat:
                    uid = self.next_user_id
                    self.next_user_id += 1
                    target_seat.start_use(uid)
                    self.users[uid] = User(uid, target_seat.id, curr_time)
                    print(f"checkin: userid = {uid}, seatid = {target_seat.id}")
                else:
                    print("checkin: fully occupied")

            # 利用時間取得クエリ
            elif cmd == "get-duration:":
                sid = int(parts[2])
                seat = self.seats[sid]
                if seat.current_user_id is None:
                    print("get-duration: seat not used")
                else:
                    user = self.users[seat.current_user_id]
                    # 分単位で切り上げ
                    print(f"get-duration: {math.ceil(user.get_duration_sec(curr_time) / 60)}")

            # フード注文クエリ
            elif cmd == "order-food:":
                sid, fid = int(parts[2]), int(parts[3])
                uid = self.seats[sid].current_user_id
                if uid is None:
                    print("order-food: seat not used")
                else:
                    self.users[uid].ordered_food_ids.append(fid)
                    print("order-food: ok")

            # シャワー使用開始クエリ
            elif cmd == "shower-start:":
                sid = int(parts[2])
                uid = self.seats[sid].current_user_id
                if uid is None:
                    print("shower-start: seat not used")
                elif self.users[uid].current_shower_start:
                    print("shower-start: already started")
                else:
                    target_shower = next((sh for sh in self.showers.values() if sh.is_available(curr_time)), None)
                    if target_shower:
                        target_shower.start_use(uid)
                        self.users[uid].current_shower_start = curr_time
                        print(f"shower-start: {target_shower.id}")
                    else:
                        print("shower-start: fully occupied")

            # シャワー使用終了クエリ
            elif cmd == "shower-end:":
                sid = int(parts[2])
                uid = self.seats[sid].current_user_id
                if uid is None:
                    print("shower-end: seat not used")
                elif not self.users[uid].current_shower_start:
                    print("shower-end: not started")
                else:
                    user = self.users[uid]
                    # シャワー料金計算
                    duration_sec = int((curr_time - user.current_shower_start).total_seconds())
                    user.shower_total_fee += get_cycles(duration_sec, 15) * self.s_charge
                    # ユーザのシャワー利用状況を初期に戻す
                    user.current_shower_start = None
                    # シャワー室解放
                    shower = next(sh for sh in self.showers.values() if sh.current_user_id == uid)
                    shower.end_use(self.s_clean_dur, curr_time)
                    print(f"shower-end: {math.ceil(duration_sec / 60)}")

            elif cmd == "get-vacant-seats:":
                vacant_map = {}
                for s in self.seats.values():
                    if s.is_vacant(curr_time):
                        # 空席なシートsのタイプの個数を1加算
                        vacant_map[s.type_id] = vacant_map.get(s.type_id, 0) + 1
                sorted_types = sorted(vacant_map.keys())
                print(f"get-vacant-seats: {len(sorted_types)}")
                for tid in sorted_types:
                    print(f"{tid} {vacant_map[tid]}")

            elif cmd == "checkout:":
                uid = int(parts[2])
                if uid not in self.users:
                    print("checkout: invalid user")
                elif self.users[uid].is_checked_out:
                    print("checkout: already done")
                elif self.users[uid].current_shower_start:
                    print("checkout: shower is still in use")
                else:
                    user = self.users[uid]
                    # クーポンを所持していない場合は空リスト
                    coupon_ids = [int(x) for x in parts[4:]] if int(parts[3]) > 0 else []
                    
                    # バリデーション
                    ordered_set = set(user.ordered_food_ids)
                    # 提示クーポンの内，一つでも注文したフードのいずれにも使用できないものがある場合は，不正なクエリとしてスキップ
                    if any(self.coupons[cid]["target"] not in ordered_set for cid in coupon_ids):
                        print("checkout: invalid coupon")
                        continue
                    
                    # 料金確定
                    bill = self.calculate_total_bill(user, coupon_ids, curr_time)
                    print(f"checkout: {bill}")
                    
                    # 座席解放
                    user.is_checked_out = True
                    self.seats[user.seat_id].end_use(self.clean_seat_dur, curr_time)

if __name__ == "__main__":
    system = InternetCafeSystem()
    system.run()