red = int(input())
white = int(input())
yellow = int(input())

red_min = int(input())
white_yellow_min = int(input())
red3_white_min = int(input())

bundle = 1
red_ori = red
white_ori = white
yellow_ori = yellow

while red < red_min and (white + yellow) < white_yellow_min and (red*3 + white) < red3_white_min:
    red += red_ori
    white += white_ori
    yellow += yellow_ori
    # print(red, white, yellow)
    # print()
    bundle += 1

print(bundle)