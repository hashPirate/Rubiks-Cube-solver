# 3x3 Rubiks cube project started November 20th 
# I have restricted myself to intro to programming techniques to prove that advanced projects can be built upon learning the basics. I did not use anything in this project that was not taught in my intro to programming class.
# AND ALL IN 1 CLASS FILE!
# This project will be recoded using more advanced data structures when I get bored

# cube = ['WWWWWWWWW','RRRRRRRRR','YYYYYYYYY','OOOOOOOOO','BBBBBBBBB','GGGGGGGGG']
# cube[0] faces you and cube[4] is the bottom and cube[5] is the top

from pystyle import Colors

cube = ['BBBBBBBBB','RRRRRRRRR','GGGGGGGGG','OOOOOOOOO','WWWWWWWWW','YYYYYYYYY']
wordDict = {'B':'Blue','R':'Red','O':'Orange','G':'Green','W':'White','Y':'Yellow'}



def rotateStringClockwise(string):
    stringlist = []
    for i in string:stringlist.append(i)
    tempchar0,tempchar2,tempchar6,tempchar8 = stringlist[0],stringlist[2],stringlist[6],stringlist[8]
    stringlist[0],stringlist[2],stringlist[6],stringlist[8],newstring = tempchar6,tempchar0,tempchar8,tempchar2,''
    tempchar1,tempchar3,tempchar5,tempchar7 = stringlist[1],stringlist[3],stringlist[5],stringlist[7]
    stringlist[1],stringlist[3],stringlist[5],stringlist[7] = tempchar3,tempchar7,tempchar1,tempchar5
    for i in range(len(stringlist)):newstring+=stringlist[i]
    return newstring

def rotateStringCounterclockwise(string):
    stringlist = []
    for i in string:stringlist.append(i)
    tempchar0,tempchar2,tempchar6,tempchar8 = stringlist[0],stringlist[2],stringlist[6],stringlist[8]
    stringlist[0],stringlist[2],stringlist[6],stringlist[8],newstring = tempchar2,tempchar8,tempchar0,tempchar6,''
    tempchar1,tempchar3,tempchar5,tempchar7 = stringlist[1],stringlist[3],stringlist[5],stringlist[7]
    stringlist[1],stringlist[3],stringlist[5],stringlist[7] = tempchar5,tempchar1,tempchar7,tempchar3
    for i in range(len(stringlist)):newstring+=stringlist[i]
    return newstring




def doMove(cube,move):
    if move=='U-':
        tempvar = []
        for i in range(4):
            tempvar.append(cube[i][:3])
            if(i==0):cube[0] = cube[3][:3] + cube[0][3:]
            else: cube[i] = tempvar[i-1] + cube[i][3:]
        cube[5] = rotateStringCounterclockwise(cube[5])
    if move=='U':
        tempvar = cube[0][:3]
        for i in range(4):
            if(i==0):cube[0] = cube[1][:3] + cube[0][3:]
            elif(i<3): cube[i] = cube[i+1][:3] + cube[i][3:]
            else: cube[i] = tempvar + cube[i][3:]
        cube[5] = rotateStringClockwise(cube[5])
    if move=='F':
        tempvar1,tempvar2,tempvar3,tempvar4 = cube[4][:3], cube[3][2] + cube[3][5] + cube[3][8],cube[5][6:9], cube[1][0] + cube[1][3] + cube[1][6]
        cube[4],cube[3],cube[5],cube[1] = tempvar4[2]+ tempvar4[1] + tempvar4[0] + cube[4][3:],cube[3][:2] + tempvar1[0] + cube[3][3:5] + tempvar1[1] + cube[3][6:8] + tempvar1[2],cube[5][:6] + tempvar2[2] + tempvar2[1]+tempvar2[0], tempvar3[0] + cube[1][1:3]+ tempvar3[1] + cube[1][4:6]+ tempvar3[2] + cube[1][7:9]
        cube[0] = rotateStringClockwise(cube[0])
    if move=='F-':
        tempvar1,tempvar2,tempvar3,tempvar4 = cube[4][:3], cube[3][2] + cube[3][5] + cube[3][8],cube[5][6] + cube[5][7] + cube[5][8], cube[1][0] + cube[1][3] + cube[1][6]
        cube[4],cube[3],cube[5],cube[1] = tempvar2 + cube[4][3:],cube[3][:2] + tempvar3[2] + cube[3][3:5] + tempvar3[1] + cube[3][6:8] + tempvar3[0],cube[5][:6] + tempvar4, tempvar1[2] + cube[1][1:3]+ tempvar1[1] + cube[1][4:6]+ tempvar1[0] + cube[1][7:9]
        cube[0] = rotateStringCounterclockwise(cube[0])
    if move=='R':
        tempvar1,tempvar2,tempvar3,tempvar4 = cube[0][2] + cube[0][5] + cube[0][8], cube[5][2] + cube[5][5] + cube[5][8],cube[2][0] + cube[2][3] + cube[2][6], cube[4][2] + cube[4][5] + cube[4][8]
        cube[0],cube[5],cube[2],cube[4] = cube[0][:2] + tempvar4[0] + cube[0][3:5] + tempvar4[1] + cube[0][6:8] + tempvar4[2], cube[5][:2] + tempvar1[0] + cube[5][3:5] + tempvar1[1] + cube[5][6:8] + tempvar1[2], tempvar2[2] + cube[2][1:3]+ tempvar2[1] + cube[2][4:6]+ tempvar2[0] + cube[2][7:9], cube[4][:2] + tempvar3[2] + cube[4][3:5] + tempvar3[1] + cube[4][6:8] + tempvar3[0]
        cube[1] = rotateStringClockwise(cube[1])
    if move=='R-':
        tempvar1,tempvar2,tempvar3,tempvar4 = cube[0][2] + cube[0][5] + cube[0][8], cube[5][2] + cube[5][5] + cube[5][8],cube[2][0] + cube[2][3] + cube[2][6], cube[4][2] + cube[4][5] + cube[4][8]
        cube[0],cube[5],cube[2],cube[4] = cube[0][:2] + tempvar2[0] + cube[0][3:5] + tempvar2[1] + cube[0][6:8] + tempvar2[2], cube[5][:2] + tempvar3[2] + cube[5][3:5] + tempvar3[1] + cube[5][6:8] + tempvar3[0], tempvar4[2] + cube[2][1:3]+ tempvar4[1] + cube[2][4:6]+ tempvar4[0] + cube[2][7:9], cube[4][:2] + tempvar1[0] + cube[4][3:5] + tempvar1[1] + cube[4][6:8] + tempvar1[2]
        cube[1] = rotateStringCounterclockwise(cube[1])
    if move=='L':
        tempvar1,tempvar2,tempvar3,tempvar4 = cube[0][0] + cube[0][3] + cube[0][6], cube[4][0] + cube[4][3] + cube[4][6], cube[2][2] + cube[2][5] + cube[2][8], cube[5][0] + cube[5][3] + cube[5][6]
        cube[0],cube[4],cube[2],cube[5] = tempvar4[0] + cube[0][1:3] + tempvar4[1] + cube[0][4:6] + tempvar4[2] + cube[0][7:9], tempvar1[0] + cube[4][1:3] + tempvar1[1] + cube[4][4:6] + tempvar1[2] + cube[4][7:9], cube[2][:2] + tempvar2[2] + cube[2][3:5] + tempvar2[1] + cube[2][6:8] + tempvar2[0], tempvar3[2] + cube[5][1:3] + tempvar3[1] + cube[5][4:6] + tempvar3[0] + cube[5][7:9]
        cube[3] = rotateStringClockwise(cube[3])
    if move=='L-':
        tempvar1,tempvar2,tempvar3,tempvar4 = cube[0][0] + cube[0][3] + cube[0][6], cube[4][0] + cube[4][3] + cube[4][6], cube[2][2] + cube[2][5] + cube[2][8], cube[5][0] + cube[5][3] + cube[5][6]
        cube[0],cube[4],cube[2],cube[5] = tempvar2[0] + cube[0][1:3] + tempvar2[1] + cube[0][4:6] + tempvar2[2] + cube[0][7:9], tempvar3[2] + cube[4][1:3] + tempvar3[1] + cube[4][4:6] + tempvar3[0] + cube[4][7:9], cube[2][:2] + tempvar4[2] + cube[2][3:5] + tempvar4[1] + cube[2][6:8] + tempvar4[0], tempvar1[0] + cube[5][1:3] + tempvar1[1] + cube[5][4:6] + tempvar1[2] + cube[5][7:9]
        cube[3] = rotateStringCounterclockwise(cube[3])
        



def findUnsolvedPair(cube):
    if(cube[0][5]!=cube[0][4] or cube[1][3]!=cube[1][4]): return 0
    if(cube[1][5]!=cube[1][4] or cube[2][3]!=cube[2][4]): return 1
    if(cube[2][5]!=cube[2][4] or cube[3][3]!=cube[3][4]): return 2
    if(cube[3][5]!=cube[3][4] or cube[0][3]!=cube[0][4]): return 3
    return 'T'

def turnCubeRight(cube):
    tempside0,tempside1,tempside2,tempside3 = cube[0],cube[1],cube[2],cube[3]
    cube[0],cube[1],cube[2],cube[3] = tempside1,tempside2,tempside3,tempside0
    cube[5],cube[4] = rotateStringClockwise(cube[5]),rotateStringClockwise(cube[4])

def getMovesFromString(string):
    returnlist = []
    for index,value in enumerate(string):
        if(index!=len(string)-1):
            if(string[index+1]!='-'): returnlist.append(value)
            else: 
                returnlist.append(value + string[index+1])
        else:returnlist.append(value)
    for value in returnlist:
        if(value=='-'):returnlist.remove(value)
    return returnlist

def doSecondLayerAlgorithmR(cube):
    print("Do these moves: U R U' R' U' F' U F ")
    for i in (getMovesFromString('URU-R-U-F-UF')):doMove(cube,i)

def doSecondLayerAlgorithmL(cube):
    print("Do these moves: U' L' U L U F U' F'")
    for i in (getMovesFromString('U-L-ULUFU-F-')): doMove(cube,i)

def solveSecondLayer(cube):
    while(findUnsolvedPair(cube)!='T'):
        tosolve,unum = '',0
        for i in range(4):
            unum = i
            if(cube[0][1]==cube[0][4] and cube[5][7]!=cube[5][4]):
                tosolve = 0
                break
            if(cube[1][1]==cube[1][4] and cube[5][5]!=cube[5][4]):
                tosolve = 1
                break
            if(cube[2][1]==cube[2][4] and cube[5][1]!=cube[5][4]):
                tosolve = 2
                break
            if(cube[3][1]==cube[3][4] and cube[5][3]!=cube[5][4]):
                tosolve = 3
                break
            doMove(cube,'U')
        else:
            print(f'\nTurn the cube to the {wordDict[cube[findUnsolvedPair(cube)][4]]} side!')
            for i in range(findUnsolvedPair(cube)): turnCubeRight(cube)
            doSecondLayerAlgorithmR(cube)
            
        if(tosolve!=''):
            print(f'\nDo these moves: {"U"*unum}')
            for i in range(tosolve):
                turnCubeRight(cube)
            if(tosolve!=0):
                print(f'Turn the cube to the {wordDict[cube[0][4]]} side!')
            if(cube[5][7] == cube[3][4]):doSecondLayerAlgorithmL(cube)
            if(cube[5][7] == cube[1][4]):doSecondLayerAlgorithmR(cube)
        printCube(cube)
        q = input('Continue?')
    print('SECOND LAYER SOLVED!!!')
        
def doTopCrossMove(cube,type):
    if(type=='line'):
        for i in (getMovesFromString('FRUR-U-F-')):
            doMove(cube,i)
        print("Do these moves: F R U R' U' F'")
    if(type=='l'):
        for i in getMovesFromString('FURU-R-F-'):
            doMove(cube,i)
        print("Do these moves: F U R U' R' F' ")

def isTopCrossSolved(cube):
    if(cube[5][1]==cube[5][4] and cube[5][3]==cube[5][4] and cube[5][7]==cube[5][4]and cube[5][5]==cube[5][4]):return True
    return False

def solveTopCross(cube):
    while(isTopCrossSolved(cube)==False):
        if((cube[5][1]==cube[5][4] and cube[5][7]==cube[5][4] and cube[5][3]!=cube[5][4])):
            print('Do this Move: U')
            doMove(cube,'U')
            doTopCrossMove(cube,'line')
        elif((cube[5][3]==cube[5][4] and cube[5][5]==cube[5][4] and cube[5][1]!=cube[5][4])):
            doTopCrossMove(cube,'line')
        else:
            for i in range(4):
                if(cube[5][1]==cube[5][4] and cube[5][3]==cube[5][4]): 
                    print(f'Do these Moves - {"U"*i}')
                    doTopCrossMove(cube,'l')
                    break
                doMove(cube,'U')
            else:
                doTopCrossMove(cube,'line')
                
            

    #Continue here

    
    









    
def printCube(cube):
    colorDict = {'W':Colors.white,'Y':Colors.yellow,'B':Colors.turquoise,'G':Colors.green,'R':Colors.red,'O':Colors.orange}
    numspaces = 4
    for index,value in enumerate(cube[5]):
        colorval = f'{colorDict[value]}{value}'
        if(index%3==0): print('\n' + numspaces*' ' + colorval,end='')
        else: print(colorval,end='')
    print()
    nextlinestring,listOfCubes = '',[3,0,1,2]
    for num in listOfCubes:
        for index,value in enumerate(cube[num][:3]):nextlinestring += f'{colorDict[value]}{value}'
        nextlinestring += ' '
    print(nextlinestring)
    nextlinestring = ''
    for num in listOfCubes:
        for index,value in enumerate(cube[num][3:6]):nextlinestring += f'{colorDict[value]}{value}'
        nextlinestring += ' '
    print(nextlinestring)
    nextlinestring = ''
    for num in listOfCubes:
        for index,value in enumerate(cube[num][6:9]):nextlinestring += f'{colorDict[value]}{value}'
        nextlinestring += ' '
    print(nextlinestring)
    for index,value in enumerate(cube[4]):
        colorval = f'{colorDict[value]}{value}'
        if(index==0):print(numspaces*' ' + colorval,end='')
        elif(index%3==0): print('\n' + numspaces*' ' + colorval,end='')
        else: print(colorval,end='')
    print()



    
exampleCube = f'''{Colors.white}
    555 (Upper Side)
    555
    555
333 000 111 222 (2 is the side on the back!)
333 000 111 222
333 000 111 222
    444
    444
    444 (Solved first layer 4)

''' 

cube = []
print(exampleCube)
print('Check the diagram above to reference and enter the sides of a cube with the first layer solved!')
for i in range(6):
    sideinput = input(f'Enter side {i}: ').upper()
    cube.append(sideinput)

printCube(cube)
solveSecondLayer(cube)
solveTopCross(cube)


printCube(cube)



