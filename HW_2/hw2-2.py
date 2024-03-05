red_price = int(input())
white_price = int(input())
price_limit = int(input())

max_score = 0
red = 0
white = 0

for r in range(101):
    for w in range(76):
        score = (200-r)*r + (300-2*w)*w
        if score > max_score and r >= 2*w and (r*red_price + w*white_price) <= price_limit:
            max_score = score
            red = r
            white = w

print(max_score)