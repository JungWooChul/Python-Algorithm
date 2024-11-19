from collections import deque


def solution(begin, target, words):
    if target not in words:
        return 0

    queue = deque()
    queue.append([begin,0])
    while queue:
        now, depth = queue.popleft()
        if now == target:
            return depth

        for word in words:
            cnt = 0
            for i in range(len(now)):
                if now[i] != word[i]:
                    cnt += 1

            if cnt == 1:
                queue.append([word, depth + 1])