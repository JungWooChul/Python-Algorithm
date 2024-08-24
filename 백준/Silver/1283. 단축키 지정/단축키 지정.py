import sys
input = sys.stdin.readline

N = int(input())
words = [input().strip() for _ in range(N)]

def shortcut(words):
    sc_keys = []
    
    for word in words:
        check, word_split = 0, word.split()
        if len(word_split) > 1:
            for i in range(len(word_split)):
                if word_split[i][0].lower() not in sc_keys:
                    sc_keys.append(word_split[i][0].lower())
                    word_split[i] = f'[{word_split[i][0]}]' + word_split[i][1:]
                    print(' '.join(word_split))
                    check += 1
                    break

        if check:
            continue

        check = 0
        for alp in word:
            if alp.lower() in sc_keys:
                print(alp, end = '')
            else:
                if check or alp == ' ':
                    print(alp, end = '')
                else:
                    sc_keys.append(alp.lower())
                    print(f'[{alp}]', end = '')
                    check = 1
        print()
    return

shortcut(words)