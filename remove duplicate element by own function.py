def UsingOwnFunction(arr):
    mp = dict()
    a = list()
    for i in arr:
        if(i not in mp):
            ans.append(i)
            mp[i] = 1
    return a
    
arr = list(map(int, input().split()))

a = UsingOwnFunction(arr)

print(a)
