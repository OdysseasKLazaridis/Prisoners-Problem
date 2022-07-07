import numpy as np # installed with matplotlib
import random as random
import matplotlib.pyplot as plt
import time

def new_game(seed): #This function starts a new game with 100 prisoners and 100 boxes with a seed input

    def open_box(i, key, steps): #This is a recursive function which will keep opening boxes until it makes a loop 

        if dict[i] == key:
            return steps
        else:
            steps += 1
            return open_box(dict[i], key, steps)
        
    array2 = list(range(1, 101))
    
    random.Random(seed).shuffle(array2)
    dict = {}

    for  i in range(1,101):
        dict[i] = array2[i-1]
        
    
    total_steps = 0

    for i in range(1,101):
        steps = 1
        total_steps += 1
        if total_steps >= 50:
            return 1

        if open_box(i, i, steps) > 50:
            return 0
    return 1

wins = 0
reps = 100000
tic = time.perf_counter()


x = np.array([0])
y = np.array([0])

for i in range(1,reps+1): 
    if new_game(i+30000) == 1:
        wins += 1

    winrate = wins / i
    x = np.append(x, i)
    y = np.append(y, winrate)

plt.xlabel('# of games played')
plt.ylabel('winrate')
plt.plot(x, y)
plt.savefig('testplot.png')

toc = time.perf_counter()
print(toc - tic)

winrate = wins / reps
print(winrate)