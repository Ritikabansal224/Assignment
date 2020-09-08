def flattenArray(inputArray):      
    flatList = []
    for item in inputArray:        
        flatList += item if type(item) is list else [item]
    return flatList

print(flattenArray([1,2,3,[4,5],6,[7,8],9]))
