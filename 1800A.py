import re
for _ in range(int(input())):
    t = int(input())
    if re.match('^m+e+o+w+$', input().lower()):
        print("YES")
    else:
        print("NO") 
    

