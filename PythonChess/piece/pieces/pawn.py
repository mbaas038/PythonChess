from typing import TYPE_CHECKING

from enums import PieceType
from mover.movers import PawnMover
from piece.piece import Piece

if TYPE_CHECKING:
    from enums import PieceColor


class Pawn(Piece):
    def __init__(self, color: "PieceColor") -> None:
        super().__init__(color, PieceType.PAWN, PawnMover(color))
