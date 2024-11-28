import sys
input = sys.stdin.readline

def main():
    query = []
    chocolate = []
    coffee = []

    while True:
        cmd = input().strip().split()
        # 입력 종료
        if not cmd:
            break

        if cmd[0] == 'Query':
            query.append(int(cmd[1]))
        elif cmd[0] == 'Chocolate':
            chocolate.append((int(cmd[1]), float(cmd[2])))
        elif cmd[0] == 'Coffee':
            coffee.append((int(cmd[1]), float(cmd[2])))
    
    query.sort()
    for q in query:
        safe_distance = 0

        # 초콜릿
        for t, n in chocolate:
            if t > q:
                continue
            effect = 8 * n - (q - t) / 12
            # 음식을 다 소화했는지 여부
            if effect > 0:
                safe_distance += effect

        # 커피
        for t, n in coffee:
            if t > q:
                continue
            effect = 2 * n - ((q - t) ** 2) / 79
            # 음식을 다 소화했는지 여부
            if effect > 0:
                safe_distance += effect
        
    
        safe_distance = round(max(safe_distance, 1.0), 1)
        print(f'{q} {safe_distance}')
    
    return


if __name__ == '__main__':
    main()