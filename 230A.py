strength,t = map(int,input().split())
c = 0
l = []
for i in range(t):
    l.append(list(map(int,input().split())))
l.sort()
k = "YES"
for power in l:
    if strength > power[0]:
        strength+=power[1]
    else:
        k ="NO"
        break
print(k)

