import sys
from collections import defaultdict

input = sys.stdin.readline

def main():
    N = int(input())
    nodes = list(map(int, input().strip().split()))
    del_node = int(input())

    # 트리 구성 {부모노드 : [자식노드1, 자식노드2]}
    graph = defaultdict(list)
    for i in range(N):
        if nodes[i] == -1:
            graph[i]
        else:
            graph[nodes[i]].append(i)
            graph[i]

    # 반례(N = 2, nodes = [-1, 0], del_node = 1)
    # del_node가 제거되기 전, 모든 부모 노드에서 del_node를 제거
    for parent, children in graph.items():
        if del_node in children:
            children.remove(del_node)

    # del_node가 제거될 때 같이 제거되는 자식노드 찾는 함수
    def find_child(node, queue):
        while graph[node]:
            # graph[node]의 첫 번째 자식 노드를 pop하면서 동시에 queue에 추가
            child = graph[node].pop(0)
            queue.append(child)
            queue = find_child(child, queue)
        
        return queue

    queue = find_child(del_node, [del_node])
    
    # 노드 제거
    for q in queue:
        graph.pop(q)

    # 리프 노드 수 계산
    answer = 0
    for val in graph.values():
        if val == []:
            answer += 1
    
    print(answer)
    return 

if __name__ == '__main__':
    main()