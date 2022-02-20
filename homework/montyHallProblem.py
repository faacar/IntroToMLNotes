import random
from select import select

def runTrial(switchDoor):
    #prepare the boxes for the game
    #false = goat
    #true = car
    boxes = [False, False, True]

    random.shuffle(boxes)

    selectedBoxIndex = random.randint(0,2)

    if switchDoor:
        boxes.remove(False)
        selectedBoxIndex = random.randint(0,1)
        return boxes[selectedBoxIndex]
    else:
        return boxes[selectedBoxIndex]

def getResultPossibility(data, resultType):
    return data[resultType] / 1000

runTrial(True)

resultsForChangeBox = {
    'win': 0,
    'lose': 0
}

resultsForWithoutChangeBox = {
    'win': 0,
    'lose': 0
}

for i in range(1000):
    #check 1000 times if contestant win or lose game with change card status
    if runTrial(True):
        resultsForChangeBox['win'] += 1
    else:
        resultsForChangeBox['lose'] += 1

for i in range(1000):
    #check 1000 times if contestant win or lose game with keep card status
    if runTrial(False):
        resultsForWithoutChangeBox['win'] += 1
    else:
        resultsForWithoutChangeBox['lose'] += 1


print("If contestant change the box in hand win possibility = " ,getResultPossibility(resultsForChangeBox, 'win'))
print("If contestant keep the box in hand win possibility = " ,getResultPossibility(resultsForWithoutChangeBox, 'win'))

print("If contestant change the box in hand lose possibility = " ,getResultPossibility(resultsForChangeBox, 'lose'))
print("If contestant keep the box in hand lose possibility = " ,getResultPossibility(resultsForWithoutChangeBox, 'lose'))
