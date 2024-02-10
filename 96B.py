n = int(input())
for i in range((n)):
    if str(n).count("4") == str(n).count("7"):
       break
    else:
        n+=1
print(n)
