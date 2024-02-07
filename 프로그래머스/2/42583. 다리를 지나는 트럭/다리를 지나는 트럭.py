from collections import deque

# 다리의 자리수를 만들어 접근
def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = deque(truck_weights)
    on_bridge, on_bridge_weight = deque([0] * bridge_length), 0
    
    # 1초 동안 할 수 있는 행위 : 다리에 올라오기, 기다리기, 다리 건너기
    while(truck_weights):
        # 현 상태에서 트럭이 추가되지 못하는 경우
        if on_bridge_weight + truck_weights[0] > weight:
            on_bridge_weight -= on_bridge.popleft()
            # 트럭 한 대가 다리를 지남과 동시에 대기 트럭에서 트럭이 올라올 수 있는지 확인
            if on_bridge_weight + truck_weights[0] > weight:
                on_bridge.append(0)
            else:
                tmp = truck_weights.popleft()
                on_bridge.append(tmp)
                on_bridge_weight += tmp
        # 현 상태에서 트럭이 추가 가능한 경우
        else:
            on_bridge_weight -= on_bridge.popleft()
            tmp = truck_weights.popleft()
            on_bridge.append(tmp)
            on_bridge_weight += tmp
        
        answer += 1
    return answer + bridge_length