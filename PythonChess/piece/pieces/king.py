from typing import TYPE_CHECKING

from enums import PieceType
from mover.movers import KingMover
from piece.piece import Piece

if TYPE_CHECKING:
    from enums import PieceColor


class King(Piece):
    def __init__(self, color: "PieceColor") -> None:
        super().__init__(color, PieceType.KING, KingMover(color))
