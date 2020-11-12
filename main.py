import itertools
values = [1, 2, 5, 10, 20, 50, 100, 200]

def make_bag(values):
    coin_bag = []
    for i in range(len(values)):
        for n in range(200/values[i]):
            coin_bag.append(values[i])
    return(coin_bag)

coins = make_bag(values)
combinations = []
for length in range(len(coins)):
    combinations.append(list(itertools.combinations(coins, length)))
print(combinations)
