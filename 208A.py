st = str(input())
if "WUB" in st:
    s =st.split("WUB")
st = ''
for i in range(len(s)):
    st+= f"{s[i]} "
print(st)
