int_list = list(map(int, input().split(',')))

if int_list[0] * int_list[1] == int_list[2]:
    print(int_list[2])
elif int_list[0] * int_list[2] == int_list[1]:
    print(int_list[1])
elif int_list[1] * int_list[2] == int_list[0]:
    print(int_list[0])
else:
    print(int_list[0] * int_list[1] * int_list[2])
