class Board:
    """Класс, который описывает игровое поле."""

    field_size = 3

    def __init__(self) -> list:
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    # Метод, который обрабатывает ходы игроков.
    def make_move(self, row, col, player):
        self.board[row][col] = player

    # Метод, который отрисовывает игровое поле.
    def display(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)
    # Метод, который определяет победу.
    def check_win(self, player) -> bool:
        for i in range(self.field_size):
            # Проверка по горизонталям и вертикалям
            if (all([self.board[i][j] == player for j in range(self.field_size)]) or
                    all([self.board[j][i] == player for j in range(self.field_size)])):
                return True
            if (all([self.board[i][i] == player for i in range(self.field_size)]) or
                    all([self.board[i][self.field_size - 1 - i]] == player for i in range(self.field_size))):
                return True
        return False

    # Метод, который определяет ничью.
    def is_board_full(self) -> bool:
        for i in range(self.field_size):
            for j in range(self.field_size):
                if self.board[i][j] == ' ':
                    return False
        return True

    # переопределяем метод __str__.
    def __str__(self) -> str:
        return (
            'Объект игрового поля размером '
            f'{self.field_size}x{self.field_size}'
        )
