n= int(input())
steps = map(int,input().split())
a,count,total=0,0,0
for step in steps:
  if a>step:
    count=0
  count+=1
  a=step
  total=max(total,count)
print(total)
