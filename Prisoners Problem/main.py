from functions import CreateRoom, OpenBox, PlayGame ,CreatePlot
import numpy as np # installed with matplotlib
import time

if __name__ == '__main__':

    wins = 0
    reps = 3000
    #tic = time.perf_counter()

    x = np.array([0])
    y = np.array([0])

    for i in range(1,reps+1): #Η λούπα που κατασκεβάζει τα δωμάτια

        room = CreateRoom(i+30000)
        if PlayGame(room) == 1:
            wins += 1

        winrate = wins / i
        x = np.append(x, i)
        y = np.append(y, winrate)

    CreatePlot(x,y)


    #toc = time.perf_counter()
    #print(toc - tic)

    winrate = wins / reps
    print(winrate)
