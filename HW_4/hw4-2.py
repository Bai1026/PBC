# client from 1 and discount from 0
client_num, discount_num = map(int, input().split(','))

# construct a 2D list, whose elements i is the prob of this client mapping each discount
# notice that the 0th discount is no account
prob_list = []
for _ in range(client_num):
    tmp_list = list(map(int, input().split(',')))
    prob_list.append(tmp_list)

limit_list = list(map(int, input().split(',')))
block_list = list(map(int, input().split(',')))

limit_list.insert(0, client_num)

max_prob = 0
chosen_client = None
chosen_discount = None
client_count = 0 # since we can not use enumerate, so we use count += 1 instead

for client in prob_list:
    # choose the client we want
    if block_list[client_count] == 1:
        client_count += 1
        continue

    for i in range(discount_num + 1):
        if limit_list[i] == 0:
            continue

        if client[i] > max_prob:
            max_prob = client[i]
            chosen_client = client_count + 1
            chosen_discount = i

    client_count += 1

print(f"{chosen_client},{chosen_discount}")



'''
3,2
44,31,41
17,45,23
23,65,44
2,2
0,1,0
'''