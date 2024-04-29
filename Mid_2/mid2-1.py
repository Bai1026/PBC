# int_list = list(map(int, input().split(',')))
n, m = map(int, input().split(','))
positions = list(map(int, input().split(',')))

if m!=0:
    unavailable = list(map(int, input().split(',')))
else:
    unavailable = []
# out_store = []

# 需要確認可用便利商店的位置
available_positions = {i: positions[i-1] for i in range(1, len(positions)+1) if i not in unavailable}

# 計算每一間可以設置的便利商店與其他所有便利商店的距離總和
distances = {}
for store_id, store_pos in available_positions.items():
    total_distance = sum(abs(store_pos - pos) for pos in positions)
    distances[store_id] = total_distance

# 找出距離總和最小的便利商店編號
min_distance = min(distances.values())
best_stores = [store_id for store_id, distance in distances.items() if distance == min_distance]

print(','.join(map(str, best_stores)))
