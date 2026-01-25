from typing import TYPE_CHECKING

from enums import PieceType
from mover.movers import KnightMover
from piece.piece import Piece

if TYPE_CHECKING:
    from enums import PieceColor


class Knight(Piece):
    def __init__(self, color: "PieceColor") -> None:
        super().__init__(color, PieceType.KNIGHT, KnightMover(color))
