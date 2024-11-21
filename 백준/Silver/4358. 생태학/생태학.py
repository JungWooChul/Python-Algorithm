import sys
from collections import defaultdict
input = sys.stdin.readline

def main():
    N = 0
    graph = defaultdict(int)

    while True:
        kind = input().strip()
        if kind == '':
            break
        N += 1
        graph[kind] += 1
    
    
    for k,v in sorted(graph.items()):
        print(k, format(v/N * 100, '.4f'))

if __name__ == '__main__':
    main()
