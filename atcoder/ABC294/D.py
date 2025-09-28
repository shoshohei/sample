import heapq

n, Q = map(int, input().split())
called_heap = []
removed = set()
called_ptr = 0  # 次に呼ばれる人

for _ in range(Q):
    query = list(map(int, input().split()))
    print(called_heap, removed)
    if query[0] == 1:
        called_ptr += 1
        heapq.heappush(called_heap, called_ptr)
    elif query[0] == 2:
        removed.add(query[1])
    else:
        # 削除済みの要素を先頭から取り除く
        while called_heap[0] in removed:
            removed.remove(called_heap[0])
            heapq.heappop(called_heap)
        print(called_heap[0])
