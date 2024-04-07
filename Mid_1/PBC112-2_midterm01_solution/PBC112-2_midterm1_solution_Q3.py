# 讀取輸入值
row1 = input().split(",")
n, x0 = int(row1[0]), int(row1[1])

# 處理接下來的一行，將其轉換為整數列表
x_input = input().split(",")
x = [int(num) for num in x_input]


# 初始化一個計數器用於記錄符合條件的數對數量
count = 0

# 遍歷所有可能的數對組合
for i in range(n):
    for j in range(i+1, n):  # 確保 j > i
        if x[i] * x[j] == x0:
            count += 1  # 如果乘積等於 x0，則符合條件

# 輸出符合條件的數對數量
print(count)
