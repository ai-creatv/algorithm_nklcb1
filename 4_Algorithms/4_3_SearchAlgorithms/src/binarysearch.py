# https://programmers.co.kr/learn/courses/30/lessons/43236

def solve(target, max_dist, rocks):
    removed = 0
    min_dist = max_dist
    for rock in rocks[::-1]:
        diff = max_dist - rock
        if diff < target:
            removed += 1
        else:
            min_dist = diff
            break
    
    current = 0
    if removed > 0:
        rocks = rocks[:-removed]

    for rock in rocks:
        diff = rock - current
        if diff < target:
            removed += 1
        else:
            current = rock
            min_dist = min(min_dist, diff)
    
    return removed, min_dist


def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    left, right = 1, distance
    
    while left <= right:
        mid = (left + right) // 2
        
        removed, min_dist = solve(mid, distance, rocks)
        
        if removed > n:
            right = mid  - 1
        else:
            answer = max(min_dist, answer)
            left = mid + 1
    
    return answer