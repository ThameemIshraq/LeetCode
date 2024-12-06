from typing import List
def kthDistinct(arr: List[str], k: int) -> str:
    if arr is None or len(arr) == 0 or k <= 0:
        return ""   
    alreadyvisited:List[str] = []
    kthDistinct:List[str] = []
    distinctindex=0
    for i in range(len(arr)):
        if arr.count(arr[i]) == 1 and arr[i] not in alreadyvisited:
           kthDistinct.append(arr[i])
           distinctindex+=1
           alreadyvisited.append(arr[i])
    if k > len(kthDistinct):
        return ""
    else:
        return kthDistinct[k-1]
    

print(kthDistinct(["d","b","c","b","c","a"],2))