print("\n"*100)
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

by: Arush                                                                                            
""")

input("Enter anything to start: ") #later chose mode here (1 player, 2 player)

print("\n"*100)

X = """ .----------------. 
| .--------------. |
| |  \033[31m____  ____\033[0m  | |
| | \033[31m|_  _||_  _|\033[0m | |
| | \033[31m  \\ \\  / /\033[0m   | |
| |  \033[31m  > `' <\033[0m    | |
| | \033[31m _/ /'`\\ \\_ \033[0m | |
| | \033[31m|____||____| \033[0m| |
| |              | |
| '--------------' |
 '----------------' """

O = """ .----------------. 
| .--------------. |
| | \033[34m    ____ \033[0m    | |
| | \033[34m  .'    `. \033[0m  | |
| | \033[34m /  .--.  \\ \033[0m | |
| | \033[34m | |    | | \033[0m | |
| | \033[34m \\  `--'  / \033[0m | |
| |  \033[34m `.____.'  \033[0m | |
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

GAME_OVER = r"""
                                                                                                             
                                     ____                        ,----..                                     
  ,----..      ,---,               ,'  , `.    ,---,.           /   /   \                  ,---,.,-.----.    
 /   /   \    '  .' \           ,-+-,.' _ |  ,'  .' |          /   .     :        ,---.  ,'  .' |\    /  \   
|   :     :  /  ;    '.      ,-+-. ;   , ||,---.'   |         .   /   ;.  \      /__./|,---.'   |;   :    \  
.   |  ;. / :  :       \    ,--.'|'   |  ;||   |   .'        .   ;   /  ` ; ,---.;  ; ||   |   .'|   | .\ :  
.   ; /--`  :  |   /\   \  |   |  ,', |  '::   :  |-,        ;   |  ; \ ; |/___/ \  | |:   :  |-,.   : |: |  
;   | ;  __ |  :  ' ;.   : |   | /  | |  ||:   |  ;/|        |   :  | ; | '\   ;  \ ' |:   |  ;/||   |  \ :  
|   : |.' .'|  |  ;/  \   \'   | :  | :  |,|   :   .'        .   |  ' ' ' : \   \  \: ||   :   .'|   : .  /  
.   | '_.' :'  :  | \  \ ,';   . |  ; |--' |   |  |-,        '   ;  \; /  |  ;   \  ' .|   |  |-,;   | |  \  
'   ; : \  ||  |  '  '--'  |   : |  | ,    '   :  ;/|         \   \  ',  /    \   \   ''   :  ;/||   | ;\  \ 
'   | '/  .'|  :  :        |   : '  |/     |   |    \          ;   :    /      \   `  ;|   |    \:   ' | \.' 
|   :    /  |  | ,'        ;   | |`-'      |   :   .'           \   \ .'        :   \ ||   :   .':   : :-'   
 \   \ .'   `--''          |   ;/          |   | ,'              `---`           '---" |   | ,'  |   |.'     
  `---`                    '---'           `----'                                      `----'    `---'       
                                                                                                             
"""

X_WIN = """\033[31m
 /$$   /$$       /$$      /$$ /$$$$$$ /$$   /$$  /$$$$$$ 
| $$  / $$      | $$  /$ | $$|_  $$_/| $$$ | $$ /$$__  $$
|  $$/ $$/      | $$ /$$$| $$  | $$  | $$$$| $$| $$  \\__/
 \\  $$$$/       | $$/$$ $$ $$  | $$  | $$ $$ $$|  $$$$$$ 
  >$$  $$       | $$$$_  $$$$  | $$  | $$  $$$$ \\____  $$
 /$$/\\  $$      | $$$/ \\  $$$  | $$  | $$\\  $$$ /$$  \\ $$
| $$  \\ $$      | $$/   \\  $$ /$$$$$$| $$ \\  $$|  $$$$$$/
|__/  |__/      |__/     \\__/|______/|__/  \\__/ \\______/ 
\033[0m                                                                                                                 
                                                         
"""

O_WIN = """\033[34m
  /$$$$$$        /$$      /$$ /$$$$$$ /$$   /$$  /$$$$$$ 
 /$$__  $$      | $$  /$ | $$|_  $$_/| $$$ | $$ /$$__  $$
| $$  \\ $$      | $$ /$$$| $$  | $$  | $$$$| $$| $$  \\__/
| $$  | $$      | $$/$$ $$ $$  | $$  | $$ $$ $$|  $$$$$$ 
| $$  | $$      | $$$$_  $$$$  | $$  | $$  $$$$ \\____  $$
| $$  | $$      | $$$/ \\  $$$  | $$  | $$\\  $$$ /$$  \\ $$
|  $$$$$$/      | $$/   \\  $$ /$$$$$$| $$ \\  $$|  $$$$$$/
 \\______/       |__/     \\__/|______/|__/  \\__/ \\______/ 
\033[0m
                                                          
"""

DRAW = """
 /$$$$$$$$ /$$$$$$ /$$$$$$$$ /$$
|__  $$__/|_  $$_/| $$_____/| $$
   | $$     | $$  | $$      | $$
   | $$     | $$  | $$$$$   | $$
   | $$     | $$  | $$__/   |__/
   | $$     | $$  | $$          
   | $$    /$$$$$$| $$$$$$$$ /$$
   |__/   |______/|________/|__/
                                                               
                                
"""

class Board:
    def __init__(self,X,O,B) -> None:
        self.X = X
        self.O = O
        self.B = B
        # 0 = blank, 1 = X, 2 = 0
        self.board = [[0,0,0],[0,0,0],[0,0,0]]
    
    #places piece on the board
    def is_valid_move(self,loc):
        if loc < 1 or loc > 9:
            return False, "Must be between 1 to 9"
        if self.board[(loc-1)//3][(loc-1)%3] == 0:
            return True, ""
        return False, "Cell already occupied"

    def check_win(self):
        #check rows:
        for row in self.board:
            if row[0] == row[1] == row[2] and row[0] != 0:
                return True, row[0]
        
        #check columns:
        for i in range(len(self.board[0])):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] != 0:
                return True, self.board[0][i]

        #check diagonals:
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != 0:
            return True, self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != 0:
            return True, self.board[0][2]

        for row in self.board:
            for cell in row:
                if cell == 0:
                    return False, None #Not a draw yet

        return True, None #Draw

    def place_piece(self,loc, X):
        self.board[(loc-1)//3][(loc-1)%3] = X

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
board.print_board()

for x in range(0,100):
    while True:
        loc = int(input("Enter location: "))
        valid, msg = board.is_valid_move(loc)
        if valid:
            break
        board.print_board()
        print(msg)

    board.place_piece(loc, 1 if x % 2 == 0 else 2)
    print("\n"*100)
    board.print_board()
    win, winner = board.check_win()
    if win:
        print("\n"*100)
        if winner == 1:
            print(X_WIN)
        else:
            print(O_WIN)
        break


if winner == None:
    print("\n"*100)
    print(DRAW)
print(GAME_OVER)
