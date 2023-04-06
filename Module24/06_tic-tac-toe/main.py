import random


class Cell:
    busy = False
    contain = ' '

    def __init__(self, number):
        self.number = number


class Board:
    def __init__(self):
        self.cells = tuple(Cell(number) for number in range(0, 9))
        self.show_current_board()

    def show_current_board(self):
        print(f'{" " * 3}|{" " * 3}|{" " * 3}')
        print(f' {self.cells[0].contain} | {self.cells[1].contain} | {self.cells[2].contain} ')
        print(f'{"—" * 11}')
        print(f' {self.cells[3].contain} | {self.cells[4].contain} | {self.cells[5].contain} ')
        print(f'{"—" * 11}')
        print(f' {self.cells[6].contain} | {self.cells[7].contain} | {self.cells[8].contain} ')
        print(f'{" " * 3}|{" " * 3}|{" " * 3}')
        print()
        print()


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def move(self, board):
        free_numbers = tuple(cell.number for cell in board.cells if not cell.busy)
        if len(free_numbers):
            index_cell = -1
            while index_cell not in free_numbers:
                index_cell = random.randint(free_numbers[0], free_numbers[- 1])
            board.cells[index_cell].busy = True
            board.cells[index_cell].contain = self.symbol


winning_combinations = ({0, 1, 2}, {3, 4, 5}, {6, 7, 8}, {0, 3, 6}, {1, 4, 7}, {2, 5, 8}, {0, 4, 8}, {2, 4, 6})


def check_uniqueness_players(player_1, player_2):
    if player_1.name == player_2.name:
        raise ValueError('Имена игроков должны быть уникальными!')
    if player_1.symbol == player_2.symbol:
        raise ValueError('Символы игроков должны быть уникальными!')


def check_winner(board, player):
    busy_numbers_by_current_symbol = {cell.number for cell in tuple(filter(
        lambda cell: cell.busy and cell.contain == player.symbol, board.cells))}
    no_difference = tuple(bool(combination - busy_numbers_by_current_symbol)
                          for combination in winning_combinations).count(False)
    if no_difference:
        print(f'Игрок {player.name} победил! Игра окончена.')
        return True
    return False


def round(board, player):
    player.move(board)
    board.show_current_board()
    return check_winner(board, player)


def play(board, player_1, player_2):
    check_uniqueness_players(player_1, player_2)
    while not all(tuple(cell.busy for cell in board.cells)):
        if round(board, player_1):
            break
        if round(board, player_2):
            break
    else:
        print(f'Ничья!')


player_1 = Player('Виктория', 'x')
player_2 = Player('Игорь', '0')
board = Board()

play(board, player_1, player_2)

