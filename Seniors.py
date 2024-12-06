from typing import List
def countSeniors(details: List[str]) -> int:
    seniorsCount=0
    for i in range(len(details)):
        age  = int(details[i][11:13])
        if(age>60):
            seniorsCount+=1
    return seniorsCount

print(countSeniors(["7868190130M7522","5303914400F9211","9273338290F4010"]))