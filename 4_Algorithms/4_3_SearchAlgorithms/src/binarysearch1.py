# https://programmers.co.kr/learn/courses/30/lessons/43238

def solution(n, times):
    left = min(times)
    right = max(times) * n
    
    while left < right:
        mid = (left + right) // 2
        possible = 0
        for time in times:
            possible += mid // time
        if possible >= n:
            answer = mid
            right = mid
        else:
            left = mid + 1
    
    return answer
