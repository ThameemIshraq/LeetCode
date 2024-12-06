from typing import List

def maxProfitAssignment(difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        sorted_list = list(sorted(zip(difficulty, profit)))
        length = len(sorted_list)
        mid = int(length//2)
        mid_value = sorted_list[mid][0]
        start_index, end_index = 0,0
        valuestore ={}  
        worker.sort()  
        total_worker_value = 0 
        for w in worker:
            max_value = 0 
            if w in valuestore.keys():
                max_value = valuestore[w] 
            else:
                if w >= mid_value:
                    start_index = mid
                    end_index = length
                else:
                    start_index = 0
                    end_index = mid
                for x in range(start_index, end_index):
                    diff = sorted_list[x][0]
                    prof = sorted_list[x][1]
                    if diff > w:  
                        break
                    if diff <= w and prof > max_value: 
                        max_value = prof 
            total_worker_value += max_value 
            valuestore[w] = max_value 
        return total_worker_value 

maxProfitAssignment([68,35,52,47,86], [67,17,1,81,3], [92,10,85,84,82])
    