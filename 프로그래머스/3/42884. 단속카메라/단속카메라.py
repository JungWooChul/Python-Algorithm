def solution(routes):
    routes.sort(key=lambda x:x[1])
    answer = 1
    check = routes[0][1]
    for route in routes[1:]:
        if check < route[0]:
            check = route[1]
            answer += 1
    return answer
