n = int(input())
for i in range(n):
    t = input()
    ti = len(t)
    li = [ch for ch in t]
    if ti%2 != 0:
        print("NO")
    if ti%2 == 0:
        if li[int(len(t)/2):] == li[:int(len(t)/2)]:
            print("YES")
        else:
            print("NO")
