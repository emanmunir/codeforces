t = int(input())
count = 0
for i in range(t):
    people,room = map(int,input().split())
    if people < room:
        if room - people != 1:
            count+=1
print(count)
