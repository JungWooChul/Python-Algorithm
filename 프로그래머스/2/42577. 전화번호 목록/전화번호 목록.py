def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        prefix, word = phone_book[i], phone_book[i+1]
        if word[:len(prefix)] == prefix and word != prefix:
            return False
    return answer