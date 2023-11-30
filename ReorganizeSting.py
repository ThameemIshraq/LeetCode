class Solution:
    def max_frequency_char(frequency_dict):
        max_char = None
        max_frequency = 0
        for char, frequency in frequency_dict.items():
            if frequency > max_frequency:
                max_frequency = frequency
                max_char = char
    
        return max_char, max_frequency

    def reorganizeString(self, s: str) -> str:
        frquency_dict={}
        for char in s:
            if char in frquency_dict:
                frquency_dict[char]+=1
            else:
                frquency_dict[char]=1
        
        max_char, max_frequency = Solution.max_frequency_char(frquency_dict)
        if max_frequency > (len(s)+1)//2:
            return ""
        res=[None]*len(s)
        index=0
        while max_frequency>0:
            res[index]=max_char
            index+=2
            max_frequency-=1
        frquency_dict[max_char]=0
        for char, frequency in frquency_dict.items():
            while frequency>0:
                if index>=len(s):
                    index=1
                res[index]=char
                index+=2
                frequency-=1
        return "".join(res)
