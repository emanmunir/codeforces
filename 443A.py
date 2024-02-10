n = input()
s= n.replace(" ","")
s= s.replace("{","")
s= s.replace("}","")
s= s.replace(",","")
print(len(set(s)))
#print(len(t))

