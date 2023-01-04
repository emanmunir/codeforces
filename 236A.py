user = str(input()).lower()
u = set()
for i in range(len(user)):
    u.add(user[i])
if len(u)%2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")