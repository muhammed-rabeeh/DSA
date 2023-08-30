
def mountain(n, arr):
    largest = 0
    for i in range(1, n - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            left = i - 1
            right = i + 1

            while left > 0 and arr[left] > arr[left - 1]:
                left -= 1

            while right < n - 1 and arr[right] > arr[right + 1]:
                right += 1

            largest = max(largest, right - left + 1)
    return largest if largest >= 3 else 0

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
result = mountain(n, arr)
print(result)
