number = list(map(int, input().split(',')))
# print(number)

out = [number[0]+number[1], number[1]+number[2]*2, number[0]*number[2]]

print(max(out))