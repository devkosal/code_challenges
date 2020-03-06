from pprint import pprint
# Connect Four
"""
Today's CS Practical - Connect 4

1/ BOARD

User input grid size, start with a 4*4

2/ DROP PIECE
Place piece in board, alternating between players 1 and 2.
Pieces will stack on top of each other so make sure you build from the bottom up.

3/ WINNING MOVE
The game should work for two players and tell you when you have won, be it horizontal vertical or diagonal (4 in a row).

4/ MOVE IS VALID
Check for excepts: "Illegal move", "This column is full.  Try another one!", "The board is full!"

5/ 6x6 BOARD
Still only win by getting 4 in a row (vertically, horizontally, diagonally)
"""



class ConnectFour:
    def __init__(self, N):
        assert N >= 4, "Grid size must be greater than or equal to 4."
        self.N = N
        self.board = [[0]*N for _ in range(N)]
        self.counts = [0 for _ in range(N)]
        self.player_dict = {1:1,-1:2}

    def update_board(self, player):
        player_move = -1
        valid_move = False
        while (player_move > self.N-1 or player_move < 0) and not valid_move:
            player_move = int(input("Please input a number between 1 and 6 to place a token on an open column: ")) - 1

            if 0 <= player_move <= self.N-1:
                if self.counts[player_move] >= self.N:
                    print("The selected column is full.")
                else:
                    valid_move = True

        row = self.N - self.counts[player_move] -1
        self.counts[player_move] += 1
        self.board[row][player_move] = player

    def check_for_four(self,arr):
        return any([abs(sum(arr[i:i+4])) == 4 for i in range(self.N-3)])

    def has_won(self, player):
        # checking rows
        for x in self.board:
            if self.check_for_four(x):
                return True
        # checking columns
        for x in range(self.N):
            if self.check_for_four([self.board[i][x] for i in range(self.N)]):
                return True
        # diagonal
        if self.check_for_four([self.board[i][i] for i in range(self.N)]):
            return True
        # opposite diagonal
        elif self.check_for_four([self.board[i][-i-1] for i in range(self.N)]):
            return True
        return False

    def is_board_full(self):
        return all([True if c == self.N else False for c in self.counts])

    def play(self):
        player = 1
        while True:
            print("Current Board:\n")
            pprint(self.board)
            print(f"Player {self.player_dict[player]} is up")
            self.update_board(player)
            if self.has_won(player):
                pprint(self.board)
                print(f"Player {self.player_dict[player]} wins!")
                break
            elif self.is_board_full():
                pprint(self.board)
                print("The board is full! It's a tie!")
            player *= -1
        print("The game has ended.")

c = ConnectFour(6)
c.play()
