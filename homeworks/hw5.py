def find_pair_with_sum(arr, target_sum):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target_sum:
                return (arr[i], arr[j])
    return None

arr = [10, 15, 3, 7]
target_sum = 17
pair = find_pair_with_sum(arr, target_sum)
if pair:
    print(f"Найдена пара: {pair}")
else:
    print("Пара не найдена")
