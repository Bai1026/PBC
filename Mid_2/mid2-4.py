n, d = map(int, input().split(','))
positions = list(map(int, input().split(',')))

# set the best store.
def find_best_stores(positions, ice_cream_store):
    # available_positions = {i: positions[i-1] for i in range(1, len(positions)+1) if }
    available_positions = {i: positions[i-1] for i in range(1, len(positions)+1) if i in ice_cream_store}
    # print(available_positions)

    distances = {}
    for store_id, store_pos in available_positions.items():
        total_distance = sum(abs(store_pos - pos) for pos in positions)
        distances[store_id] = total_distance

    min_distance = min(distances.values())
    best_stores = [store_id for store_id, distance in distances.items() if distance == min_distance]

    print(','.join(map(str, best_stores)))


def find_adjacent_min_differences(lst, d):
    new_list = []
    for idx, i in enumerate(lst):
        
        differences = [abs(i - j) for j in lst if i != j]
        
        min_difference = min(differences)
        
        if min_difference >= d:
            new_list.append(idx+1)
    return new_list


ice_cream_store = find_adjacent_min_differences(positions, d)
if len(ice_cream_store) == 0:
    print('NONE')
else:
    find_best_stores(positions, ice_cream_store)

