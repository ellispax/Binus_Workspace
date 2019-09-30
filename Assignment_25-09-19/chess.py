#--------------------------------------------------------------------------
#        !!!!! ------ strictly python v3.*    !!!!!!
#   filename : chess.py
#   author   : paxman
#   program  : an apllication that show the available movements for a
#              knight in a game if chess
#--------------------------------------------------------------------------
#from typing import List, Union

def Menu():
    print("""
----------     C H E S S    [ K N I G H T - MOVE PREDICTION ]    ------------

 [*]  This program determines the possible moves for the KNIGHT
      in a game of chess depending on the piece's current position .eg A7
            -------------------------------------------

 [->] Enter the KNIGHT'S  position (if -NO- position is selected one of 
      the  default positions of a KNIGHT chess piece will be used )
            
""")

#--------------------------------------------------------

def possibleMove(x,y):
    moveList = [] # will be used to store the moves
    # this list of chained if conditions will check if the move is possible
    # --------------------- currently checking for the positive 'x - axis'
    if ((x + 2) <= 8 and (x + 2) >= 1) and ((y + 1) <= 8 and (y + 1) >= 1):
        x1 = y + 3; y1 = y + 1
        a = [x1,y1];
        moveList.append(a)
    if ((x + 2) <= 8 and (x + 2) >= 1) and ((y - 1) <= 8 and (y - 1) >= 1):
        x1 = x + 2; y1 = y - 1
        a = [x1,y1]
        moveList.append(a)
    if ((y + 2) <= 8 and (y + 2) >= 1) and ((x + 1) <= 8 and (x + 1) >= 1):
        y1= y + 2; x1 = x + 1
        a = [x1,y1]
        moveList.append(a)
    if ((y - 2) <= 8 and (y - 2) >= 1) and ((x + 1) <= 8 and (x + 1) >= 1):
        y1 =y- 2; x1 =x + 1
        a = [x1,y1]
        moveList.append(a)

    # --------------------- currently checking for the negative 'x - axis'
    if ((y + 2) <= 8 and (y + 2) >= 1) and ((x - 1) <= 8 and (x - 1) >= 1):
        y1 =y + 2; x1 = x - 1
        a = [x1,y1]
        moveList.append(a)
    if ((y - 2) <= 8 and (y - 2) >= 1) and ((x - 1) <= 8 and (x - 1) >= 1):
        y1 = y - 2; x1 = x -1
        a = [x1,y1]
        moveList.append(a)
    if ((y + 1) <= 8 and (y + 1) >= 1) and ((x - 2) <= 8 and (x - 2) >= 1):
        y1=y + 1; x1=x - 2
        a = [x1,y1]
        moveList.append(a)
    if ((y - 1) <= 8 and (y - 1) >= 1) and ((x - 2) <= 8 and (x - 2) >= 1):
        y1=y - 1; x1=x - 2
        a = [x1,y1]
        moveList.append(a)
    # -------------------------------------------------collected all moves possible
    print("\n Done collecting all " + str(len(moveList)) + " possible moves from \n the position -> " +
          str(UsersResult[1]) + str(UsersResult[2]) + "\n")
    return moveList


#--------------------------------------------------------
def Selection():

    select = input()
    select = select.upper()
    #checking for input and throwing exception
    if (len(select) == 1):
        select = select[0] + "-"
        select = select.upper()
        Result = [False, select[0], select[1]]
        return Result
    elif len(select) == 0:
        select = "b1" or "g1"
    # declaring variables used
    char1 = select[0];    char2 = select[1]
    alphaList = ('A','B','C','D','E','F','G');  numList = (1,2,3,4,5,6,7,8)
    trueChar1 = False; trueChar2 = False # will be used to check if coordinates are valid
    # now checking for validity [char1]
    for checkC1 in alphaList:
        if checkC1 == char1 :
            trueChar1 = True

    # now checking for validity [char2]
    for checkC2 in alphaList:
        if checkC2 == char1 :
            trueChar2 = True

    if len(select) == 2:
        ValidCoord = trueChar1 and trueChar2  # making sure the values were correct
    else:ValidCoord = False

    Result = [ValidCoord, char1, char2]

    return Result

#--------------------------------------------------------
def coord_X_ToNum(coord_Alpha):
    # changing the ALPHA coordinate to a NUM
    if (coord_Alpha == 'A'):
        coord_Alpha = 1
    elif (coord_Alpha == 'B'):
        coord_Alpha = 2
    elif (coord_Alpha == 'C'):
        coord_Alpha = 3
    elif (coord_Alpha == 'D'):
        coord_Alpha = 4
    elif (coord_Alpha == 'E'):
        coord_Alpha = 5
    elif (coord_Alpha == 'F'):
        coord_Alpha = 6
    elif (coord_Alpha == 'G'):
        coord_Alpha = 7
    elif (coord_Alpha == 'H'):
        coord_Alpha = 8
    return  coord_Alpha


#---------------------------------------------------------

def printPos():

# these will be used for printing the chess board
    printVals = "  -   -   -   -   -   -   -   - "
    Knight = " o "; PossibleMove = " + "
    alphaList = "_________________________________\n" +\
                "|-A-|-B-|-C-|-D-|-E-|-F-|-G-|-H-\n" +\
                "_________________________________\n"
    x = cdX; y = cdY
    AvailableMoves = list2
    count = 0; xVal = 0 # we will be using the x - coordinate for determining the row position
    yVal = 0             # y - coordinate for positioning the key-char(s)
    initY = 0; finY = 0  # initial and final positions occupied in the string

    # The Chessboard list will be containing the print info
    ChessBoard = [printVals,printVals,
                  printVals,printVals,
                  printVals,printVals,
                  printVals,printVals]  # assigning string whitespace to the chessboard printout
    SamelineMove = [False,False,False,False,  # these will be used to check if
                    False,False,False,False,] # two moves exist on the same line and prevent overwriting

    while count < len(AvailableMoves):
        xVal = AvailableMoves[count][0] - 1
        yVal = AvailableMoves[count][1] - 1; initY = yVal * 4; finY = initY + 4  # ----for replacing the string values

        if(SamelineMove[xVal] == True): # Prevention of string truncation because of move on same x-coordinate
            Row = printVals[0:(initY + 1)] + PossibleMove + ChessBoard[xVal][finY:] # prevents truncation by taking from the previous entrance into the chessboard
            ChessBoard[xVal] = Row  # assigning the ready to be printed row
            count += 1
            continue

        Row = printVals[0:(initY + 1)] + PossibleMove + printVals[finY:]
        ChessBoard[xVal] = Row # assigning the ready to be printed row
        SamelineMove[xVal] = True # toggling the line to contain input
        count += 1
    # after embedding the moves ..its time to embed the knight


    xVal = x - 1; yVal = y - 1;
    initY = yVal * 4;
    finY = initY + 4  # ----for replacing the string values
    Row = printVals[0:(initY + 1)] + Knight + ChessBoard[xVal][finY:]  # prevents truncation by taking from the previous entrance into the chessboard
    ChessBoard[xVal] = Row  # assigning the ready to be printed row

    # printing the coordinates

    print(alphaList)
    for theRow in ChessBoard:
        print(theRow)

#--------------------  M A I N        P R O G R A M  ---------------------------
#            -------------- H E R E  -------------------------

on = 1 # looping for correct input
Menu()
UsersResult = Selection()
alpha = UsersResult[1]
num = UsersResult[2]
if  UsersResult[0] == False:
    print(UsersResult[0])
    print(f"""" Your input '{UsersResult[1]}{UsersResult[2]}' is a wrong coordinate
     --------------> Retrying...
                 * * *  * *  * * * * * * * * * * * * 
    [->] Please Enter the KNIGHT'S  position e.g[ BE ](if -NO- position is selected one of 
          the default positions of a KNIGHT chess piece will be used... )
    """)
else:  print(f" Your input '{alpha}{num}' is the coordinate")
cdX = int(coord_X_ToNum(alpha)); cdY = int(num) # some errors ocuured which needed explicit casting
list2 = possibleMove(cdX,cdY)
printPos()

