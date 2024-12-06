from collections import Counter

def minimumPushes(word: str) -> int:
    collection = Counter(word).most_common()
    value:int =0
    multiplervalue:int =1
    multipliercounter:int =1
    for item in collection:
       value += item[1]*multiplervalue
       multipliercounter +=1    
       if multipliercounter > 8:
           multiplervalue +=1
           multipliercounter =1
    return value    
     

print(minimumPushes("aabbccddeeffgghhiiiiii")) # 3