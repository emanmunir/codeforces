abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
t = int(input())
for _ in range(t):
    ln = int(input())
    ch = list(map(str,input()))
    st = [abc.index(i)+1 for i in ch]
    print(max(st))

        

