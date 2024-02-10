t = int(input())
l = []
count = 1
for i in range(t):
    m = int(input())
    l.append(m)
for i in range(len(l)-1):
    if l[i] != l[i+1]:
        count+=1
print(count)


