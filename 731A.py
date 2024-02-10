abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
l = list(map(str,input()))
dis = 0
total = 0
for x in l:
    pos = abc.index(x)
    forward =  abs(dis-pos)
    backward = abs(len(abc)-forward)
    total += min(forward,backward)
    dis = pos
print(total)

