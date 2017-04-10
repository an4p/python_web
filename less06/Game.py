class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def start_game(self):
        while True:
            if not self.player1.is_free_cell():
                print("Draw")
                break
            self.player1.step()
            if self.player1.is_winner():
                print("Player1 is winner")
                break
            if not self.player2.is_free_cell():
                print("Draw")
                break
            self.player2.step()
            if self.player2.is_winner():
                print("Player2 is winner")
                break

class Player:
    def __init__(self,field, mark):
        self.field = field
        self.mark = mark

    def is_free_cell(self):
        return self.field.is_free_cell()

    def step(self):
        pass

    def is_winner(self):
        return self.field.is_line(self.mark)

class Human(Player):
    def __init__(self, field, mark):
        Player.__init__(self, field, mark)

    def step(self):
        x = int(input("x: \n")) #validation is needed
        y = int(input("y: \n"))
        #validation: is cell free?
        self.field.set_mark(x, y, self.mark)
        self.field.show()

class Computer(Player):
    def __init__(self, field, mark):
        Player.__init__(self, field, mark)

    def step(self):
        x, y = self.field.find_free_cell()
        self.field.set_mark(x, y, self.mark)
        self.field.show()

class Field:
    def __init__(self):
        self.cells = []
        for i in range(0,3):
            temp = []
            for j in range(0,3):
                temp.append(Cell())
            self.cells.append(temp)

    def is_free_cell(self):
        for i in range(0,3):
             for j in range(0,3):
                 if self.cells[i][j].status == "P":
                     return True
        return False

    def is_line(self, mark):
        for i in range(0,3):
            if self.cells[i][0].status == mark and self.cells[i][1].status == mark \
                and self.cells[i][2].status == mark:
                return True
        for j in range(0,3):
            if self.cells[0][j].status == mark and self.cells[1][j].status == mark \
                and self.cells[2][j].status == mark:
                return True
        if self.cells[0][0].status == mark and self.cells[1][1].status == mark \
            and self.cells[2][2].status == mark:
            return True
        if self.cells[0][2].status == mark and self.cells[1][1].status == mark \
            and self.cells[2][0].status == mark:
            return True
        return False

    def set_mark(self,x, y, mark):
        self.cells[x][y].status = mark

    def show(self):
        for i in range(0,3):
            for j in range(0,3):
                print(self.cells[i][j].status, end=" ")
            print()
        print("---------------")

    def find_free_cell(self):
        for i in range(0,3):
            for j in range(0,3):
                if self.cells[i][j].status == "P":
                    return (i, j)



class Cell:
    def __init__(self):
        self.status = "P"


def main():
    field = Field()
    player1 = Human(field, "X")
    player2 = Computer(field, "O")
    game = Game(player1, player2)
    game.start_game()

main()

