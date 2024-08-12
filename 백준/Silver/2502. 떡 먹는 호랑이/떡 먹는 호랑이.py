import sys
input = sys.stdin.readline

cnt, ricecake = map(int, input().split())

dp_x, dp_y = [-1]*30, [-1]*30
dp_x[3], dp_x[4] = 1, 1
dp_y[3], dp_y[4] = 1, 2

def ricecake_tiger(cnt, ricecake):
    for i in range(5, cnt+1):
        dp_x[i] = dp_x[i-1] + dp_x[i-2]
        dp_y[i] = dp_y[i-1] + dp_y[i-2]

    x, y = dp_x[cnt], dp_y[cnt]
    for i in range(ricecake//y, 0, -1):
        if (ricecake-(y*i))%x == 0 and (ricecake-(y*i))//x != 0:
            print((ricecake-(y*i))//x)
            print(i)
            return

ricecake_tiger(cnt, ricecake)