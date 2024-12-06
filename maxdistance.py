from typing import List
def maxDistance(arrays: List[List[int]]) -> int:
    min_val, max_val,max_final = arrays[0][0],arrays[0][-1],0
    for array  in arrays[1:]:
        min_distance = abs(array[0] - max_val)
        max_distance = abs(array[-1] - min_val)
        max_final = max(max_final,min_distance,max_distance)
        min_val = min(min_val,array[0])
        max_val = max(max_val,array[-1])
    return max_distance

maxDistance([[1,2,3],[4,5],[1,2,3]])