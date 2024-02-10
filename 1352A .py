t = int(input())
for _ in range(t):
    n = int(input())
    summands = []
    divisor = 1
    while n > 0:
        num = n % 10
        if num > 0:
            summands.append(num * divisor)
        n //= 10
        divisor *= 10
    print(len(summands))
    print(*reversed(summands))