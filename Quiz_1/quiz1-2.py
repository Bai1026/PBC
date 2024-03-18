# number = list(map(int, input().split(',')))
# red = number[0]
# white = number[1]
# yellow = number[2]

# red_min = number[3]
# white_yellow_min = number[4]
# red3_white_min = number[5]

# better way to employ the input
red, white, yellow, red_min, white_yellow_min, red3_white_min = map(int, input().split(','))

enough_1 = False
enough = False
count = 0
# count_2 = 0

output = 0
output_2 = 0

while not enough:
    count += 1
    red_num = red * count
    white_num = white * count
    yellow_num = yellow * count

    if (red_num >= red_min or white_num + yellow_num >= white_yellow_min or red_num * 3 + white_num >= red3_white_min) and not enough_1:
        enough_1 = True
        output = count

    if red_num >= red_min and white_num + yellow_num >= white_yellow_min and red_num * 3 + white_num >= red3_white_min:
        output_2 = count
        enough = True

print(output, output_2, sep=',')

# # print(count)

# enough = False
# count_2 = 0

# while not enough:
#     count_2 += 1
#     red_num = red * count_2
#     white_num = white * count_2
#     yellow_num = yellow * count_2

#     if red_num >= red_min and white_num + yellow_num >= white_yellow_min and red_num * 3 + white_num >= red3_white_min:
#         enough = True

# # print(count_2)
# print(f"{count},{count_2}")