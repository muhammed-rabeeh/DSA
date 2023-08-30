#hashing implementation on integer

# def hash(n,arr,find):
#     hash=[0]*10
#     for i in range(n):
#         hash[arr[i]]+=1
#     return hash[find]
# n=int(input())
# arr=[]
# for i in range(n):
#     arr.append(int(input()))
# find=int(input())
# result=hash(n,arr,find)
# print(result)

#hashing implementation on character

def hash(n,arr,find):
    hash=[0]*26
    for i in range(n):
        hash[ord(arr[i])-ord('a')]+=1
    return hash[ord(find)-ord('a')]
arr=input()
n=len(arr)
find=input()
result=hash(n,arr,find)
print(result)