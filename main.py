from os import system

class Tictactoe:

    def __init__(self):
        self.grid = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        self.rows = ('A', 'B', 'C')
        self.alias = {'A': 0, 'B': 1, 'C': 2}
        self.used = []
        system('clear')
        self.playerone()

    def playerone(self):
        self.printGrid()
        coors = input('P1 coordinates: ')
        if coors not in self.used:
            if len(coors) == 2 and coors[0].isalpha() == True and coors[1].isdigit() == True:
                self.grid[self.alias[coors[0].upper()]][int(coors[1]) - 1] = 'X'
                self.used.append(coors)
        else:
            self.playerone()
        if self.check() == False:
            self.playertwo()
        else:
            print('Player 1 wins!')
            self.newGame()

    def playertwo(self):
        self.printGrid()
        coors = input('P2 coordinates: ')
        if coors not in self.used:
            if len(coors) == 2 and coors[0].isalpha() == True and coors[1].isdigit() == True:
                self.grid[self.alias[coors[0].upper()]][int(coors[1]) - 1] = 'O'
                self.used.append(coors)
        else:
            self.playertwo()
        if self.check() == False:
            self.playerone()
        else:
            print('Player 2 wins!')
            self.newGame()

    def check(self):
        for i in range(3):
            if self.grid[i].count('X') == 3 or self.grid[i].count('O') == 3:
                return True
            for j in range(3):
                if self.grid[0][i] == self.grid[1][i] == self.grid[2][i] != '-':
                    return True
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] != '-' or self.grid[0][2] == self.grid[1][1] == self.grid[2][0] != '-':
            return True
        draw = False
        for line in self.grid:
            if '-' in line:
                break
            else:
                draw = True
        if draw == True:
            print('Draw!')
            self.newGame()
        return False

    def newGame(self):
        self.printGrid()
        ans = input('Do you want to play again? [y/N]: ')
        if ans.lower() == 'y':
            game = Tictactoe()
        elif ans.lower() == 'n':
            exit()
        else:
            self.newGame()

    def printGrid(self):
        system('clear')
        print('  123')
        for i in range(3):
            print(f'{self.rows[i]} {"".join(self.grid[i])}')

game = Tictactoe()




