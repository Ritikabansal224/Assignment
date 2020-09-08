def UsingOwnFunction(data):
    data = list(data)
    i = 0
    j = len(data) - 1
    while(i < j):
        temp = data[i]
        data[i] = data[j]
        data[j]=temp
        i+=1
        j-=1
        ans=""
        ans=ans.join(data);
        return ans
data = input()
ans=UsingOwnFunction(data)
print(ans)
