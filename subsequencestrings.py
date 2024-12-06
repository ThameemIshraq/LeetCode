class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        str1len = len(str1)
        str2len = len(str2)
        str1startindex=0
        if str2len > str1len: return False
        for str2index in range(0,str2len):
            str2char = str2[str2index]
            found=False
            for str1index in range(str1startindex,str1len): 
                str1char = str1[str1index]
                previouschar = chr((ord(str2char) - ord('a') - 1) % 26 + ord('a'))
                if str1char == str2char or str1char == previouschar:
                    str1startindex = str1index+1
                    found = True
                    break
            if found == False: return False
        return True

sol = Solution()
print(sol.canMakeSubsequence("ab","d"))