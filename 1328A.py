t= int(input())
c =0
for i in range(t):
    a,b = map(int,input().split())
    print((b-a%b)%b)
