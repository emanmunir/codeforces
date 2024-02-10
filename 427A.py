n = int(input())
t = list(map(int,input().split()))
police,crime = 0,0
for i in range(n):
    if t[i] != -1:
        police += t[i]
    if t[i] == -1:
        if police != 0:
            police += t[i]
        else:
            crime+=1
print(crime)

