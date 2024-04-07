price = list()

for i in range(3):
    price.append(int(input()))


num = list()

for i in range(2):
    num.append(int(input()))

discount_1 = int(input())
discount_2 = int(input())

B_1 = int(input())
B_2 = int(input())

number = sum(num)

total_price = price[0] + price[1]*num[0] + price[2]*num[1]

# calculate the number of the flowers
if total_price >= discount_1 and total_price < discount_2:
    number += 2
elif total_price >= discount_1 and total_price >= discount_2:
    number += 5

if total_price >= B_1 and total_price <= B_2:
    total_price = B_1

output = str(number) + ',' + str(total_price)
print(output)
