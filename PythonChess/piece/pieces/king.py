from typing import TYPE_CHECKING

from enums import PieceColor
from piece.piece import Piece
from piece.pieces.rook import Rook
from piece.utils import get_straight_moves
from position import Position

if TYPE_CHECKING:
    from board import Board


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
        moves = get_straight_moves(
            board, current_position, directions, self.color, stop_after=1
        )
        moves.extend(self._castle_moves(board, current_position))
        return moves

    def _castle_moves(self, board: "Board", position: "Position") -> list["Position"]:
        if not self._in_starting_position(position):
            return []

        moves = []
        row = position.row
        kingside_castle = Position(row, 6)
        if self._can_castle(board, position, kingside_castle):
            moves.append(kingside_castle)

        queenside_castle = Position(row, 2)
        if self._can_castle(board, position, queenside_castle):
            moves.append(queenside_castle)

        return moves

    def _can_castle(self, board: "Board", from_: "Position", to: "Position") -> bool:
        if not self._in_starting_position(from_):
            return False

        if to.col not in {2, 6}:
            return False

        rook_position = Position(from_.row, 7 if to.col == 6 else 0)
        rook = board.get_piece(rook_position)
        if not isinstance(rook, Rook) or self.color != rook.color or rook.has_moved:
            return False

        start_col = min(from_.col, rook_position.col) + 1
        end_col = max(from_.col, rook_position.col)
        for col in range(start_col, end_col):
            if not board.get_square(Position(from_.row, col)).is_empty():
                return False

        return True

    def _in_starting_position(self, position: "Position") -> bool:
        row, col = position.row, position.col
        return (
            not self.has_moved
            and col == 4
            and (
                (self.color == PieceColor.WHITE and row == 7)
                or (self.color == PieceColor.BLACK and row == 0)
            )
        )
