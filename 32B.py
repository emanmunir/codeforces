a = str(input())
ans = ''
haha = 0
while haha <= len(a) - 1:
    if a[haha] == '.':
        ans += '0'
        haha += 1
    else:
        if a[haha + 1] == '.': #just checking
            ans += '1'
            haha += 2
        else:
            ans += '2'
            haha += 2
print(ans)
