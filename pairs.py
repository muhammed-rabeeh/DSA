def pair(s,a):
    o=[]
    for i in a:
        if s-i in a:
            o.append(i)
            o.append(s-i)
            break
    return o
n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
s=int(input())
result=pair(s,arr)
print(result)