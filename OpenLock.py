from typing import List
from collections import deque
def openLock(deadends: List[str], target: str) -> int:
    deadends = set(deadends)
    if "0000" in deadends: return -1
    q = deque([("0000",0)])
    visited = set()
    while q:
        cand, steps = q.popleft()
        if cand == target: return steps
        for i in range(4):
            updigit = ((int(cand[i])+1)%10)
            downdigit = ((int(cand[i])-1)%10)
            for digit in [updigit,downdigit]:
                nx = cand[:i]+str(digit)+cand[i+1:]
                if nx not in deadends and nx not in visited:
                    visited.add(nx)
                    q.append((nx,steps+1))
    
    return -1

reqsteps  = openLock(["0201","0101","0102","1212","2002"],"0202")
print(reqsteps)