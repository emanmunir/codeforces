num = int(input())
for i in range(num):
    for j in range(8):    
        st = str(input())
        for k in range(8):
            if st[k] != ".":
                print(st[k],end="")
    print("")
        
