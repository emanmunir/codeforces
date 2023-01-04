leng = int(input())
for i in range(leng):
    w = input() #enter a word
    word = str(w).lower()
    if len(word) > 10:
        print(word[0],end="")
        print((len(word)-2),end="")
        print(word[-1])
    else:
        print(word)