import random
import matplotlib.pyplot as plt

def CreateRoom(seed):
    array2 = list(range(1, 101))
    
    random.Random(seed).shuffle(array2)
    room = {}

    for  i in range(1,101):
        room[i] = array2[i-1]
        
    return room

def OpenBox(i, key, steps, room): #This is a recursive function which will keep opening boxes until it makes a loop 
    if room[i] == key:
        return steps
    else:
        steps += 1
        return OpenBox(room[i], key, steps, room)

def PlayGame(room):
    totalSteps = 1
    for i in range(1,101):
        steps = 1
        totalSteps += 1
        if totalSteps >= 50:
            return 1

        if OpenBox(i, i, steps, room) > 50:
            return 0

def CreatePlot(x,y):
    plt.xlabel('# of games played')
    plt.ylabel('winrate')
    plt.plot(x, y)
    plt.savefig('testplot.png')