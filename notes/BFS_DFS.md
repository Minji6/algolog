# BFS/DFS

구분: 개인  
Tags: 공부

# BFS/DFS - 그래프 탐색 알고리즘

**탐색**: 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정

## 스택

먼저 들어온 데이터가 나중에 나감 → **선입후출**
- ex) 상자 쌓기, 상자 빼기
- 입구와 출구가 동일하다.

```python
append()  # 값 추가
pop()     # 값 삭제
```

## 큐

먼저 들어온 데이터가 먼저 나감 → **선입선출**
- ex) 대기줄

```python
# 큐 사용 라이브러리
# 리스트보다 시간이 훨씬 적게 걸리므로 라이브러리를 사용하는 것을 권장
from collections import deque
append()   # 값 추가
popleft()  # 값 삭제
```

## 재귀 함수

**자기 자신을 호출하는 함수**
- 코테에서는 꼭! 종료 조건을 명시해야 한다.
- ex) 팩토리얼, 최대공약수(유클리드 호제법) GCD(192,162)
- DFS를 구현할 때 자주 사용한다.
- 스택 사용할 때 구현상 스택 라이브러리 대신 재귀함수로 구현하기도 한다.

```python
def recursive_function():
    print('재귀 함수를 호출합니다')
    recursive_function()
    
recursive_function()
```

---

## DFS(Depth First Search)

**깊이 우선 탐색**
- 그래프에서 깊은 부분을 우선적으로 탐색
- DFS는 스택 자료구조 혹은 재귀 함수를 이용한다.
- → 한 놈만 끝까지 판다

### 알고리즘

1. 탐색 시작 노드를 스택에 삽입 후 방문 처리
2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문 처리  
   방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드 꺼냄
3. 더 이상 2번 과정을 수행할 수 없을 때까지 탐색

```python
# dfs 메서드 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],      # 0번째 인덱스는 사실 의미가 없음
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 각 노드가 방문한 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)
```

## BFS(Breadth First Search)

**너비 우선 탐색**
- 가까운 노드부터 탐색하는 알고리즘
- 큐 사용
- 인접한 노드가 여러 개 있을 때 가장 작은 숫자부터 탐색

```python
from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)
```
