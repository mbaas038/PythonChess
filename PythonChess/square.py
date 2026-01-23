from enums import PieceColor
from pieces import Piece
from position import Position


class Square:
    def __init__(self, position: Position, piece: Piece | None = None) -> None:
        self.position = position
        self.piece = piece

    def is_empty(self) -> bool:
        return self.piece is None

    def has_enemy_piece(self, color: PieceColor) -> bool:
        return not self.is_empty() and self.piece.color != color

    def has_friendly_piece(self, color: PieceColor) -> bool:
        return not self.is_empty() and self.piece.color == color