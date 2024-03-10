job_amount = int(input())

time = list(map(int, input().split(',')))
deadline = list(map(int, input().split(',')))
init_order = list(map(int, input().split(',')))

# I do a order list like HW2 by swapping each neighbor elements in the order list
order_list = []
order_list.append(init_order)

# For Head and Tail since the index issue
# use copy for avoiding the address issue for the future work
swapped = init_order.copy()
swapped[0], swapped[-1] = swapped[-1], swapped[0]
order_list.append(swapped)

# For others combinations
for i in range(len(init_order) - 1):
    swapped = init_order.copy()
    swapped[i], swapped[i + 1] = swapped[i + 1], swapped[i]
    order_list.append(swapped)

# For calculating the minmum delay time
min_delay = float('inf')

for order in order_list:
    used_time = 0
    total_late = 0

    for i in range(job_amount):
        # getting the useful information
        job_id = order[i]
        ddl = deadline[job_id-1]
        used_time += time[job_id-1]
        late = used_time - ddl

        if late >= 0:
            total_late += late

    # if equal, we do not change since it's no needed
    if total_late < min_delay:
        min_delay = total_late

print(min_delay)