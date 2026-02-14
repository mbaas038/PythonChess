from enums import PieceColor
from piece.piece import Piece
from position import Position


class Square:
    def __init__(self, position: Position, piece: Piece | None = None) -> None:
        self.position = position
        self.piece = piece

    def __str__(self) -> str:
        if self.is_empty():
            return f"{self.position}: Empty"
        return f"{self.position}: {self.piece}"

    def set_piece(self, piece: Piece) -> None:
        self.piece = piece

    def remove_piece(self) -> None:
        self.piece = None

    def is_empty(self) -> bool:
        return self.piece is None

    def has_enemy_piece(self, color: PieceColor) -> bool:
        return not self.is_empty() and self.piece.color != color

    def has_friendly_piece(self, color: PieceColor) -> bool:
        return not self.is_empty() and self.piece.color == color
