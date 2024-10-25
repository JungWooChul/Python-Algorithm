import sys
input = sys.stdin.readline

def main():
    # 방의 크기와 로봇 청소기의 초기 위치 및 방향 입력
    N, M = map(int, input().strip().split())
    r, c, d = map(int, input().strip().split())
    matrix = [list(map(int, input().strip().split())) for _ in range(N)]
    cleaned = [[0] * M for _ in range(N)]  # 청소 상태를 저장할 배열

    # 방향 정의 (0: 북, 1: 동, 2: 남, 3: 서)
    direction = {
        0: [-1, 0],  # 북
        1: [0, 1],   # 동
        2: [1, 0],   # 남
        3: [0, -1]   # 서
    }

    def in_bounds(x, y):
        return 0 <= x < N and 0 <= y < M

    cleaned_count = 0

    while True:
        # 1. 현재 칸 청소
        if cleaned[r][c] == 0:
            cleaned[r][c] = 1
            cleaned_count += 1

        # 2. 주변 4칸 검사
        found = False
        for _ in range(4):
            d = (d + 3) % 4  # 왼쪽으로 회전
            nx, ny = r + direction[d][0], c + direction[d][1]
            # 청소되지 않은 빈 칸이 있는 경우 한 칸 전진 후 다시 청소
            if in_bounds(nx, ny) and matrix[nx][ny] == 0 and cleaned[nx][ny] == 0:
                r, c = nx, ny
                found = True
                break

        # 청소되지 않은 빈 칸을 찾지 못했을 때
        if not found:
            # 후진할 좌표 계산
            back_direction = (d + 2) % 4
            br, bc = r + direction[back_direction][0], c + direction[back_direction][1]
            # 후진할 위치가 벽이면 작동을 멈추기
            if not in_bounds(br, bc) or matrix[br][bc] == 1:
                break
            # 후진 가능하면 후진
            r, c = br, bc

    # 청소한 칸의 개수 출력
    print(cleaned_count)

main()