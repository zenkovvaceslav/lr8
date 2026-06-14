def first(n):
    ways = [0] * (n + 1)
    ways[1] = 1
    if n >= 2:
        ways[2] = 1
    if n >= 3:
        ways[3] = 2
    for i in range(4, n + 1):
        ways[i] = ways[i - 1] + ways[i - 2] + ways[i - 3]
    return ways[n]
def second(matric):
    stroka = len(matric)
    stolbec = len(matric[0])
    ways = [[0] * stolbec for _ in range(stroka)]
    ways[0][0] = matric[0][0]
    for i in range(1, stroka):
        ways[i][0] = ways[i - 1][0] + matric[i][0]
    for i in range(1, stolbec):
        ways[0][i] = ways[0][i - 1] + matric[0][i]
    for i in range(1, stroka):
        for j in range(1, stolbec):
            ways[i][j] = matric[i][j] + min(ways[i - 1][j], ways[i][j - 1])
    return ways[stroka - 1][stolbec - 1]
def third(coins, total):
    big = float('inf')
    ways = [0] + [big] * total
    for i in range(1, total + 1):
        for j in coins:
            if j <= i and ways[i - j] + 1 < ways[i]:
                ways[i] = ways[i - j] + 1
    return ways[total] if ways[total] != big else -1
def fourth(nums):
    if not nums:
        return 0
    ways = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i] and ways[j] + 1 > ways[i]:
                ways[i] = ways[j] + 1
    return max(ways)
def fifth(weights, values, limit):
    count = len(weights)
    ways = [[0] * (limit + 1) for _ in range(count + 1)]
    for i in range(1, count + 1):
        for j in range(limit + 1):
            ways[i][j] = ways[i - 1][j]
            if weights[i - 1] <= j:
                take = ways[i - 1][j - weights[i - 1]] + values[i - 1]
                if take > ways[i][j]:
                    ways[i][j] = take
    return ways[count][limit]
def main():
    print(first(6))
    matric = [[1, 2, 3], [4, 5, 6], [7,8, 9]]
    print(second(matric))
    print(third([1, 2, 3], 4))
    print(third([2], 3))
    print(fourth([1, 2, 3, 4, 5, 6, 7, 8]))
    weights = [1, 2, 3, 4]
    values = [5, 6, 7, 8]
    print(fifth(weights, values, 9))
if __name__ == "__main__":
    main()