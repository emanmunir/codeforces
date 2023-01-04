lenn, t = (map(int,input().split()))
st= (input())
s = [ch for ch in st]
for i in range((t)):
    if s[i] == "B" and s[i+1] == "G":
        s[i] = "G"
        s[i+1] = "B"
for i in range(len(s)):
    print(s[i],end="")


