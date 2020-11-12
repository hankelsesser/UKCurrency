values = [1, 2, 5, 10, 20, 50, 100, 200]
coin_bag = []
for i in range(len(values)):
    for n in range(200/values[i]):
        coin_bag.append(i)
print(coin_bag)
