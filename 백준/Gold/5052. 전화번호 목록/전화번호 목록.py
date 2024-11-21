def is_consistent(phone_numbers):
    phone_numbers.sort()  # 사전순 정렬
    for i in range(len(phone_numbers) - 1):
        # 현재 번호가 다음 번호의 접두어인지 확인
        if phone_numbers[i + 1].startswith(phone_numbers[i]):
            return "NO"
    return "YES"

# 테스트 케이스 입력 및 처리
T = int(input())  # 테스트 케이스 수
results = []

for _ in range(T):
    n = int(input())  # 전화번호 개수
    phone_numbers = [input().strip() for _ in range(n)]
    results.append(is_consistent(phone_numbers))

# 결과 출력
for result in results:
    print(f"{result}")