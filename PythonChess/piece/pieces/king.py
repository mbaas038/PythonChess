from typing import TYPE_CHECKING

from piece.piece import Piece
from piece.utils import get_straight_moves

if TYPE_CHECKING:
    from board import Board
    from position import Position


class King(Piece):
    def can_move(self, board: "Board", from_: "Position", to: "Position") -> bool:
        return to in self.get_possible_moves(from_, board)

    def get_possible_moves(
        self, current_position: "Position", board: "Board"
    ) -> list["Position"]:
        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
            (-1, -1),
            (-1, 1),
            (1, -1),
            (1, 1),
        ]
        return get_straight_moves(
            board, current_position, directions, self.color, stop_after=1
        )
