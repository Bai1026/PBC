job_amount = int(input())

time = list(map(int, input().split(',')))
deadline = list(map(int, input().split(',')))
order = list(map(int, input().split(',')))

used_time = 0
total_late = 0

for i in range(job_amount):
    job_id = order[i]
    ddl = deadline[job_id-1]

    used_time += time[job_id-1]
    late = used_time - ddl

    if late >= 0:
        total_late += late

print(total_late)