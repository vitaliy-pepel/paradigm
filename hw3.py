import tkinter as tk

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")

        self.current_player = 'X'
        self.board = [' ' for _ in range(9)]

        self.buttons = []
        for i in range(3):
            row_buttons = []
            for j in range(3):
                button = tk.Button(self.root, text='', font=('Arial', 20), width=5, height=2,
                                   command=lambda i=i, j=j: self.make_move(i, j))
                button.grid(row=i, column=j)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

    def make_move(self, i, j):
        index = i * 3 + j
        if self.board[index] == ' ':
            self.board[index] = self.current_player
            self.buttons[i][j].config(text=self.current_player)
            if self.is_winner(self.current_player):
                self.display_winner()
            elif self.is_draw():
                self.display_draw()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def is_winner(self, player):
        # Check rows, columns and diagonals
        for i in range(0, 9, 3):
            if all([self.board[i + j] == player for j in range(3)]):
                return True
        for i in range(3):
            if all([self.board[i + j] == player for j in range(0, 9, 3)]):
                return True
        if all([self.board[i] == player for i in range(0, 9, 4)]) or all([self.board[i] == player for i in range(2, 7, 2)]):
            return True
        return False

    def is_draw(self):
        return ' ' not in self.board

    def display_winner(self):
        winner_label = tk.Label(self.root, text=f'Player {self.current_player} wins!', font=('Arial', 16))
        winner_label.grid(row=3, columnspan=3)

    def display_draw(self):
        draw_label = tk.Label(self.root, text='It\'s a draw!', font=('Arial', 16))
        draw_label.grid(row=3, columnspan=3)

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()