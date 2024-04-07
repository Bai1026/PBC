# item_cnt: integer
# minutes: a list of item_cnt integers 
# prices: a list of item_cnt integers
# return the two most profitable product index
# if tie, let the smallest index be the first
def best_product_info(item_cnt, minutes, prices):
    '''TODO'''
    ratios = []
    for i in range(item_cnt):
        ratios.append(prices[i]/minutes[i])
  
    sorted_ratios = sorted(ratios)

    max_list = []
    for i in range(item_cnt):
        if ratios[i] == sorted_ratios[-1]:
            max_list.append(i)
    # print(max_list)

    # both +1 since it's starts from 1 ot n
    if len(max_list) > 1:
        best_index = max_list[0] + 1
        second_best_index = max_list[1] + 1
    else:
        best_index = ratios.index(sorted_ratios[-1]) + 1
        second_best_index = ratios.index(sorted_ratios[-2]) + 1   
    
    # print(ratios)
    return best_index, second_best_index

# input
item_cnt, capacity_1 , capacity_2 = [int(x) for x in input().split(",")]
minutes = [int(x) for x in input().split(",")]
prices = [int(x) for x in input().split(",")]

# call function and calculate the answer
# best_product_info(item_cnt, minutes, prices)
best_index, second_best_index = best_product_info(item_cnt, minutes, prices)
revenue = prices[best_index-1] * (capacity_1//minutes[best_index-1]) + prices[second_best_index-1] * (capacity_2//minutes[second_best_index-1])

# print
print(best_index, second_best_index, revenue, sep = ",")
