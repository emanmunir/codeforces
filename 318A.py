n, k = list(map(int, input().split()))
print((k - (n + 1) // 2) * 2 if k > (n + 1) // 2 else k * 2 - 1)


