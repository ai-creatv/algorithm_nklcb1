# 그래프 (Graph)

## 그래프란

![그래프](img/1.png)

- 객체 간에 짝을 이루는 구조를 나타내기 위한, 가장 유연한 자료 구조
- Vertex(Node, Point)와 이를 잇는 Edge로 구성되어 있다.
- Edge는 무향(Undirected) 또는 유향(Directed)일 수 있다.
- Edge에는 가중치(Weight)가 있을 수 있으며, 이는 연결의 강도를 나타낸다.

## 그래프와 트리의 관계

![트리](img/2.png)

- 트리는 방향성 비순환 그래프 DAG (Directed Acyclic Graph)의 일종으로 볼 수 있다.
  - 트리에는 회로(Cycle)이 없으며, 루트에서 리프 노드로의 방향성(Direction)이 존재한다.

## 그래프의 종류

![그래프의 종류](img/3.png)

- 무향 그래프 (Undirected Graph)
- 유향 그래프 (Directed Graph)
- 다중 그래프 (Multigraph)

## 그래프의 관련 용어

![그래프의 부분 구조](img/4.png)

- 경로 (Path)
- 회로 (Cycle)
- 부분 그래프 (Subgraph) - 어떤 그래프에 속하는 그래프
- 연결 그래프 (Connected Graph) - 임의의 두 Vertex 사이에 경로가 존재하는 그래프

## 그래프의 구현 방법

- 인접 리스트 (Adjacency List) - Sparse할 경우 유리함
![인접 리스트](img/5.png)
- 인접 행렬 (Adjacency Matrix) - Dense할 경우 유리함
![인접 행렬](img/6.png)

## 그래프의 탐색 방법

- 너비 우선 탐색 (Breadth-First Search)
![BFS](img/7.png)
  - 두 Vertex 사이의 최단 경로 or 임의의 경로를 찾을 때 사용
  - 트리와 달리 특정 Node의 방문 여부 `visited`를 검사해야 함
  - Queue를 이용하여 반복적(Iterative)인 방법으로 손쉽게 구현 가능
- 깊이 우선 탐색 (Depth-First Search)
![DFS](img/8.png)
  - 모든 Vertex를 방문하고자 할 때 주로 사용 (순회)
  - 트리와 달리 특정 Node의 방문 여부 `visited`를 검사해야 함
  - 재귀(Recursive) 함수를 이용하여 전위 순회의 형태로 구현

## [실습] 인접 리스트 기반 그래프 구현하기

- Python의 `list`와 `class`를 이용해 직접 구현하기
- **구현 조건**
  - `class`와 `list`를 이용하여 그래프를 구현한다.
  - 그래프의 Vertex 삽입을 구현한다.
    - Vertex 삽입 시, 연결될 인접점(Adjacency Vertices)를 입력 받는다
    - 각 Vertex에 인접 리스트를 이용하여 인접점을 표현한다.
  - 다음과 같은 그래프의 연산을 구현한다.
    - 순회 알고리즘: 시작 Vertex를 입력받고 모든 Vertex를 순회하고, 그 순서를 출력한다.
      1. 너비 우선 순회 (Breadth-First Traversal)
      1. 깊이 우선 순회 (Depth-First Traversal)
- **참조 코드**
  - [기반 소스 코드](src/before.py)
  - [솔루션 코드](src/after.py)
