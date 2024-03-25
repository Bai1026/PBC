# 讀取輸入值，包括總部門經理數量、經驗值下限、專業度下限和總和下限
input_values = input().split(",")
manager_count, experience_threshold, proficiency_threshold, sum_threshold = int(input_values[0]), int(input_values[1]), int(input_values[2]), int(input_values[3])

# 讀取部門經理的經驗值列表
experience_values = input().split(",")
experiences = [int(value) for value in experience_values]

# 讀取部門經理的專業度列表
proficiency_values = input().split(",")
proficiencies = [int(value) for value in proficiency_values]

# 初始化一個空列表來儲存符合條件的部門經理編號
qualified_manager_indices = []

# 檢查每位部門經理是否同時滿足經驗值和專業度的下限
for index in range(manager_count):
    if experiences[index] >= experience_threshold and proficiencies[index] >= proficiency_threshold:
        # 如果符合條件，將部門經理的編號加入到列表中
        qualified_manager_indices.append(str(index + 1))

# 如果找到符合條件的部門經理，則輸出其編號
if qualified_manager_indices:
    print(','.join(qualified_manager_indices))
else:
    # 如果沒有符合經驗值和專業度下限的部門經理，則檢查經驗值和專業度總和是否達到總和下限
    qualified_manager_indices = [str(index + 1) for index in range(manager_count) if experiences[index] + proficiencies[index] >= sum_threshold]
    if qualified_manager_indices:
        print(','.join(qualified_manager_indices))
    else:
        # 如果仍然沒有找到符合任何條件的部門經理，則輸出0
        print(0)
