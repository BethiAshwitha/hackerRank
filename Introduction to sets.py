def average(array):
    s=set(array)
    m=sum(s)/len(s)
    mn=round(m,3)
    return mn
n = int(input())
arr = list(map(int, input().split()))
result = average(arr)
print(result)
