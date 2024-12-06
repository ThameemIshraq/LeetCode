def getLucky(s:str,k:int) -> int:
    c:str = ""
    for char in s:
      alphabeticPosition = ord(char) - 96
      c = c+str(alphabeticPosition)
    for i in range(k):
      c = str(sum([int(x) for x in c]))
    
    return int(c)
    
print(getLucky("iiii",1))