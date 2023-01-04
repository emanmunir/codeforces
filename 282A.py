n = int(input())
x=0
for i in range(n):
    bit = input()
    if str(bit) == "++X" or str(bit) == "X++":
        x = x + 1
    if str(bit) == "--X" or str(bit) == "X--":
        x = x - 1
print(x)