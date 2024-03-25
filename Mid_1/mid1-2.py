n, E, P, S = map(int, input().split(','))

e_list = list(map(int, input().split(',')))
p_list = list(map(int, input().split(',')))

both_manager_list = []
sum_manager_list = []

for i in range(n):
    if e_list[i] >= E and p_list[i] >= P:
        both_manager_list.append(i+1)
    elif e_list[i] + p_list[i] >= S:
        sum_manager_list.append(i+1)

if len(both_manager_list) == 0 and len(sum_manager_list) == 0:
    print(0)
elif len(both_manager_list) == 0:
    print(','.join(map(str, sum_manager_list)))
else:
    print(','.join(map(str, both_manager_list)))