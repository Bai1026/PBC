price = list()

for i in range(3):
    price.append(int(input()))

num = list()

for i in range(2):
    num.append(int(input()))

number = sum(num)

total_price = price[0] + price[1]*num[0] + price[2]*num[1]

print(f"{number},{total_price},{total_price%10}")