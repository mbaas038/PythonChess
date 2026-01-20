from typing import Literal
from pieces import Piece
from position import Position

Direction = Literal[-1, 1]


class Square:
    def __init__(self, position: Position, piece: Piece | None = None) -> None:
        self.position = position
        self.piece = piece


class Board:
    def __init__(self, size: int) -> None:
        self.squares = [
            [
                Square(Position(i, j), None)
                for j in range(size)
            ]
            for i in range(size)
        ]

    def set_piece(self, position: Position, piece: Piece) -> None:
        y, x = position
        self.squares[y][x].piece = piece

    def get_piece(self, position: Position) -> Piece | None:
        y, x = position
        return self.squares[y][x].piece