from typing import TYPE_CHECKING

from enums import PieceType
from mover.movers import QueenMover
from piece.piece import Piece

if TYPE_CHECKING:
    from enums import PieceColor


class Queen(Piece):
    def __init__(self, color: "PieceColor") -> None:
        super().__init__(color, PieceType.BISHOP, QueenMover(color))
