n, m = map(int, input().split(','))
positions = list(map(int, input().split(',')))

if m!=0:
    unavailable = list(map(int, input().split(',')))
else:
    unavailable = []

available_positions = {i: positions[i-1] for i in range(1, len(positions)+1) if i not in unavailable}

distances = {}
for store_id, store_pos in available_positions.items():
    total_distance = sum(abs(store_pos - pos) for pos in positions)
    distances[store_id] = total_distance

min_distance = min(distances.values())
best_stores = [store_id for store_id, distance in distances.items() if distance == min_distance]

print(','.join(map(str, best_stores)))
