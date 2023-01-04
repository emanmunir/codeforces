int = input()
list=[]
for i in range(0,len(int),2):
    list.append(int[i])
for j in range(0,len(list)):
    for k in range(0,len(list)-1):
        if list[k]>list[k+1]:
            list[k],list[k+1]=list[k+1],list[k]
for m in range(len(list)):
    print(list[m],end="")
    if len(list)> len(list)-1:
        print("+",end="")
