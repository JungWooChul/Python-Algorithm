def solution(N, number):
    answer = -1
    dp = [[] for _ in range(9)]
    for i in range(1, 9):
        number_set = set()
        number_set.add(int(str(N)*i))
        for j in range(1, i):
            for comb1 in dp[i - j]:
                for comb2 in dp[j]:
                    plus = comb1 + comb2
                    minus = comb1 - comb2
                    mul = comb1 * comb2
                    if comb2 != 0:
                        div = comb1 / comb2
                        if div % 1 == 0:
                            number_set.add(int(div))
                    number_set.add(plus)
                    number_set.add(mul)
                    if minus >= 0:
                        number_set.add(minus)
        if number in number_set:
            return i
        for q in number_set:
            dp[i].append(q)
    return answer