from typing import TYPE_CHECKING

from enums import PieceType
from mover.movers import BishopMover
from piece.piece import Piece

if TYPE_CHECKING:
    from enums import PieceColor


class Bishop(Piece):
    def __init__(self, color: "PieceColor") -> None:
        super().__init__(color, PieceType.BISHOP, BishopMover(color))
