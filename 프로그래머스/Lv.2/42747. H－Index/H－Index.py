def solution(citations):
    citations.sort()
    n = len(citations)
    answer = 0
    
    for i in range(1, len(citations)+1):
        min_lst = [j for j in citations if j<=i]
        max_lst = [k for k in citations if k>=i]
        if (len(min_lst) <= i) and (len(max_lst) >= i):
            answer = i
            
    return answer