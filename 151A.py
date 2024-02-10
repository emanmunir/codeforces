n, k, l, c, d, p, nl, np = map(int,input().split())
ml = k*l
toast_rn = ml/n
lime = d*c
salt = p/np
print(toast_rn,lime,salt)
print(min(int(toast_rn),int(lime),int(salt))//3)
