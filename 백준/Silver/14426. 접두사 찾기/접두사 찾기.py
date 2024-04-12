import sys
input = sys.stdin.readline

class Node(object):
    def __init__(self, key, data=None):
        self.key = key 
        self.children = {} 

class Trie:
    def __init__(self) -> None:
        self.head = Node(None)
    
    def insert(self, S):
        current_node = self.head
        for s in S:
            if s not in current_node.children:
                current_node.children[s] = Node(s)
            current_node = current_node.children[s]
    
    def checkPrefix(self, prefix):
        current_node = self.head
        for s in prefix:
            if s in current_node.children:
                current_node = current_node.children[s]
            else:
                return 0
        return 1

def search_prefix():
    N, M = map(int, input().split())

    trie = Trie()
    # 문자열 입력
    for _ in range(N):
        trie.insert(input().rstrip())

    # 접두사 입력 및 확인
    answer = 0
    for _ in range(M):
        answer += trie.checkPrefix(input().rstrip())
    return answer

print(search_prefix())

