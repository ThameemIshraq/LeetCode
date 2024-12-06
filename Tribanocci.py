def tribonacci(n: int) -> int:
    first,second,third = 0,1,1
    if n==0: return 2
    for i in range(3, n+1) :
        curr = first + second + third
        first = second
        second = third
        third = curr
    return curr   

n=10
print(tribonacci(n))