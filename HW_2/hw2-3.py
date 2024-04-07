happy_red = int(input())
happy_white = int(input())
happy_yellow = int(input())

true_red = int(input())
true_white = int(input())
true_yellow = int(input())

red_min = int(input())
white_yellow_min = int(input())
red3_white_min = int(input())

budget = int(input())

strategy = 0
happy_price = 800
true_price = 1000
# assign inf for futher min price test
min_price = float('inf')

# max condition is only buy one item with maximum num(ex: budget // happy_price + 1)
# +1 for the equivalent condition
for happy_num in range(budget // happy_price + 1):
    for true_num in range(budget // true_price + 1):
        total_price = happy_num * happy_price + true_num * true_price
        if total_price <= budget:
            strategy += 1

        red = happy_red * happy_num + true_red * true_num
        white = happy_white * happy_num + true_white * true_num
        yellow = happy_yellow * happy_num + true_yellow * true_num

        # fit either condition
        if red >= red_min or (white + yellow) >= white_yellow_min or (red*3 + white) >= red3_white_min:
            if total_price < min_price:
                min_price = total_price

# did not find any valid solution
if min_price == float('inf'):
    min_price = -1

print(strategy, min_price, sep=',')