from typing import TYPE_CHECKING

from position import Position
from square import Square

if TYPE_CHECKING:
    from piece.pieces import Piece


class Board:
    SIZE = 8

    def __init__(self) -> None:
        self.squares = [
            [Square(Position(i, j), None) for j in range(self.SIZE)]
            for i in range(self.SIZE)
        ]

    def get_square(self, position: "Position") -> Square:
        return self.squares[position.row][position.col]

    def set_piece(self, position: "Position", piece: "Piece") -> None:
        self.get_square(position).piece = piece

    def get_piece(self, position: "Position") -> "Piece | None":
        return self.get_square(position).piece
