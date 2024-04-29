def find_longest_sequence(lst, m, threshold):
    best_start = None
    best_length = 0
    
    current_length = 0
    start_index = None

    for i in range(len(lst)):
        if lst[i] >= threshold:
            if current_length == 0:
                start_index = i
            current_length += 1
        else:
            if current_length >= m and current_length > best_length:
                best_length = current_length
                best_start = start_index + 1
            current_length = 0

    if current_length >= m and current_length > best_length:
        best_length = current_length
        best_start = start_index + 1

    # return (best_start, best_length) if best_start is not None else None
    return best_start if best_start is not None else None

n, m, L, M, H = map(int, input().split(','))
lst = list(map(int, input().split(',')))

threshold = None
start_position = find_longest_sequence(lst, m, H)
if start_position == None:
    start_position = find_longest_sequence(lst, m, M)
    if start_position == None:
        start_position = find_longest_sequence(lst, m, L)
        if start_position != None: 
            threshold = 'L'
    else:
        threshold = 'M'
else:
    threshold = 'H'

if threshold != None:
    print(start_position, threshold, sep=',')
else:
    print('NONE')