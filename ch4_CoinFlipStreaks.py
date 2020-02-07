

import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.

    arr = []
    for i in range(100):
        if random.randint(0, 1) == 0:
            arr.append('T')
        else: arr.append('H')

    # Code that checks if there is a streak of 6 heads or tails in a row.
    count = 0
    last = ''
    for i in range(100):
        if last != arr[i]:
            count = 0
            last = arr[i]
        else: count = count + 1
        if count == 6:
            numberOfStreaks = numberOfStreaks + 1

print('Chance of streak : %s%%' % (numberOfStreaks / 100 ))