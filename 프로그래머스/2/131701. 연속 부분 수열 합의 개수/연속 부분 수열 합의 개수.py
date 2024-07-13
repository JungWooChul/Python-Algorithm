def solution(elements):
    total_sums = []
    check, len_elem = 0, len(elements)
    
    temp_list = [0] * len_elem
    while check < len_elem:
        for i in range(len(temp_list)):
            temp_list[i] += elements[(i+check)%len_elem]
        
        total_sums.extend(temp_list)
        check += 1
    return len(set(total_sums))