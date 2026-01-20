import enum


class PieceColor(enum.Enum):
    WHITE = enum.auto()
    BLACK = enum.auto()


class PieceType(enum.Enum):
    KING = ("K", 1)
    QUEEN = ("Q", 9)
    ROOK = ("R", 5)
    BISHOP = ("B", 3)
    KNIGHT = ("N", 3)
    PAWN = ("P", 1)

    def get_symbol(self) -> str:
        return self.value[0]

    def get_value(self) -> int:
        return self.value[1]
