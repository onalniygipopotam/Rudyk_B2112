import tkinter as tk
import random

class PyatnashkiGame:
    def __init__(self, root):
        self.root = root
        self.root.title("П'ятнашки")
        self.size = 4
        self.tiles = list(range(1, self.size**2)) + [None]
        random.shuffle(self.tiles)
        self.buttons = []
        self.empty_tile_index = self.tiles.index(None)
        self.create_widgets()
        self.draw_board()

    def create_widgets(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack()

    def draw_board(self):
        for button in self.buttons:
            button.destroy()
        self.buttons = []
        for i in range(self.size):
            for j in range(self.size):
                tile_index = i * self.size + j
                tile_value = self.tiles[tile_index]
                if tile_value is not None:
                    button = tk.Button(
                        self.frame,
                        text=str(tile_value),
                        font=("Arial", 18),
                        width=4,
                        height=2,
                        command=lambda index=tile_index: self.move_tile(index)
                    )
                else:
                    button = tk.Label(self.frame, width=4, height=2)
                button.grid(row=i, column=j, padx=2, pady=2)
                self.buttons.append(button)

    def move_tile(self, tile_index):
        if self.can_move(tile_index):
            self.tiles[self.empty_tile_index], self.tiles[tile_index] = (
                self.tiles[tile_index],
                self.tiles[self.empty_tile_index],
            )
            self.empty_tile_index = tile_index
            self.draw_board()
            if self.is_solved():
                self.show_win_message()

    def can_move(self, tile_index):
        row1, col1 = divmod(self.empty_tile_index, self.size)
        row2, col2 = divmod(tile_index, self.size)
        return abs(row1 - row2) + abs(col1 - col2) == 1

    def is_solved(self):
        return self.tiles[:-1] == list(range(1, self.size**2))

    def show_win_message(self):
        win_label = tk.Label(self.root, text="Ви виграли!", font=("Arial", 18), fg="green")
        win_label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    game = PyatnashkiGame(root)
    root.mainloop()
