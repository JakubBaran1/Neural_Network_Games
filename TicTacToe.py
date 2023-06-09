from PIL import Image, ImageTk
import tkinter as tk



###########################
#Tic Tac Toe game in python

board = [' ' for x in range(10)]

def insertLetter(letter, pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == ' '

def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    
def isWinner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or(bo[1] == le and bo[2] == le and bo[3] == le) or(bo[1] == le and bo[4] == le and bo[7] == le) or(bo[2] == le and bo[5] == le and bo[8] == le) or(bo[3] == le and bo[6] == le and bo[9] == le) or(bo[1] == le and bo[5] == le and bo[9] == le) or(bo[3] == le and bo[5] == le and bo[7] == le)

# Function to handle click events
def on_click(row, col):
    # Determine the cell number based on the clicked image
    cell_number = row * 3 + col + 1
    print("Cell number:", cell_number)

    # Update the board with the corresponding value
    board[row*3+col+1] = 'X'  # Assuming the player placing X in the cell

    # Update the display
    update_display()


def playerMove():
    run = True
    while run:
        move = input('Please select a position to place an \'X\' (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')
            
    update_display()


# def playerMove():
#     run = True
#     move = 0  # Initialize move to 0
    
#     # Function to handle the click event for player move
#     def on_click_player(row, col):
#         nonlocal move
#         cell_number = row * 3 + col + 1
#         if spaceIsFree(cell_number):
#             move = cell_number
#             run = False
#             insertLetter('X', move)
#             update_display()
    
#     # Bind the click event to the labels for player move
#     for i in range(3):
#         for j in range(3):
#             labels[i][j].bind("<Button-1>", lambda event, row=i, col=j: on_click_player(row, col))
    
#     # Wait until a valid move is made by the player
#     window.mainloop()
    
#     # Unbind the click event from the labels
#     for i in range(3):
#         for j in range(3):
#             labels[i][j].unbind("<Button-1>")
    
#     # Check if a valid move was made
#     if move > 0:
#         run = False
#     else:
#         print('Please select a valid position!')

            
def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
            
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
            
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        
    return move

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]
    

def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


##################
#displaying images

#custom images
image_path_x = "x.png"
image_path_o = "o.png"
image_path_blank = "blank.png"

# Define the desired width and height for the resized images
image_width = 100
image_height = 100

# Create the Tkinter window
window = tk.Tk()

def resize_image(image_path):
    image = Image.open(image_path)
    resized_image = image.resize((image_width, image_height), Image.ANTIALIAS)
    return ImageTk.PhotoImage(resized_image)

def update_display():
    for i in range(3):
        for j in range(3):
            if board[i*3+j+1] == 'X':
                labels[i][j].configure(image=image_x)
            elif board[i*3+j+1] == 'O':
                labels[i][j].configure(image=image_o)
            else:
                labels[i][j].configure(image=image_blank)


# Create ImageTk objects from the resized images
image_x = resize_image(image_path_x)
image_o = resize_image(image_path_o)
image_blank = resize_image(image_path_blank)

# Create labels to display the images
labels = [[tk.Label(window, image=image_blank) for _ in range(3)] for _ in range(3)]


# Place the labels in a grid layout
for i in range(3):
    for j in range(3):
        labels[i][j].grid(row=i, column=j)


# Bind the click event to the labels
for i in range(3):
    for j in range(3):
        labels[i][j].bind("<Button-1>", lambda event, row=i, col=j: on_click(row, col))


def main():
    print('Welcome to Tic Tac Toe!')
    
    

    printBoard(board)
    update_display()
    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print('Sorry, O\'s won this time!')
            break

        if not(isWinner(board, 'X')):
            move = compMove()
            if move == 0:
                print('Tie Game!')
            else:
                insertLetter('O', move)
                update_display()
                print('Computer placed an \'O\' in position', move , ':')
                printBoard(board)
        else:
            print('X\'s won this time! Good Job!')
            break

    if isBoardFull(board):
        print('Tie Game!')

while True:
    answer = input('Do you want to play again? (Y/N)')
    if answer.lower() == 'y' or answer.lower == 'yes':
        board = [' ' for x in range(10)]
        print('-----------------------------------')
        main()
    else:
        break

