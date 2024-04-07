# input the data we need
red_min = int(input())
white_min = int(input())

happy_red = int(input())
happy_white = int(input())
happy_price = int(input())

joy_red = int(input())
joy_white = int(input())
joy_price = int(input())

total_num = 0
total_price = 0

# buy lower
if happy_red >= red_min and happy_white >= white_min and joy_red >= red_min and joy_white >= white_min:
    if happy_price <= joy_price:
        total_num = happy_red + happy_white
        total_price = happy_price
    else:
        total_num = joy_red + joy_white
        total_price = joy_price

# buy happy one
elif happy_red >= red_min and happy_white >= white_min and (joy_red < red_min or joy_white < white_min):
    total_num = happy_red + happy_white
    total_price = happy_price

# buy joy one
elif (happy_red < red_min or happy_white < white_min) and joy_red >= red_min and joy_white >= white_min:
    total_num = joy_red + joy_white
    total_price = joy_price

# buy both
else:
    total_num += (happy_white + happy_red + joy_white + joy_red)
    total_price += (happy_price + joy_price)

# use sep = '' to control the output string
print(total_num, ',', total_price, sep='')