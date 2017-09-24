from sys import stdin
from copy import copy
from collections import defaultdict
from timeit import default_timer

Inf = 1000000000
best_value = defaultdict(int)


def min_coins_greedy(coins, value):

    count = 0
    for coin in coins:                          #check for all coins
        while value >= coin:                    #check if coin can be used
            value -= coin                       #subtract coin from value
            count += 1                          #cound coin used
    return count



def min_coins_dynamic(coins, value):
    temp_list = []
    list = []
    originalvalue = value
    j = 1
    print(coins)

    while value > 0:


            for index in range(len(coins)):
                value = originalvalue
                while value >= coins[index]:
                    temp_list.append(coins[index])
                    value -= coins[index]

                if index == len(coins):
                    break

                else:
                    while j < len(coins) - 1:
                        for index1 in range (j, len(coins)):
                            while value >= coins[index1]:
                                temp_list.append(coins[index1])
                                value -= coins[index1]

                        if len(list) == 0:
                            list = temp_list.copy()

                        else:
                            if len(temp_list) < len(list) and len(temp_list) != 0:
                                list = temp_list.copy()

                        j += 1
                        temp_list.clear()
                        value = originalvalue
                        while value >= coins[index]:
                            temp_list.append(coins[index])
                            value -= coins[index]
    return len(list)


"""
def min_coins_dynamic(coins, value):

    if len(coins) < 1 or value < 0:
        return 0

    coins_copy = coins.copy()
    try:
        return len(best_value.get(value))       #Check if the value is in dic

    except:


        while True:

            temp_picks, first_index = min_coins_greedy_dyn(coins_copy, value)       #Calculate combination
            coins_copy = coins_copy[first_index + 1:]                               #Edit coinlist to check first possible solution after last comb

            if best_value.get(value) is None:                                       #If comb has not yet been added to the dic
                best_value[value] = temp_picks.copy()

            elif len(best_value.get(value)) > len(temp_picks):                      #If current comb is better than last found comb
                best_value[value] = temp_picks.copy()

            if len(coins_copy) <= 1:                                                #If coin list just contains '1'
                print("Comb found", best_value)
                return len(best_value.get(value)) if len(best_value.get(value)) < value else value #return value if there is no better comb


def min_coins_greedy_dyn2(coins, value):

    temp_picks = []
    i = 0
    for index in range(len(coins)):             #check for all coins
        while value >= coins[index]:
            #Check if coin can be used
            if len(temp_picks) == 0:            #Save first index of comb
                i = index
            temp_picks.append(coins[index])     #Save comb
            value -= coins[index]               #Subtract coin from value
    return temp_picks, i

"""
def can_use_greedy(coins):
    return False

coins = []
for c in stdin.readline().split():
    coins.append(int(c))
coins.sort()
coins.reverse()
method = stdin.readline().strip()
if method == "graadig" or (method == "velg" and can_use_greedy(coins)):
    for line in stdin:
        print(min_coins_greedy(coins, int(line)))
else:
    for line in stdin:
        print(min_coins_dynamic(coins, int(line)))

"""
t0 = default_timer()

values = [64]
coin_l = [50,10,7,1]
for x in values:
    print("Value: ", x)
    print("Min coins used: ", min_coins_dynamic(coin_l, x),'\n')

t1 = default_timer()
print("Timer", round(t1-t0, 3))


coins = [50,10,5,4,1]

x = min_coins_dynamic(coins, 8)
print(x)
"""