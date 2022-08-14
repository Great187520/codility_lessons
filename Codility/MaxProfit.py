def solution(A):
    if A[0] == 0:
        return 0
    mymin = A[0]
    mymax = 0
    s = 0

    for i in range( 1, len(A)):
        if A[i] < mymin:
            mymin = A[i]
            s = 0
        else:
            s += (A[1]-A[i-1])
        if mymax<s:
            mymax = s
    return mymax
        
