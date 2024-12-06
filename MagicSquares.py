from typing import List

def isMagic(a, b, c, d, e, f, g, h, i): 
        s1 = set([a, b, c, d, e, f, g, h, i]) 
        s2 = set([1, 2, 3, 4, 5, 6, 7, 8, 9]) 
    
        # Elements of grid must contain all numbers 
        # from 1 to 9, sum of all rows, columns and 
        # diagonals must be same, i.e., 15. 
        if (s1 == s2 and (a + b + c) == 15 and
        (d + e + f) == 15 and (g + h + i) == 15 and
        (a + d + g) == 15 and (b + e + h) == 15 and
        (c + f + i) == 15 and (a + e + i) == 15 and
        (c + e + g) == 15): 
            return True
            
        return False  
def numMagicSquaresInside(grid: List[List[int]]) -> int:
    rows = len(grid)   
    cols = len(grid[0])
    count = 0
    if rows < 3 or cols < 3:
        return 0    
    for i in range(rows - 2):
        for j in range(cols - 2):
            if grid[i + 1][j + 1] != 5:
                continue
            if (isMagic(grid[i][j], grid[i][j + 1], 
                  grid[i][j + 2], grid[i + 1][j], 
                  grid[i + 1][j + 1], grid[i + 1][j + 2], 
                  grid[i + 2][j], grid[i + 2][j + 1], 
                  grid[i + 2][j + 2]) == True): 
                
                count +=1
    
   
    return count

print(numMagicSquaresInside([[4,3,8,4],[9,5,1,9],[2,7,6,2]]))