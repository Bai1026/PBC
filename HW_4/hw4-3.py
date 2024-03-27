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
    def find_max_prob():
        max_prob = 0
        client_count = 0 # since we can not use enumerate, so we use count += 1 instead
        chosen_list = []

        for client in prob_list:
            if client_count + 1 in omit_client:
                client_count += 1
                continue

            # since we have m+1 kinds of discount
            for i in range(discount_num + 1):
                if limit_list[i] == 0: continue

                if client[i] >= max_prob:
                    if client[i] > max_prob:
                        chosen_list = []
                    max_prob = client[i]
                    chosen_list.append(((client_count + 1), i))
                    # limit_list[i] -= 1

            client_count += 1
        return chosen_list

    def find_max_limit():
        max_limit = 0
        max_limit_client_list = []

        for item in max_prob_list:
            client, discount = item[0] - 1, item[1]

            # find the limitation >= cases
            if limit_list[discount] >= max_limit:
                if limit_list[discount] > max_limit:
                    max_limit_client_list = []

                max_limit = limit_list[discount]
                max_limit_client_list.append((client+1, discount))
        return max_limit_client_list

    '''
    for same prob -> has the most limit num -> min discount id -> min client id
    so I find the list with the "highest prob" first
    then I find the list with the "highest limitation num"
    then I find the list with the lowest "discount id"
    finally, print the list's first element's [0] and [1] since it's appended by the client id
    ''' 


    max_prob_list = find_max_prob()
    max_limit_client_list = find_max_limit()

    min_discount = 9999999 # since we can not use float('inf), we use 99999 instead
    min_discount_list = []
    for item in max_limit_client_list:
        client, discount = item[0], item[1]
        if discount <= min_discount:
            if discount < min_discount:
                min_discount_list = []
            min_discount = discount
            min_discount_list.append((client, discount))

    min_client, min_discount = min_discount_list[0][0], min_discount_list[0][1]

    output_list.append([min_client, min_discount])
    omit_client.append(min_client)
    limit_list[min_discount] -= 1

    

omit_client = []
for _ in range(client_num):
    find_max_client()

for i in range(client_num):
    for item in output_list:
        if i + 1 == item[0]:
            # print(item)
            if item[0] == client_num:
                print(item[1])
            else:
                print(item[1], end=',')
