level =  set(range(1, int(input()) + 1))
x = list(map(int, input().split()))
y = list(map(int, input().split()))

x = set(x[1:])
y = set(y[1:])


if level - (x | y) == set():
    print('I become the guy.')
else:
    print('Oh, my keyboard!')
