import tkinter as tk

class Game:
    def __init__(self, master):
        self.master = master
        self.master.title("Tres en Raya")
        self.master.resizable(False, False)

        self.turn = "X"

        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.master, text="", font=("Helvetica", 40), width=2, height=1, command=lambda i=i, j=j: self.on_click(i, j))
                button.grid(row=i, column=j, sticky="news")
                row.append(button)
            self.buttons.append(row)

        restart_button = tk.Button(self.master, text="Reiniciar", font=("Helvetica", 20), width=6, height=1, command=self.restart)
        restart_button.grid(row=3, column=0, columnspan=3, sticky="news")

    def on_click(self, i, j):
        if self.buttons[i][j]["text"] == "":
            self.buttons[i][j]["text"] = self.turn
            if self.check_win():
                tk.messagebox.showinfo("Tres en Raya", f"Ganó el jugador {self.turn}!")
                self.restart()
            elif self.check_tie():
                tk.messagebox.showinfo("Tres en Raya", "Empate!")
                self.restart()
            else:
                self.turn = "O" if self.turn == "X" else "X"

    def check_win(self):
        for i in range(3):
            if self.buttons[i][0]["text"] == self.buttons[i][1]["text"] == self.buttons[i][2]["text"] != "":
                return True
            if self.buttons[0][i]["text"] == self.buttons[1][i]["text"] == self.buttons[2][i]["text"] != "":
                return True
        if self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"] != "":
            return True
        if self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0]["text"] != "":
            return True
        return False

    def check_tie(self):
        for i in range(3):
            for j in range(3):
                if self.buttons[i][j]["text"] == "":
                    return False
        return True

    def restart(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]["text"] = ""
        self.turn = "X"

if __name__ == "__main__":
    root = tk.Tk()
    game = Game(root)
    root.mainloop()
