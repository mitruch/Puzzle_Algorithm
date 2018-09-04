import random
import math
import os

#Autor programu: Katarzyna Mitrus
#2017-12-18
#grupa z godziny 13:15

class Puzzle():
    matrix = []
    positions = { '1':(0,0), '2':(1,0), '3':(2,0), '4':(0,1), '5':(1,1), '6':(2,1), '7':(0,2), '8':(1,2), 'X':(2,2)}
    elements = ['1', '2', '3', '4', '5', '6', '7', '8', 'X']
    
    #inicjalizacja
    def __init__(self):
        #losowanie elementow 
        randomElements = random.sample(self.elements, len(self.elements))
        for i in range(0, 9, 3):
            self.matrix.append([x for x in randomElements[i:i+3]])
        print("Start puzzle combination: ")
        for row in self.matrix:
            print(row)

    #metoda obliczajaca odleglosc elementu od wlasciwej pozycji
    def numDist(self, num, x, y):
        if(num == 'X'):
            return 0
        difX = math.fabs(self.positions[num][0] - x)
        difY = math.fabs(self.positions[num][1] - y)
        dist = difX + difY
        return dist

    #metoda obliczajaca Manhattan Distance
    def manhattanDist(self, table = None):
        if table == None:
            table = self.matrix
        mnhtDist = 0
        for i in range(len(table)):
            for j in range(len(table)):
                mnhtDist = mnhtDist + self.numDist(table[i][j], i, j);
        return mnhtDist

    #metoda obliczajaca Manhattan Distance
    def getActualPos(self, num, table = None):
        if table == None:
            table = self.matrix
        index = 0
        for i in range(len(table)):
            for j in range(len(table)):
                if num == table[i][j]:
                    index = (i, j)
        return index

    #metoda zwracajaca macierz z przesunietym pustym polem
    def moveBlank(self, destination):
        nextMatrix = [list(x) for x in self.matrix]
        destNum = 0
        blankPos = self.getActualPos('X')

        if destination == 'left':
            try:
                destNum = -1
                move = blankPos[1] + destNum
                if move < 0:
                    return None
                nextMatrix[blankPos[0]][blankPos[1]] = self.matrix[blankPos[0]][blankPos[1] + destNum]
                nextMatrix[blankPos[0]][blankPos[1] + destNum] = 'X'
                return nextMatrix
            except Exception:
                return None        

        elif destination == 'right':
            try:
                destNum = 1
                nextMatrix[blankPos[0]][blankPos[1]] = self.matrix[blankPos[0]][blankPos[1] + destNum]
                nextMatrix[blankPos[0]][blankPos[1] + destNum] = 'X'
                return nextMatrix
            except Exception:
                return None          

        elif destination == 'up':
            try:
                destNum = -1
                move = blankPos[0] + destNum
                if move < 0:
                    return None
                nextMatrix[blankPos[0]][blankPos[1]] = self.matrix[blankPos[0] + destNum][blankPos[1]]
                nextMatrix[blankPos[0] + destNum][blankPos[1]] = 'X'
                return nextMatrix
            except Exception:
                return None

        elif destination == 'down':
            try:
                destNum = 1
                nextMatrix[blankPos[0]][blankPos[1]] = self.matrix[blankPos[0] + destNum][blankPos[1]]
                nextMatrix[blankPos[0] + destNum][blankPos[1]] = 'X'
                return nextMatrix
            except Exception:
                return None

    #wybor optymalnej sciezki
    def selectPath(self, lastDist):      
        destinations = ['up', 'down', 'right', 'left']
        pathCost = dict()
        path = []
        for dest in destinations:
            path = self.moveBlank(dest)
            if path is not None:
                mnhtDist = self.manhattanDist(path)
                pathCost[dest] = mnhtDist
        minDist = min(pathCost.values())
        if minDist > lastDist:
            print("Next minimum manhattan dist: ", minDist , ">", lastDist )
            return None
        lastDist = minDist
        minPaths = []
        for key, value in pathCost.items():
            if value == minDist:
                minPaths.append(key)
        selectedDest = random.choice(minPaths)
        selectedPth = self.moveBlank(selectedDest)
        print("Selected Dest: ", selectedDest, "Manhattan Distance: ", pathCost[selectedDest])
        self.matrix = [list(x) for x in selectedPth]
        return 1   
        
puz = Puzzle()
mnhtDist = puz.manhattanDist()
found = True

while mnhtDist != 0:
    if puz.selectPath(mnhtDist) is None:
        print("Local Minimum Found ! ")
        found = False
        break
    for row in puz.matrix:
        print(row)

    mnhtDist = puz.manhattanDist()

if found:
    print("Puzzle Problem Solved !")
    for row in puz.matrix:
        print(row)

os.system("pause")