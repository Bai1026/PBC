# 讀取輸入值
input_values = input().split(",")
a, b, c = int(input_values[0]), int(input_values[1]), int(input_values[2])

# 檢查是否滿足等式 ab = c
if a * b == c:
    print(c)  # 如果滿足，輸出 c 的值
# 檢查是否滿足等式 ac = b
elif a * c == b:
    print(b)  # 如果滿足，輸出 b 的值
# 檢查是否滿足等式 bc = a
elif b * c == a:
    print(a)  # 如果滿足，輸出 a 的值
else:
    # 若沒有任何等式成立，輸出 a、b、c 三數相乘的結果
    print(a * b * c)
