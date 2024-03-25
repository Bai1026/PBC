# got 6 points only
n = int(input())
r_num = list(map(int, input().split(',')))
y_num = list(map(int, input().split(',')))
w_num = list(map(int, input().split(',')))
price = list(map(int, input().split(',')))

rl, rh = map(int, input().split(','))
yl, yh = map(int, input().split(','))
wl, wh = map(int, input().split(','))

min_price_h = float('inf')
min_price_l = float('inf')
got_high = False
got_low = False

for i in range(n):
    if r_num[i] >= rh and y_num[i] >= yh and w_num[i] >= wh:
        got_high = True
        if price[i] < min_price_h:
            min_price_h = price[i]

    elif r_num[i] >= rl and y_num[i] >= yl and w_num[i] >= wl:
        got_low = True
        if price[i] < min_price_l:
            min_price_h = price[i]

def find_combinations_exceeding_x(lst, x):
    result = []
    for i in range(len(lst)):
        # for j in range(i + 1, len(lst)):
        for j in range(i, len(lst)):
            if lst[i] + lst[j] > x:
                result.append((i, j))
    return result

def get_set(list1, list2, list3):
    set1 = set(list1)
    set2 = set(list2)
    set3 = set(list3)
    common_elements = set1.intersection(set2, set3)

    return common_elements

def min_value_in_combination(combination, price_list):
    min_value = float('inf')  # 设置一个初始值为正无穷大的最小值
    for idx, index_pair in enumerate(combination):
        # print(list(index_pair))
        index_pair = list(index_pair)
        price = price_list[index_pair[0]] + price_list[index_pair[1]]
        if price < min_value:
            min_value = price

    return min_value

if not got_low and not got_high:
    red_h = find_combinations_exceeding_x(r_num, rh)
    yellow_h = find_combinations_exceeding_x(y_num, yh)
    white_h = find_combinations_exceeding_x(w_num, wh)

    red_l = find_combinations_exceeding_x(r_num, rl)
    yellow_l = find_combinations_exceeding_x(y_num, yl)
    white_l = find_combinations_exceeding_x(w_num, wl)
    
    combination_high = get_set(red_h, yellow_h, white_h)
    combination_low = get_set(red_l, yellow_l, white_l)
    print(combination_low, combination_high)

    if len(red_h) != 0 and len(yellow_h) != 0 and len(white_h) != 0 and combination_high:
        print('high')
        got_high = True
        print(red_l, yellow_l, white_l, sep='\n')
        # combination = get_set(red_h, yellow_h, white_h)
        print(combination_low)
        print()
        min_price_h = min_value_in_combination(combination_high, price)
        print(min_price_l)

    elif len(red_l) != 0 and len(yellow_l) != 0 and len(white_l) != 0 and combination_low:
        print('low')
        got_low = True
        print(red_l, yellow_l, white_l, sep='\n')
        # combination = get_set(red_l, yellow_l, white_l)
        print(combination_low)
        print()
        min_price_l = min_value_in_combination(combination_low, price)
        print(min_price_l)

if got_high:
    print(min_price_h)
elif got_low:
    print(min_price_l)
else:
    print(sum(price))
        

