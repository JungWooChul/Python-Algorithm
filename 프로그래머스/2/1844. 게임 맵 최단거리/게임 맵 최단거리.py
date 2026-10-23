from collections import deque
def solution(maps):
    directions = [
        (0, 1),   # 오른쪽
        (0, -1),  # 왼쪽
        (1, 0),   # 아래
        (-1, 0)   # 위
    ]
    visited = [[-1]*len(maps[0]) for _ in range(len(maps))]
    visited[0][0] = 1
    queue = deque([(0,0)])
    while queue:
        x,y = queue.popleft()
        if x == len(maps)-1 and y == len(maps[0])-1:
            return visited[x][y]
        for dx,dy in directions:
            if (0 <= x+dx < len(maps)) and (0 <= y+dy < len(maps[0])) and maps[x+dx][y+dy] == 1 and visited[x+dx][y+dy] == -1:
                visited[x+dx][y+dy] = visited[x][y] + 1
                queue.append([x+dx,y+dy])
    print(visited)
    return visited[len(maps)-1][len(maps[0])-1]