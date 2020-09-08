def UsingInBuiltFunction(arr):
    ans = list(dict.fromkeys(arr))
    return ans
arr = list(map(int, input().split()))
ans = UsingInBuiltFunction(arr)
print(ans)
