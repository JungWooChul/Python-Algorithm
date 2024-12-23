def solution(n, words):
    answer = [0,0]
    check = words[0][-1]
    dup = {words[0]:1}
    for i in range(1, len(words)):
        if check == words[i][0]:
            if dup.get(words[i]):
                return [i%n + 1, i//n + 1]
            check = words[i][-1]
            dup[words[i]] = 1
        else:
            return [i%n + 1, i//n + 1]
        
    return [0,0]