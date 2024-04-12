# max condition is only buy one item with maximum num(ex: budget // price_happiness + 1)
# +1 for the equivalent condition
def within_budget(i, j, price_happiness, price_heart, budget):
    is_within_budget = False
    total_price = i * price_happiness + j * price_heart
    if total_price <= budget:
        is_within_budget = True
    return is_within_budget

def meet_one_req(i, j, happy_flower, heart_flower, price_happiness, price_heart, budget, requirement):
    happy_red, happy_white, happy_yellow = happy_flower
    true_red, true_white, true_yellow = heart_flower
    red_min, white_yellow_min, red3_white_min = requirement

    total_price = i * price_happiness + j * price_heart

    red = happy_red * i + true_red * j
    white = happy_white * i + true_white * j
    yellow = happy_yellow * i + true_yellow * j

    if red >= red_min or (white + yellow) >= white_yellow_min or (red*3 + white) >= red3_white_min:
        return total_price
    else:
        return budget + 1


happy_flower = [5,10,4]
heart_flower = [3,6,2]
requirement = [200,100,50]
budget = 6000

strategy = 0
price_happiness = 800
price_heart = 1000

min_price = budget + 1
counter = 0

for i in range(budget // price_happiness + 1):
    for j in range(budget // price_heart + 1):
        if within_budget(i, j, price_happiness, price_heart, budget) == True:
            counter += 1
            price = meet_one_req(i, j, happy_flower, heart_flower, price_happiness, price_heart, budget, requirement)
            if price < min_price:
                min_price = price

print(counter, min_price)
