a = [[1], [2,3], [4,5,6,7], [9,89,1,1,1,1,1,3]]
height = 3
n = 0
width = 5

for i in range(0,len(a)):
    sep_len = width*2**(height - i) + 2**(height - i) - 1
    start_space = (2**height + width * (2**height - 1) - sep_len * (2**i - 1) - 2**i)//2
    print(" " * start_space, end='')
    for j in range(0,len(a[i])):
        print(str(a[i][j]), end = ' '* (sep_len - len(str(a[i][j]))//2))
    print()
