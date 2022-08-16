def solution(N):
    for i in range(int(N**0.5), 0, -1):
        if N%i == 0:
            return int(2*(i+N/i))
