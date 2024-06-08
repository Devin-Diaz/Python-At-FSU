def a_stair_case(n: int):
    for i in range(n):
        for j in range(i):
            print('*', end='')
        print('')

def b_stair_case(n: int):
    for i in range(n):
        for j in range(n - i):
            print('*', end='')
        print('')

def c_stair_case(n: int):
    prefix = ''
    for i in range(n):
        prefix += ' '
        print(prefix, end = '')
        for j in range(n - i):
            print('*', end='')
        print('')

def d_stair_case(n: int):
    for i in range(1, n+1):
        print(' ' * (n - i) + '*' * i)

