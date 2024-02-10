t = int(input())
p=input().split()
for i in range(1,t+1):
	print((p.index(str(i))+1),end=" ")
