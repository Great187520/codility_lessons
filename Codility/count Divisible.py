def solution(A, B, K):
    c=int(B/K)-int(A/K)
    if (A%B==0):
        c=c+1
    return c
