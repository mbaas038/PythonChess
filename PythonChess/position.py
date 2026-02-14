class Position:
    def __init__(self, row: int, col: int) -> None:
        if not Position.is_valid(row, col):
            raise ValueError("Invalid position")
        self.row = row
        self.col = col

    def __repr__(self) -> str:
        return f"<Position ({self.row}, {self.col})>"

    def __eq__(self, other: "Position") -> bool:
        return self.row == other.row and self.col == other.col

    def __str__(self) -> str:
        return self.to_chess_notation()

    def to_chess_notation(self) -> str:
        return f"{chr(ord('a') + self.col)}{8 - self.row}"

    @staticmethod
    def is_valid(row: int, col: int) -> bool:
        return 0 <= row < 8 and 0 <= col < 8
