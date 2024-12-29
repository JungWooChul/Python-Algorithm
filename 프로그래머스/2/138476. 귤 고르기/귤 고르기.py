from collections import Counter
def solution(k, tangerine):
    tangerine_dict = Counter(tangerine)
    tangerine_dict = sorted(tangerine_dict.items(), key=lambda x:x[1], reverse=True)
    tmp, answer = 0, 0
    for key,val in tangerine_dict:
        tmp += val
        answer += 1
        if tmp >= k:
            return answer