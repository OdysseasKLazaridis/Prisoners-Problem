import numpy as np # installed with matplotlib
import random as random
import matplotlib.pyplot as plt
import time

def new_game(seed):
    def open_box(i, key, steps):
        total_steps +=1
        my_list.append(i)
        if dict[i] == key:
            return steps
        else:
            steps = steps + 1
            return open_box(dict[i], key, steps)
        
    list2 = list(range(1, 101))
    random.Random(seed).shuffle(list2)

    dict = {}

    for  i in range(1,101):
        dict[i] = list2[i-1]
    
    total_steps = 0

    for i in range(1,101):
        steps = 1
        
        if total_steps >= 50:
            return 1

        if open_box(i, i, steps) >= 50:

                return 0
    return 1

my_list = []
wins = 0
reps = 10000
tic = time.perf_counter()

for i in range(1,reps): 
    if new_game(i) == 1:
        wins = wins +1
toc = time.perf_counter()
print(toc - tic)

winrate = wins / reps
print(winrate)