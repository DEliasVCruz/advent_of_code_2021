import re
import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="part_2.log",
    filemode="w",
    format="%(name)s - %(levelname)s - %(message)s",
)


class Board:

    @classmethod
    def create_columns(cls, board_raw: list) -> list:
        board: list = []

        for row in board_raw:
            board.append([])

        for row in board_raw:
            for number, element in enumerate(row):
                board[number].append(element)

        logging.debug(f"The board columns are {board}")
        return board

    @classmethod
    def empty_board(cls):
        return cls([])

    def __init__(self, board: list, number=None) -> None:

        self.rows: list = board
        logging.debug(f"The board rows are {self.rows}")
        self.columns: list = Board.create_columns(board)

        if number is not None:
            self.number: int = number

        self.latest_row: int = 0
        self.latest_col: int = 0
        logging.info(f"Successfully created board object number {number}")

    @property
    def flatten(self):
        self.__flatten = [element for row in self.rows for element in row]
        return self.__flatten

    def has_number(self, number: int) -> bool:
        for row_number, row in enumerate(self.rows):
            if number in row:
                col_number = row.index(number)
                self.latest_row = row_number
                self.latest_col = col_number
                return True
        return False

    def mark_number(self):
        self.rows[self.latest_row][self.latest_col] = -1
        self.columns[self.latest_col][self.latest_row] = -1

    def has_winning_column(self) -> bool:
        for column in self.columns:
            if sum(column) == -5:
                return True
        return False

    def has_winning_row(self) -> bool:
        for row in self.rows:
            if sum(row) == -5:
                return True
        return False

    def is_winner_board(self) -> bool:
        if self.has_winning_column() or self.has_winning_row():
            return True
        return False

    def total_not_matched(self) -> int:
        not_matched: list = []
        for casilla in self.flatten:
            if casilla >= 0:
                not_matched.append(casilla)
        return sum(not_matched)


def create_boards(raw_data: list) -> dict:

    logging.info("Initializing boards creation variables")

    boards: dict = {}
    board_number: int = 1
    board: list = []
    row: int = 0

    logging.info("Finished boards variables creation")

    for index, line in enumerate(raw_data[2:]):
        if index < row + 5:
            line = re.sub(r"^[\s]", "", line)
            line = list(map(int, re.split(r"[\s]+", line)))
            board.append(line)
        else:
            board_name: str = f"board_{board_number}"
            logging.debug(f"Board name is {board_name}")
            boards[board_name] = Board(board, board_number)
            board = []
            board_number += 1
            row += 6

    logging.info(f"Successfully created {board_number - 1} boards")

    return boards


def check_board(board, number: int):
    if board.has_number(number):
        board.mark_number()


if __name__ == "__main__":

    with open("./input.txt", "r") as f:
        raw_data: list = f.read().splitlines()
        logging.info("Created raw data as a list")

    numbers: list = list(map(int, raw_data[0].split(",")))
    logging.info(f"Created list of numbers as:\n {numbers}")

    boards = create_boards(raw_data)
    logging.info("Created dictionary of boards")
    logging.debug(f"The number of boards is {len(boards)}")

    last_number = 0
    last_winning_board = Board.empty_board()
    winning_boards: list = []
    for number in numbers:
        for board in boards.values():
            if board.number not in winning_boards:
                check_board(board, number)
                if board.is_winner_board():
                    winning_boards.append(board.number)
                    last_winning_board = board
                    last_number = number
                if len(winning_boards) == len(boards):
                    logging.info(f"The winner board is board number {last_winning_board.number}")
                    logging.info(f"The board is {last_winning_board.rows}")
                    logging.info(f"The last number is number {last_number}")
                    break
        if last_number != 0:
            break

    logging.info(f"The winner board is board number {last_winning_board.number}")
    logging.info(f"The board is {last_winning_board.rows}")
    logging.debug(f"The flatten board is {last_winning_board.flatten}")
    not_matched = last_winning_board.total_not_matched()
    logging.debug(f"The total not matched is {not_matched}")
    logging.info(f"The last number is number {last_number}")
    final_score = not_matched * last_number

    print(final_score)
