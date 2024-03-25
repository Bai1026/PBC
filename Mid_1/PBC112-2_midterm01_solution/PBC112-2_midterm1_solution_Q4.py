# 讀取花束總數
bouquet_count = int(input())

# 讀取紅玫瑰、黃玫瑰、白玫瑰及花束價格的值
red_roses_input = input().split(",")
red_roses = [int(num) for num in red_roses_input]

yellow_roses_input = input().split(",")
yellow_roses = [int(num) for num in yellow_roses_input]

white_roses_input = input().split(",")
white_roses = [int(num) for num in white_roses_input]

prices_input = input().split(",")
prices = [int(num) for num in prices_input]

# 讀取告白成功的可能性門檻值
acceptance_thresholds_input = input().split(",")
likely_acceptance_red, highly_likely_acceptance_red = int(acceptance_thresholds_input[0]), int(acceptance_thresholds_input[1])

acceptance_thresholds_input = input().split(",")
likely_acceptance_yellow, highly_likely_acceptance_yellow = int(acceptance_thresholds_input[0]), int(acceptance_thresholds_input[1])

acceptance_thresholds_input = input().split(",")
likely_acceptance_white, highly_likely_acceptance_white = int(acceptance_thresholds_input[0]), int(acceptance_thresholds_input[1])

# 初始化最小花費
minimum_cost = 9999999999

# 尋找滿足告白成功高門檻的最小花費組合
for i in range(bouquet_count):
    for j in range(i, bouquet_count+1):
        # 計算選擇單束或兩束花束時的總花朵數和花費
        if j == bouquet_count:  # 單束花束情況
            total_red = red_roses[i]
            total_yellow = yellow_roses[i]
            total_white = white_roses[i]
            total_cost = prices[i]
        else:  # 兩束花束情況
            total_red = red_roses[i] + red_roses[j]
            total_yellow = yellow_roses[i] + yellow_roses[j]
            total_white = white_roses[i] + white_roses[j]
            total_cost = prices[i] + prices[j]

        # 檢查是否達到高門檻
        if total_red >= highly_likely_acceptance_red and total_yellow >= highly_likely_acceptance_yellow and total_white >= highly_likely_acceptance_white:
            minimum_cost = min(minimum_cost, total_cost)

# 如果沒有找到符合高門檻的組合，則檢查低門檻
if minimum_cost == 9999999999:
    for i in range(bouquet_count):
        for j in range(i, bouquet_count+1):
            if j == bouquet_count:  # 單束花束情況
                total_red = red_roses[i]
                total_yellow = yellow_roses[i]
                total_white = white_roses[i]
                total_cost = prices[i]
            else:  # 兩束花束情況
                total_red = red_roses[i] + red_roses[j]
                total_yellow = yellow_roses[i] + yellow_roses[j]
                total_white = white_roses[i] + white_roses[j]
                total_cost = prices[i] + prices[j]

            # 檢查是否達到低門檻
            if total_red >= likely_acceptance_red and total_yellow >= likely_acceptance_yellow and total_white >= likely_acceptance_white:
                minimum_cost = min(minimum_cost, total_cost)

# 如果沒有任何組合符合門檻，則考慮購買所有花束
if minimum_cost == 9999999999:
    minimum_cost = sum(prices)

# 輸出最終需要的最小花費
print(minimum_cost)
