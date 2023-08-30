def triplets(n, t, arr):
    result = []
    arr.sort()
    for i in range(n-2):
        current_sum = arr[i]
        start = i+1
        end = n-1
        while start < end:
            tsum = arr[start]+arr[end]
            if current_sum+tsum == t:
                result.append([current_sum, arr[start], arr[end]])
                start += 1
                end -= 1
            elif current_sum+tsum < t:
                start += 1
            else:
                end -= 1
    return result


n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
t = int(input())
result = triplets(n, t, arr)
print(result)
