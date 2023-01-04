len = int(input())
total = 0
for i in range(len):
    Sum = sum(map(int,input().split()))
    if Sum>=2:
        Sum = 1
        total =total + Sum
print(total)