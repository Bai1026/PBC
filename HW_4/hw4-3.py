# client from 1 and discount from 0
client_num, discount_num = map(int, input().split(','))

# construct a 2D list, whose elements i is the prob of this client mapping each discount
# notice that the 0th discount is no account
prob_list = []
for _ in range(client_num):
    tmp_list = list(map(int, input().split(',')))
    prob_list.append(tmp_list)

limit_list = list(map(int, input().split(',')))
limit_list.insert(0, client_num)

discount = []
output_list = []

def find_max_client():
    max_prob = 0
    chosen_client = 99999
    chosen_discount = None

    for idx, client in enumerate(prob_list):
        if idx + 1 in omit_client:
            continue

        for i in range(discount_num + 1):
            if limit_list[i] == 0:
                continue

            if client[i] > max_prob:
                max_prob = client[i]
                chosen_client = idx + 1
                chosen_discount = i

            if client[i] == max_prob and limit_list[i] > limit_list[chosen_discount] and idx + 1 <= chosen_client:
                chosen_discount = i


    # print(f"{chosen_client},{chosen_discount}")
    output_list.append([chosen_client, chosen_discount])
    omit_client.append(chosen_client)
    limit_list[chosen_discount] -= 1
    # print(limit_list)
    # print()

    

omit_client = []
# print()
for _ in range(client_num):
    find_max_client()
#     print(omit_client)

# print(output_list)

for i in range(client_num):
    for item in output_list:
        if i + 1 == item[0]:
            # print(item)
            if item[0] == client_num:
                print(item[1])
            else:
                print(item[1], end=',')
'''
3,2
10,31,51
17,17,51
23,65,44
2,1
'''

'''
5,3
10,38,21,98
7,89,65,34
12,56,88,76
11,24,87,90
15,70,35,44
2,3,1
'''
