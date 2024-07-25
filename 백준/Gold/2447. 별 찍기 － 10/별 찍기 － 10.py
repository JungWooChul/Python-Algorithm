import sys
input = sys.stdin.readline

def draw_star(n):
    if n == 1:
        return ['*']
    
    stars = draw_star(n // 3)
    result = []
    
    for s in stars:
        result.append(s * 3)
    for s in stars:
        result.append(s + ' ' * (n // 3) + s)
    for s in stars:
        result.append(s * 3)
    
    return result

def main():
    n = int(input())
    print('\n'.join(draw_star(n)))

main()