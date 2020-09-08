def UsingOwnFunction(arr):
    mp = dict()
    ans = list()
    for i in arr:
        if(i not in mp):
            ans.append(i)
            mp[i] = 1
    return ans
    
arr = list(map(int, input().split()))

ans = UsingOwnFunction(arr)

print(ans)
