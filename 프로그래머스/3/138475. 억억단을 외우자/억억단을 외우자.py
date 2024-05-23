def solution(e, starts):
    # Step 1: Calculate the count of appearances for each number from 1 to e
    appearances = [0] * (e + 1)
    
    for i in range(1, e + 1):
        for j in range(i, e + 1, i):
            appearances[j] += 1
    
    # Step 2: Precompute the most frequent number for each start value
    most_frequent = [0] * (e + 1)
    max_freq = [0] * (e + 1)
    max_num = 0
    
    for i in range(e, 0, -1):
        if appearances[i] >= max_num:
            max_num = appearances[i]
            most_frequent[i] = i
        else:
            most_frequent[i] = most_frequent[i + 1]
        max_freq[i] = max_num

    # Step 3: Answer the queries based on precomputed values
    results = []
    for s in starts:
        results.append(most_frequent[s])

    return results

