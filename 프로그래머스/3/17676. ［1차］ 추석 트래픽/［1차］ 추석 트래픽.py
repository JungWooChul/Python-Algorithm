def div_log(log):
    log = log.split()
    hh, mm, ss = map(float, log[1].split(':'))
    t = int(float(log[-1][:-1]) * 1000)
    
    # 1초가 1000밀리초 이므로 1000을 곱하여 표현
    endTime = (hh * 3600 + mm * 60 + ss)*1000
    startTime = endTime - t + 1
    
    return [int(startTime), int(endTime)]
    
def solution(lines):
    log = []
    for line in lines:
        log.extend(div_log(line))
    
    answer = 0
    for t in log:
        check = 0
        t_1 = t + 1000 - 1
        for i in range(0, len(log), 2):
            if (t <= log[i] <= t_1) or (t <= log[i+1] <= t_1) or (log[i] <= t <= log[i+1]) or (log[i] <= t_1 <= log[i+1]):
                check += 1
                        
        answer = max(answer,check)
        
    return answer