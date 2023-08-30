def hash(n,arr,find):
    d=dict.fromkeys(arr,0)
    for i in range(n):
        d[arr[i]]+=1
    return d[find]
n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
find=int(input())
result=hash(n,arr,find)
print(result)