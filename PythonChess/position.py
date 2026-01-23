

class Position:

    def __init__(self, row: int, col: int) -> None:
        self.row = row
        self.col = col

    def __repr__(self) -> str:
        return f"<Position ({self.row}, {self.col})>"

    def __eq__(self, other: "Position") -> bool:
        return self.row == other.row and self.col == other.col

    @staticmethod
    def is_valid(row: int, col: int) -> bool:
        return 0 <= row < 8 and 0 <= col < 8

