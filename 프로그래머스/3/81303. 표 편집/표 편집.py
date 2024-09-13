def solution(n, k, cmd):
    # 각 노드의 이전, 다음을 저장하는 리스트
    prev = [i - 1 for i in range(n)]
    next = [i + 1 for i in range(n)]
    next[-1] = -1  # 마지막 행의 다음은 없으므로 -1로 설정

    # 삭제된 행을 저장할 스택
    removed = []
    
    # 현재 선택된 행의 위치
    curr = k

    for command in cmd:
        # 명령어 처리
        if command[0] == 'U':  # 위로 이동
            x = int(command.split()[1])
            for _ in range(x):
                curr = prev[curr]
        
        elif command[0] == 'D':  # 아래로 이동
            x = int(command.split()[1])
            for _ in range(x):
                curr = next[curr]
        
        elif command[0] == 'C':  # 현재 행 삭제
            removed.append(curr)  # 삭제된 행 저장
            # 이전 행과 다음 행을 서로 연결
            if prev[curr] != -1:
                next[prev[curr]] = next[curr]
            if next[curr] != -1:
                prev[next[curr]] = prev[curr]
            
            # 삭제 후 선택된 행 갱신
            if next[curr] != -1:
                curr = next[curr]
            else:
                curr = prev[curr]
        
        elif command[0] == 'Z':  # 마지막 삭제된 행 복구
            restore = removed.pop()  # 복구할 행
            # 복구할 행의 이전, 다음 노드 다시 연결
            if prev[restore] != -1:
                next[prev[restore]] = restore
            if next[restore] != -1:
                prev[next[restore]] = restore

    # 결과 출력
    result = ['O'] * n
    for r in removed:
        result[r] = 'X'
    
    return ''.join(result)