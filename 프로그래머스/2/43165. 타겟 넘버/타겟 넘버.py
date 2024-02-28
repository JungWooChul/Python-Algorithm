answer = 0
def solution(numbers, target):
    global answer
    def dfs(n, total):
        global answer
        if n == len(numbers):
            if total == target:
                answer += 1
            return answer
        dfs(n+1, total+numbers[n])
        dfs(n+1, total-numbers[n])
    
    
    dfs(0, 0)
    return answer