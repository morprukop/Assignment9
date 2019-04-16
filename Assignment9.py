import random
def battleShipgame():
    #print board
    def print_board(board):
        for row in board:
            print(' '.join(row))
    
    #create board
    board = []
    for x in range(5):
        board.append(["o"] * 5)
     
    #set up board
    random_row = random.randint(0, 4)
    random_column = random.randint(0, 4)
    
    c = 0
    #play game
    for attack in range(4):
        try:
            guest_row = int(input("what row do you want to attack: "))
            guest_column = int(input("what column do you want to attack: "))
        except ValueError:
            print("Only input numbers")
            continue
        try:
            board[guest_row][guest_column] = "X"
            
        except IndexError:
            print("Do not input numbers past 4")
            continue
        if((random_row == guest_row)and(random_column == guest_column)):
            board[guest_row][guest_column] = "F"
            print("CONGRATS YOU SUNK A SHIP")
        print_board(board)
        print("\n")
        c = c + 1
        if(c == 4):
            print("You did not sink any ships: game over")
    
land = []
#create the land
for x in range(5):
    land.append(["^"] * 5)
#place flower at original place
# flower = u'that\U+1F337'

land[0][3] = "@"

#print land
def printLand(land):
        for row in land:
            print(' '.join(row))

column = 0
row = 0
land[row][column] = "6"
printLand(land)
print("\n")
def moveKang(direction):
    global column
    global row
    if((row == 2) and (column == 3)):
        land[row][column] = "@"
    else:
        land[row][column] = "^"
    if(direction == "left"):
        column = column - 1
    if(direction == "right"):       
        column = column + 1
    if(direction == "up"):      
        row = row-1
    if(direction == "down"):     
        row = row + 1
    land[row][column] = "6" 
    printLand(land)
    print("\n") 


moveKang("right") 
moveKang("right")   
moveKang("right") 
moveKang("down") 
moveKang("down") 
moveKang("right") 

battleShipgame()
        
            
            
            