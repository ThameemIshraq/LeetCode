def maxLength(arr: list[str]) -> int:
    for j in range(len(arr)):
        possiblestring:str=arr[j]
        for i in range(j,len(arr)):
            set1 = set(possiblestring)
            if i < len(arr)-1:
                set2 = set(arr[i+1])
                if bool(set1.intersection(set2)) == False:
                    possiblestring += arr[i+1]
    
    return len(possiblestring)

def getMaxLength(startposition:int,arr:list[str]) -> int:
    possiblestring:str=arr[startposition]
    for i in range(startposition,len(arr)):
        set1 = set(possiblestring)
        if i < len(arr)-1:
            set2 = set(arr[i+1])
            if bool(set1.intersection(set2)) == False:
                possiblestring += arr[i+1]

print(maxLength(["cha","r","act","ers"]))
