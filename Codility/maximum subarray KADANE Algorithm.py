def solution(A):
    m = A[0]
    s= 0
    for i in range(0, len(A)):
        s +=A[i]
        m = max(m,s)
        if s<0:
            s=0
    return m

solution([1,2,-3,4,6])
