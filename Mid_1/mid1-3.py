n, x0 = map(int, input().split(','))
num = list(map(int, input().split(',')))

pair = set()

def count_pairs_with_product(lst, target):
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] * lst[j] == target:
                count += 1
    return count

pairs_count = count_pairs_with_product(num, x0)
print(pairs_count)
