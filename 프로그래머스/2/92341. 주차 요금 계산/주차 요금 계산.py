from collections import defaultdict
def solution(fees, records):
    accumulated_time = defaultdict(int)
    cars, max_time = dict(), 1439
    
    # 누적 주차 시간 계산
    for record in records:
        time, cn, io = record.split() # 시간, 차 번호, 입/출차
        
        # 시간 계산(분)
        time = list(map(int, time.split(':')))
        time = time[0]*60 + time[1]
        
        # 입/출차 구분
        if io == 'IN':
            cars[cn] = time
        else:
            duration = time - cars.pop(cn)
            accumulated_time[cn] += duration
    
    # 12시까지 출차하지 않은 차량
    for cn, time in cars.items():
        duration = max_time - cars[cn]
        accumulated_time[cn] += duration
    
    # 차량 번호 순서대로 정렬
    answer = []
    for cn, duration in sorted(accumulated_time.items()):
        # 기본요금
        if duration <= fees[0]:
            answer.append(fees[1])
                
        # 기본요금 초과
        else:
            # 정산금 올림 여부
            check = 0
            if (duration-fees[0])%fees[2]:
                check += 1

            answer.append(fees[1] + ((duration-fees[0])//fees[2]+check)*fees[-1])
    return answer