def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        arr = array[i-1:j]
        arr = sorted(arr)
        answer.append(arr[k-1])
    return answer