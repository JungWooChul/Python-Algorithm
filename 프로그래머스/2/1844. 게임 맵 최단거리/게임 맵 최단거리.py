from collections import deque
def solution(maps):
    visited = [[False]*len(maps[0]) for _ in range(len(maps))]
    
    # 상, 하, 좌, 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque()
    queue.append((0,0))
    
    visited[0][0] = 1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if (0 <= nx < len(maps)) and (0 <= ny < len(maps[0])) and maps[nx][ny]!=0 and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y]+1
                queue.append((nx,ny))
    
    return -1 if not visited[-1][-1] else visited[-1][-1]