n,k = (map(int,input().split()))
count=0
cont = list(map(int,input().split()))
max = cont[k-1]
for i in range(n):
    if cont[i] >= max and cont[i] != 0:
        count += 1
print(count)

