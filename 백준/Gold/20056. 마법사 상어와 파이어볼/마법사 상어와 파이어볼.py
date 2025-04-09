import sys
from collections import deque, defaultdict
input = sys.stdin.readline

N, M, K = map(int, input().strip().split())
graph = [[0]*N for _ in range(N)]
queue = []
for i in range(M):
    r, c, m, s, d = map(int, input().strip().split()) # x, y, 질량, 속력, 방
    queue.append((r-1, c-1, m, s, d))

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

for _ in range(K):
    new_q = []
    location = defaultdict(list)
    for cr, cc, cm, cs, cd in queue:
        cr = (cr + (dx[cd]*cs))%N
        cc = (cc + (dy[cd]*cs))%N

        location[(cr,cc)].append((cm, cs, cd))

    for key in location.keys():
        cr, cc = key
        cnt = len(location[key])
        if cnt > 1:
            zip_m, zip_s, zip_d = map(list, zip(*location[key]))
            cm = sum(zip_m)//5
            cs = sum(zip_s)//cnt

            # 소멸 확인
            if cm == 0:
                continue

            # 방향 확인
            check = []
            for z_d in zip_d:
                check.append(z_d%2)
            if all(ch == check[0] for ch in check):  # 모두 짝수거나 모두 홀수
                for i in range(0, 8, 2):  # 0,2,4,6
                    new_q.append((cr, cc, cm, cs, i))
            else:
                for i in range(1, 8, 2):  # 1,3,5,7
                    new_q.append((cr, cc, cm, cs, i))
        else:
            cm, cs, cd = location[key][0]
            new_q.append((cr, cc, cm, cs, cd))

    queue = new_q

answer = 0
for q in queue:
    answer += q[2]
print(answer)