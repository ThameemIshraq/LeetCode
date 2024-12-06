class Solution:
    acount,bcount,ccount,sum=0,0,0,0
    def takeCharacters(self, s: str, k: int) -> int:
        N=len(s)
        if  N < k*3: return -1
        l,r=0,N-1
        while(l<r):
            self.countchars(l,s)
            l += 1
            if self.acount == k and self.bcount ==k and self.ccount == k: return sum
            self.countchars(r,s)
            r -=1
            if self.acount == k and self.bcount ==k and self.ccount == k: return sum
        
        return -1
    
    def countchars(self,index:int,s:str):
         char =s[index]
         if char == 'a': self.acount+=1
         if char == 'b': self.bcount+=1
         if char == 'c': self.ccount+=1
         self.sum += 1
sol = Solution()
countcharacters = sol.takeCharacters("aabaaaacaabc",2)