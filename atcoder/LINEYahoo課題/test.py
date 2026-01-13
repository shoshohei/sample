import sys

# def main(lines):
#     # このコードは標準入力と標準出力を用いたサンプルコードです。
#     # このコードは好きなように編集・削除してもらって構いません。

#     for i, v in enumerate(lines):
#         print("line[{0}]: {1}".format(i, v))

# if __name__ == '__main__':
#     lines = []
#     for l in sys.stdin:
#         lines.append(l.rstrip('\r\n'))
#     main(lines)


class User():
    def __init__(self, id):
        self.user_id = id
        self.reservation = None
        self.rental = None
        self.history = []

    def has_reservation(self):
        return self.reservation is not None

    def is_renting(self):
        return self.rental is not None


    def set_reservation(self, reservation):
        self.reservation = reservation

    def clear_reservation(self):
        self.reservation = None

    def start_rental(self, rental):
        self.rental = rental

    def finish_rental(self):
        rental = self.rental
        self.rental = None
        return rental

    def cancel_reservation(self):
        if self.reservation:
            self.reservation.cancel()

    def add_history(self, rental_history):
        self.history.append(rental_history)


class Base():
    def __init__(self, id, capacity, bikes):
        self.base_id = id
        self.capacity = capacity
        self.bikes = bikes
        self.rent_reserved = 0
        self.return_reserved = 0
        self.renting_return = 0

    def can_rent(self):
        return self.bikes - self.rent_reserved > 0

    def can_return(self):
        return self.capacity - (self.bikes + self.renting_return + self.return_reserved) > 0
    
    def reserve_rent(self):
        self.rent_reserved += 1

    def reserve_return(self):
        self.return_reserved += 1

    def cancel_rent_reserve(self):
        self.rent_reserved -= 1

    def cancel_return_reserve(self):
        self.return_reserved -= 1

    def cancel_reservation(self, rid):
        if self.reservation and self.reservation.rid == rid:
            return self.reservation.cancel()
        return False

    def start_rent(self, to_base):
        # 貸出拠点
        self.bikes -= 1
        self.rent_reserved -= 1

        # 返却拠点
        to_base.return_reserved -= 1
        to_base.renting_return += 1

    def finish_return(self):
        self.bikes += 1
        self.renting_return -= 1

class Reservation:
    def __init__(self, rid, user, request_time, wish_time, from_base, to_base):
        self.rid = rid
        self.user = user
        self.request_time = request_time
        self.wish_time = wish_time
        self.expire_time = wish_time + timedelta(minutes=30)

        self.from_base = from_base
        self.to_base = to_base

        self.active = True  # 自動キャンセル・手動キャンセル対策

    def is_expired(self, now):
        return self.active and now > self.expire_time

    def invalidate(self):
        self.active = False

    def cancel(self):
        if not self.active:
            return False

        self.active = False
        self.from_base.cancel_rent_reserve()
        self.to_base.cancel_return_reserve()
        self.user.clear_reservation()
        return True

class Rental:
    def __init__(self, user, start_time, from_base, to_base):
        self.user = user
        self.start_time = start_time

        self.from_base = from_base
        self.to_base = to_base
        self.start_base = from_base

        self.change_count = 0

    def calc_duration(self, now):
        return now - self.start_time
    
    def change_destination(self, new_base):
        self.to_base = new_base
        self.change_count += 1


class RentalHistory:
    def __init__(self, start_time, start_base, end_time, end_base, price):
        self.start_time = start_time
        self.start_base = start_base
        self.end_time = end_time
        self.end_base = end_base
        self.price = price

import math

def calc_cost(duration):
    total_seconds = duration.total_seconds()
    total_minutes = total_seconds / 60

    if total_minutes <= 30:
        return 150
    else:
        extra = total_minutes - 30
        blocks = math.ceil(extra / 15)
        return 150 + blocks * 100

# def auto_cancel(now):
#     for res in list(Reservations.values()):
#         if res.is_expired(now):
#             res.invalidate()
#             res.from_base.cancel_rent_reserve()
#             res.to_base.cancel_return_reserve()
#             res.user.clear_reservation()
def auto_cancel(now):
    for res in list(Reservations.values()):
        if res.is_expired(now):
            res.cancel()


from datetime import datetime, timedelta
#入力処理
x = int(input()) # 割引率
n = int(input()) # 拠点数
A, B = [0]*n, [0]*n # 拠点iのスペース、拠点iにある自転車の数
for i in range(n):
    A[i], B[i] = [int(i) for i in input().split(' ')]
m = int(input()) # クエリ数
Q = [input() for _ in range(m)] #クエリ文字列

Users = {}
Bases = {}
Reservations = {}
Rentals = {}
for i in range(n):
    Bases[i] = Base(i+1, A[i], B[i])
# print(Bases)
def get_user(id: str) -> User:
    if id not in Users:
        Users[id] = User(id)
    return Users[id]

def get_base(id: int) -> Base:
    # print(id)
    return Bases[id-1]

reservation_id = 1
rental_id = 1
for q in Q:
    
    q_pattern = q.split(':')[0]
    q_list = q.split(' ') 
    # exit(q_list[1])
    now_time = datetime.strptime(q_list[1], "%Y/%m/%d-%H:%M:%S")
    auto_cancel(now_time)

    # 予約
    if q_pattern == 'reserve':
        user_id = q_list[2]
        rent_time = datetime.strptime(q_list[3], "%Y/%m/%d-%H:%M:%S")
        rent_base_id, return_base_id = int(q_list[4]), int(q_list[5])

        user = get_user(user_id)
        rent_Base = get_base(rent_base_id)
        return_Base = get_base(return_base_id)

        # 予約があるか確認
        if user.has_reservation():
            print('reserve: too many reservations')
            continue
        if user.is_renting():
            print('reserve: renting')
            continue
        if not rent_Base.can_rent():
            print('reserve: no bicycles available for rent')
            continue
        if not return_Base.can_return():
            print('reserve: no place to return')
            continue
        
        # 予約成功
        rent_Base.reserve_rent()
        return_Base.reserve_return()
        reservation = Reservation(reservation_id, user, now_time, rent_time, rent_Base, return_Base)
        Reservations[reservation_id] = reservation
        user.set_reservation(reservation)
        print('reserve: {} {}'.format(user_id, reservation_id))
        reservation_id += 1

        

    # 貸出
    elif q_pattern == 'rent':
        user_id = q_list[2]
        base_id = int(q_list[3])

        user = get_user(user_id)
        rent_Base = get_base(base_id)

        if not user.has_reservation():
            print('rent: no reservations')
            continue
        if rent_Base.base_id != user.reservation.from_base.base_id:
            print('rent: different from reservation information')
            continue
        
        reservation = user.reservation
        # Reservations[reservation.rid] = None
        rental = Rental(user, now_time, reservation.from_base, reservation.to_base)
        Rentals[rental_id] = rental

        user.clear_reservation()
        reservation.invalidate()
        user.start_rental(rental)

        reservation.from_base.start_rent(reservation.to_base)

        print(f"rent: {user_id} (from {reservation.from_base.base_id} to {reservation.to_base.base_id})")
        rental_id += 1


    # 返却
    elif q_pattern == 'return':
        user_id = q_list[2]
        base_id = int(q_list[3])
        
        user = get_user(user_id)
        return_Base = get_base(base_id)

        if not user.is_renting():
            print('return: the user don\'t rent a bicycle')
            continue
        if user.rental.to_base!=return_Base:
            print('return: different destination')
            continue
        
        rental = user.finish_rental()
        rental.to_base.finish_return()
        duration = rental.calc_duration(now_time)
        price = calc_cost(duration)
        history = RentalHistory(rental.start_time, rental.start_base.base_id,
                        now_time, rental.to_base.base_id, price)

        user.add_history(history)
        print(f"return: {user_id} {price}")

    # 拠点確認
    elif q_pattern == 'base':
        base_id = int(q_list[2])
        
        base = get_base(base_id)
        print('base: {} {} {} {}'.format(base.base_id, base.capacity, 
        base.bikes-base.rent_reserved, base.capacity - (base.bikes + base.renting_return + base.return_reserved)))


    elif q_pattern == 'cancel':
        user_id = q_list[2]
        reservation_id = int(q_list[3])

        user = get_user(user_id)

        if not reservation_id in Reservations.keys():
            print('cancel: unavailable reservation')
            continue
        if user.reservation.rid != reservation_id:
            print('cancel: unauthorized')
            continue

        reservation = Reservations[reservation_id]
        reservation.cancel()
        # Reservations[reservation_id] = None
        print('cancel: {}'.format(reservation_id))   

    elif q_pattern == 'change':
        user_id = q_list[2]
        new_base_id = int(q_list[3])

        user = get_user(user_id)
        new_base = get_base(new_base_id)

        if not user.is_renting():
            print("change: the user don't rent a bicycle")
            continue

        rental = user.rental

        if rental.to_base.base_id == new_base.base_id:
            print("change: same base")
            continue

        if not new_base.can_return():
            print("change: no place to return")
            continue

        old_base = rental.to_base
        old_base.renting_return -= 1
        old_base.return_reserved += 1

        rental.change_destination(new_base)

        new_base.return_reserved -= 1
        new_base.renting_return += 1


        print(f"change: {user_id} {new_base.base_id}")



    elif q_pattern == 'history':
        user_id = q_list[2]
        now_time = datetime.strptime(q_list[1], "%Y/%m/%d-%H:%M:%S")

        user = get_user(user_id)

        history_list = sorted(user.history, key=lambda h: h.start_time, reverse=True)

        history_list = history_list[:5]

        print(f"history: {user_id}")
        for h in history_list:
            start_str = h.start_time.strftime("%Y/%m/%d-%H:%M:%S")
            end_str = h.end_time.strftime("%Y/%m/%d-%H:%M:%S")
            print(f"{start_str} {h.start_base} {end_str} {h.end_base} ({h.price} yen)")
