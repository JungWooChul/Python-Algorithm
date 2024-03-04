import sys
input = sys.stdin.readline

num = int(input())

strides = [int(input()) for _ in range(num)]

scale = [ 'A', '0', 'B', 'C', '0', 'D', '0', 'E', 'F', '0', 'G', '0']
len_scale = len(scale)

for i in range(len(scale)):
    if scale[i] == '0':
        continue
    else:
        pnt, check = i, True
        for stride in strides:
            if scale[(pnt+stride)%len_scale]=='0':
                check = False
                break
            else:
                pnt = (pnt+stride)%len_scale
        if check and scale[pnt%len_scale]!='0':
           print('{} {}'.format(scale[i], scale[pnt]))
