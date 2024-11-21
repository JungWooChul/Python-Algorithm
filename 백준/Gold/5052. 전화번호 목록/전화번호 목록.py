import sys
input = sys.stdin.readline

def is_prefix(phone_numbers):
    phone_numbers.sort() # 사전순 정렬
    for i in range(len(phone_numbers) - 1):
        # 현재 번호가 다음 번호의 접두어인지 확인
        if phone_numbers[i + 1].startswith(phone_numbers[i]):
            return "NO"
    return "YES"

def main():
    T = int(input())
    results = []

    for _ in range(T):
        n = int(input())
        phone_numbers = [input().strip() for _ in range(n)]
        results.append(is_prefix(phone_numbers))

    for result in results:
        print(f"{result}")

if __name__ == '__main__':
    main()