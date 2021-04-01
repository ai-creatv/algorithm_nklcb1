# 탐색 알고리즘 (Search Algorithms)

## 탐색 알고리즘이란

- 자료구조에서 원하는 조건에 맞는 자료를 찾는 것을 탐색 알고리즘이라 한다.
- 자료가 정렬되어 있는지 여부에 따라 크게 두 가지 방법으로 나뉜다.

## 선형 탐색 (Linear Search)

![선형 탐색](img/1.png)

- 순차 탐색(Sequential search)라고도 부르며, 가장 단순한 탐색 알고리즘이다.
- 순서대로 하나씩 비교하며, 시간복잡도는 O(N)이다.

## 이분 탐색 (Binary Search)

![이분 탐색](img/2.png)

- 이진 탐색이라고도 부르며, 정렬된 자료의 탐색에 가장 많이 사용하는 알고리즘이다.
- 탐색 범위를 절반씩 줄여가며, 시간복잡도는 O(logN)이다.

## [실습] 이분 탐색 구현

```python
def solution(array, target_value):
    answer = 0
    return answer
```

- 이분 탐색을 이용하여 배열에서 target_value를 찾아, 값의 index를 반환하시오.
- target_value를 찾지 못하면 -1을 반환하시오.

## [실습] 이분 탐색 문제 - 1

- [프로그래머스 입국심사 문제](https://programmers.co.kr/learn/courses/30/lessons/43238)

## [실습] 이분 탐색 문제 - 2

- [프로그래머스 징검다리 문제](https://programmers.co.kr/learn/courses/30/lessons/43236)
