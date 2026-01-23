from typing import TYPE_CHECKING
from enums import PieceType
from mover import PawnMover

if TYPE_CHECKING:
    from board import Board
    from enums import PieceColor, PieceType
    from mover import Mover
    from position import Position


class Piece:
    def __init__(self, color: "PieceColor", type_: "PieceType", mover: "Mover") -> None:
        self.color = color
        self.type = type_
        self.has_moved = False
        self.mover = mover

    def get_possible_moves(
        self, current_position: "Position", board: "Board"
    ) -> list["Position"]:
        return self.mover.get_possible_moves(current_position, board)

    def is_valid_move(self, from_: "Position", to: "Position", board: "Board") -> bool:
        return self.mover.can_move(board, from_, to)


class Pawn(Piece):
    def __init__(self, color: "PieceColor") -> None:
        super().__init__(color, PieceType.PAWN, PawnMover(color))
