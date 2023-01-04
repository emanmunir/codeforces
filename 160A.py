n = input()
coins = list(map(int,input().split()))
coins.sort(reverse=True)
coin, quantity = 0,0
h = sum(coins)/2
for i,v in enumerate(coins):
    quantity+= v
    coin += 1
    if quantity>h:
        break
print(coin)

