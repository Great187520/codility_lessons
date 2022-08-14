def solution(X, A):
    B = [-1] * X
    for i in range(0, len(A)):
        if(A[i]<=X and B[A[i]-1]==-1):
            B[A[i]-1]=i
    m=0
    for i in range(0, len(B)):
        if B[i]==-1:
            return -1
        m = max(m, B[i])
    return m
pass


def solution(X, A):
    B = [0]*X
    s=0
    for i in range(0, len(A)):
        if (B[A[i]- 1]==0 and A[1]<=X):
            s+=1
            B[A[i]-1]=1
        if(s==X):
            return i
    return -1
