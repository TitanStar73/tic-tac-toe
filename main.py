print(r"""
 ________  __                  ________                          ________                   
|        \|  \                |        \                        |        \                  
 \$$$$$$$$ \$$  _______        \$$$$$$$$______    _______        \$$$$$$$$______    ______  
   | $$   |  \ /       \         | $$  |      \  /       \         | $$  /      \  /      \ 
   | $$   | $$|  $$$$$$$         | $$   \$$$$$$\|  $$$$$$$         | $$ |  $$$$$$\|  $$$$$$\
   | $$   | $$| $$               | $$  /      $$| $$               | $$ | $$  | $$| $$    $$
   | $$   | $$| $$_____          | $$ |  $$$$$$$| $$_____          | $$ | $$__/ $$| $$$$$$$$
   | $$   | $$ \$$     \         | $$  \$$    $$ \$$     \         | $$  \$$    $$ \$$     \
    \$$    \$$  \$$$$$$$          \$$   \$$$$$$$  \$$$$$$$          \$$   \$$$$$$   \$$$$$$$                                                                                         
                                                                                            
""")

input("Enter anything to start: ") #later chose mode here (1 player, 2 player)

print("\n"*100)

X = r""" .----------------. 
| .--------------. |
| |  ____  ____  | |
| | |_  _||_  _| | |
| |   \ \  / /   | |
| |    > `' <    | |
| |  _/ /'`\ \_  | |
| | |____||____| | |
| |              | |
| '--------------' |
 '----------------' """

O = r""" .----------------. 
| .--------------. |
| |     ____     | |
| |   .'    `.   | |
| |  /  .--.  \  | |
| |  | |    | |  | |
| |  \  `--'  /  | |
| |   `.____.'   | |
| |              | |
| '--------------' |
 '----------------' """

B = r""" .----------------. 
| .--------------. |
| |              | |
| |              | |
| |              | |
| |      L       | |
| |              | |
| |              | |
| |              | |
| '--------------' |
 '----------------' """

class Board:
    def __init__(self,X,O,B) -> None:
        self.X = X
        self.O = O
        self.B = B
        # 0 = blank, 1 = X, 2 = 0
        self.board = [[0,0,0],[0,0,0],[0,0,0]]
    
    #places piece on the board
    def place_piece(self,loc, X):
        if loc == 1:
            self.board[0][0] = X
        elif loc == 2:
            self.board[0][1] = X
        elif loc == 3:
            self.board[0][2] = X
        elif loc == 4:
            self.board[1][0] = X
        elif loc == 5:
            self.board[1][1] = X
        elif loc == 6:
            self.board[1][2] = X
        elif loc == 7:
            self.board[2][0] = X
        elif loc == 8:
            self.board[2][1] = X
        elif loc == 9:
            self.board[2][2] = X

    def print_board_raw(self):
        for row in self.board:
            print(row)
    
    def print_board(self):
        conversion = {
            0: self.B,
            1: self.X,
            2: self.O
        }
        temp_board = [[conversion[cell] for cell in row] for row in self.board]
        for x,row in enumerate(temp_board):
            for i in range(len(self.B.split("\n"))):
                for y,cell in enumerate(row):
                    temp2 = cell.split("\n")[i]
                    if 'L' in temp2:
                        for char in temp2:
                            if char == 'L':
                                print(x*3 + y + 1, end="")
                            else:
                                print(char, end="")
                    else:
                        print(temp2, end="")
                    
                    print(" ", end="")

                print("")
            print("-"*(len(self.B.split("\n")[0])*3 + 2))

board = Board(X,O,B)

for x in range(0,9):
    board.print_board()
    loc = int(input("Enter location: "))
    board.place_piece(loc, 1 if x % 2 == 0 else 2)
    print("\n"*100)
