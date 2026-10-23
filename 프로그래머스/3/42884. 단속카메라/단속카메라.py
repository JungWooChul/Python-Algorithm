import heapq
def solution(routes):
    routes.sort(key = lambda x : x[1])
    
    answer = 1
    check = routes[0][1]
    for route in routes:
        if check < route[0]:
            check = route[1]
            answer += 1
        else:
            continue
        
    return answer