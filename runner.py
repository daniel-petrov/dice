# This program shows the probability distribution of the sum of x number of dice.

import random
import collections
import matplotlib.pyplot as plt

if __name__ == '__main__':
    sums = []
    how_many_dice = int(raw_input("How many dice?: "))
    how_many_times = int(raw_input("How many times?: "))


    for j in range(1,how_many_times+1):
        values = []
        for i in range(1,how_many_dice+1):
            values.append(random.randint(1, 6))
        sums.append(sum(values))

    dictionary = collections.Counter(sums)
    # print(sums)


    plt.bar(list(dictionary.keys()), dictionary.values(), color='g')
    plt.show()