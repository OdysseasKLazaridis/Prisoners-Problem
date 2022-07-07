from room import CreateRoom, OpenBox, PlayGame
import numpy as np # installed with matplotlib
import matplotlib.pyplot as plt
import time

if __name__ == '__main__':

    wins = 0
    reps = 3000
    tic = time.perf_counter()

    x = np.array([0])
    y = np.array([0])

    for i in range(1,reps+1): 
        room = CreateRoom(i+30000)
        if PlayGame(room) == 1:
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
