n= int(input())
blocks = list(map(int,input().split()))
blocks.sort()
for i in range(len(blocks)):
    print(blocks[i],end=" ")

