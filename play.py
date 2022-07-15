#importing modules and dependencies
from random import randint
from tabulate import tabulate
from colorama import Fore, init



#functions

#creating the table wit the values receiving the point_list
def createTable(dataList):
    #create data
    data = [ 
        [dataList[13], dataList[12], dataList[11], dataList[10],dataList[9],dataList[8],dataList[7], dataList[6]],
        ['-', dataList[0], dataList[1], dataList[2],dataList[3],dataList[4],dataList[5], '-'],
        ['-','G', 'H', 'I', 'J', 'K', 'L', '-']]


#define header names
    col_names = ["TOTAL P2", "A", "B", "C", "D", "E", "F", 'TOTAL P1']


#display table
    table = tabulate(data, headers=col_names,  tablefmt="fancy_grid")
    print(table)


#ask For element

def askForElement():
    selectContainer = input('Ingresa la letra de la  casilla que deseas seleccionar \n').upper()

    if selectContainer == 'G': return 0
    elif selectContainer == 'H': return 1
    elif selectContainer == 'I': return 2
    elif selectContainer == 'J': return 3
    elif selectContainer == 'K': return 4
    elif selectContainer == 'L': return 5
    elif selectContainer == 'A': return 12
    elif selectContainer == 'B': return 11
    elif selectContainer == 'C': return 10
    elif selectContainer == 'D': return 9
    elif selectContainer == 'E': return 8
    elif selectContainer == 'F': return 7    


def setSquare(container):
    if container == 0: return 'G' 
    elif container == 1: return 'H' 
    elif container == 2: return 'I' 
    elif container == 3: return 'J' 
    elif container == 4: return 'K' 
    elif container == 5: return 'L' 
    elif container == 12: return 'A'
    elif container == 11: return 'B'
    elif container == 10: return 'C'
    elif container == 9: return 'D' 
    elif container == 8: return 'E' 
    elif container == 7: return 'F' 


def onePlayerTurn():
    index = 7
    for i in range(7,12):
        o_container = 12 - index
        turn_end = i + points_list[i]
        if 7<= turn_end <= 12 and points_list[turn_end] == 0 and o_container >0 and points_list[i] != 0:
            index = i
            break
        elif i + points_list[i] == 13:
            index = i
            break 
        else:
            index = randint(7,12)
            while points_list[index] == 0:
                   index = randint(7,12)

    init(autoreset=True)
    print(Fore.CYAN + 'Casilla movida ' + setSquare(index))         
    return index


#return the index of the selected container 
def selectElement(isOnePlayer):

    if isOnePlayer == True and current_player == 2:
       return onePlayerTurn() 

    elif isOnePlayer == True and current_player == 1:
        turnValue = askForElement()

        while points_list[turnValue] == 0:
            init(autoreset=True)
            print(Fore.RED + 'La casilla seleccionada no tiene ninguna ficha')
            turnValue = askForElement()

        return turnValue

    elif isOnePlayer == False:
        turnValue = askForElement()

        while points_list[turnValue] == 0:
            init(autoreset=True)
            print(Fore.RED + 'La casilla seleccionada no tiene ninguna ficha')
            turnValue = askForElement()

        return turnValue


        
        
        




#validate incorrect container

def validateIncorrectContainer(oldest, newest, turn, last):
    if oldest[6] != newest[6] and turn == 2:
      
        newest[6] = newest[6] - 1
        if last < 12:
            newest[last + 1 ] = newest[last + 1] + 1
        else:
            newest[0] += 1    
    

    elif oldest[13] != newest[13] and turn == 1:
        newest[13] = newest[13] - 1
        if last < 12:
            newest[last + 1 ] = newest[last + 1] + 1
        else:
            newest[0] += 1 
    
    return newest


def cloneList(toClone):
    newList = []
    for item in toClone:
        newList.append(item)
    return newList    




#defining the new values of the list when select a container
def moveValues(container, dataList):

    
    global lastChanged
    #setting a for loop to distribute the values of the container in the next containers. That means if you have 3 items in the container the next 3 containers will add 1

    oldList = cloneList(dataList)

    for i in range(dataList[container]+ 1):

        #keeping the value of the next container without filling
        next_index = container + i

        #if the next index is minus than 13 add 1 to the value
        if next_index <= 13:
            next_number = dataList[next_index]
            dataList[next_index] = next_number + 1
            lastChanged =  next_index

        #else rest 14 to loop, that means if you have that the next index is 14, this container does not exit so you rest 14 and you'll fill the container with the id 0 

        else:
            next_index = next_index - 14
            next_number = dataList[next_index]
            dataList[next_index] = next_number + 1
          
            lastChanged = next_index
        
    dataList[container] = 0



    return dataList


#changing turn 

def changeTurn(lastChanged, player):
    if player == 1 and lastChanged == 6: return player
    elif player == 2 and lastChanged == 13: return player
    else:
        if player == 1: return 2
        if player == 2: return 1


#validate turn 
def validateTurn(player, container):
  
     
    if player == 1:
        if container in player1List: return 1
        else: return 0
    elif player == 2:
        if container in player2List: return 1
        else: return 0


def oposite():
    if lastChanged >= 0 and lastChanged <= 6: return 12 - lastChanged

    elif lastChanged >= 7 and lastChanged <= 12: return 12 - lastChanged

def validateOposite(dataList, oldList):
    oposite_container = oposite()
    if  lastChanged >= 0 and lastChanged <= 6 and oldList[lastChanged] == 0 and lastChanged != 13 and lastChanged !=6 and dataList[oposite_container] != 0 and current_player == 1:
        
        dataList[6] += dataList[oposite_container] + 1
        dataList[oposite_container] = 0
        dataList[lastChanged] = 0

        return dataList
    elif lastChanged >= 6 and lastChanged <= 12 and oldList[lastChanged] == 0 and lastChanged != 13 and lastChanged !=6 and dataList[oposite_container] != 0 and current_player == 2:
        dataList[13] += dataList[oposite_container] + 1
        dataList[oposite_container] = 0
        dataList[lastChanged] = 0

        return dataList

    else: return dataList          





def validateEndGame(player):

    sume = 0

    if player == 1:
        for item in player1List:
            sume += points_list[item]
   
    elif player == 2:
        for item in player2List:
            sume += points_list[item]

    if sume == 0: return 1
    else: return 0

def gameMode():
    mode = input('A: Un jugador \n' 'B: Dos jugadores \n').upper()
    if mode == 'A': return True
    elif mode == 'B': return False


def setWinner():
    if points_list[6] > points_list[13]:
        init(autoreset=True)
        print(Fore.GREEN + 'El ganador es el jugador 1')
      
    elif points_list[6] < points_list[13]:
        init(autoreset=True) 
        print(Fore.GREEN + 'El ganador es el jugador 2')
      
    else:
        init(autoreset=True) 
        print(Fore.GREEN + 'Empate')

def printPoints():
    init(autoreset=True)
    print(Fore.BLUE + 'Juagador 1: ' + str(points_list[6]))
    init(autoreset=True)
    print(Fore.BLUE + 'Juagador 2: ' + str(points_list[13]))

#establishing a list where each element represents the number of tokens that each container has.

points_list = [4,4,4,4,4,4,0,4,4,4,4,4,4,0]

#cloning point list to keep a previus status 
oldList =  cloneList(points_list)

#squares belonging to player 1
player1List = [0,1,2,3,4,5]

#squares belonging to player 2
player2List = [7,8,9,10,11,12]


#last container changed. Default 0
lastChanged = 0

#defining who is playing. Generate a random turn (1 or 2)
current_player = randint(1,2)


#end game indicator (true or false)
endGame = 0




#main function
def main():
    global endGame
    global points_list
    global current_player

    onePlayer = gameMode()
    

    while(endGame == 0):

       
        #creating table 
        createTable(points_list)
                    #priting the current player
        init(autoreset=True)
        print(Fore.GREEN + 'Turno del jugador %i' %current_player)

        #asking for a container 
        selectedContainer = selectElement(onePlayer)

        if validateTurn(current_player, selectedContainer) == 1:
            oldList = cloneList(points_list)
            #moving te values of the selected contaienr

        
            points_list =  moveValues(selectedContainer, points_list)
            points_list = validateIncorrectContainer(oldList, points_list, current_player, lastChanged)   
            points_list = validateOposite(points_list, oldList)
            current_player = changeTurn(lastChanged, current_player)
            endGame = validateEndGame(current_player)
        

        else:
            init(autoreset=True)
            print(Fore.RED + 'No es tu turno')
        

    createTable(points_list)
    setWinner()
    printPoints()


main()
