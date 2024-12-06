from typing import List
def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        shorterarray, longerarray =[],[]
        if len(nums1) < len(nums2):
            shorterarray = nums1
            longerarray = nums2
        else:  
            shorterarray = nums2
            longerarray = nums1
        for i in shorterarray:
            if i in longerarray:
                result.append(i)
        return result

print(intersect([4,9,5], [9,4,9,8,4]))       

