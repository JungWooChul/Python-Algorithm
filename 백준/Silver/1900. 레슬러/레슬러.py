import sys
input = sys.stdin.readline

def fight(N, player_info):
    player_rank = {p:0 for p in player_info.keys()}
    for i in range(1, N):
        for j in range(i+1, N+1):
            p1 = player_info[i][0] + player_info[i][1]*player_info[j][0]
            p2 = player_info[j][0] + player_info[j][1]*player_info[i][0]
            if p1 > p2:
                player_rank[i] += 1
            elif p1 < p2:
                player_rank[j] += 1

    for k, v in sorted(player_rank.items(), reverse=True, key=lambda x:x[1]):
        print(k)

    return

N = int(input())
player_info = {i:tuple(map(int, input().split())) for i in range(1, N+1)}

fight(N, player_info)