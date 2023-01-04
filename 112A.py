str1 = input()
st1 = str(str1).lower()
str2 = input()
st2 = str(str2).lower()
string1 =0
string2 =0
for i in range(len(st1)):
    string1 += ord(st1[i])
    string2 += ord(st2[i])
for j in range(1):
    if string1== string2:
        print("0")
        break
    if string1 > string2 :
        print("1")
        break
    if string2 < string1:
        print("-1")
        break
        

