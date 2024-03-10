tmp = input().split(',')
job_amount = int(tmp[0])
combination = int(tmp[1])

time = list(map(int, input().split(',')))
deadline = list(map(int, input().split(',')))

order_list = []
for i in range(combination):
    order = list(map(int, input().split(',')))
    order_list.append(order)

min_delay = float('inf')
order_id = None

for idx, order in enumerate(order_list):
    used_time = 0
    total_late = 0

    for i in range(job_amount):
        job_id = order[i]
        ddl = deadline[job_id-1]

        used_time += time[job_id-1]
        late = used_time - ddl

        if late >= 0:
            total_late += late

    # if equal, we do not change since we want the one with min id
    if total_late < min_delay:
        min_delay = total_late
        order_id = idx + 1

print(order_id, min_delay, sep = ',')