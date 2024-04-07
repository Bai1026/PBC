job_amount = int(input())

time = list(map(int, input().split(',')))
deadline = list(map(int, input().split(',')))
init_order = list(map(int, input().split(',')))

min_delay = float('inf')
best_order = init_order.copy()

while True:
    order_list = [best_order]
    swapped = best_order.copy()
    swapped[0], swapped[-1] = swapped[-1], swapped[0]
    order_list.append(swapped)
    
    for i in range(len(best_order) - 1):
        swapped = best_order.copy()
        swapped[i], swapped[i + 1] = swapped[i + 1], swapped[i]
        order_list.append(swapped)

    found_better = False
    
    for order in order_list:
        used_time = 0
        total_late = 0

        for job_id in order:
            ddl = deadline[job_id-1]
            used_time += time[job_id-1]
            late = used_time - ddl

            if late > 0:
                total_late += late

        if total_late < min_delay:
            min_delay = total_late
            best_order = order
            found_better = True

    if not found_better:
        break

best_order_str = ','.join(map(str, best_order))
print(f"{best_order_str};{min_delay}")