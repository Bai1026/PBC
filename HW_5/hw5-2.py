# happy_red = int(input())
# happy_white = int(input())
# happy_yellow = int(input())

# true_red = int(input())
# true_white = int(input())
# true_yellow = int(input())

# red_min = int(input())
# white_yellow_min = int(input())
# red3_white_min = int(input())

# budget = int(input())

strategy = 0
price_happiness = 800
price_heart = 1000
# assign inf for futher min price test
min_price = float('inf')

# max condition is only buy one item with maximum num(ex: budget // price_happiness + 1)
# +1 for the equivalent condition
def within_budget(i, j, price_happiness, price_heart, budget):
    is_within_budget = False
    total_price = i * price_happiness + j * price_heart
    if total_price <= budget:
        is_within_budget = True
    return is_within_budget

def meet_one_req(i, j, happy_flower, heart_flower, price_happiness, price_heart, budget, requirement):
    happy_red, happy_white, happy_yellow = map(int, happy_flower.split(','))
    true_red, true_white, true_yellow = map(int, heart_flower.split(','))
    red_min, white_yellow_min, red3_white_min = map(int, requirement.split(','))

    total_price = i * price_happiness + j * price_heart

    red = happy_red * i + true_red * j
    white = happy_white * i + true_white * j
    yellow = happy_yellow * i + true_yellow * j

    if red >= red_min or (white + yellow) >= white_yellow_min or (red*3 + white) >= red3_white_min:
        return total_price
    else:
        return budget + 1

# print(strategy, min_price, sep=',')