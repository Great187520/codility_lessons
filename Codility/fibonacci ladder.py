def solution(A,B):
    result=[0]*len(A)
    fib=[0]*(len(A)+2)
    fib[1]=1
    for i in range(2,len(A)+2):
        fib[i]=fib[i-1]+fib[i-2]
    for i in range(len(A)):
        result[i]=fib[A[i]+1]%(2**B[i])
        #result[i]=fib[A[i]+1]&(2**B[i]-1)
    return result
