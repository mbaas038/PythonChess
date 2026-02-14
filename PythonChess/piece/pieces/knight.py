from typing import TYPE_CHECKING

from piece.piece import Piece
from position import Position

if TYPE_CHECKING:
    from board import Board


class Knight(Piece):
    def can_move(self, board: "Board", from_: Position, to: Position) -> bool:
        return to in self.get_possible_moves(from_, board)

    def get_possible_moves(
        self, current_position: Position, board: "Board"
    ) -> list[Position]:
        moves = []
        current_row, current_col = current_position.row, current_position.col
        possible_moves = (
            (-2, -1),
            (-2, 1),
            (-1, -2),
            (-1, 2),
            (1, -2),
            (1, 2),
            (2, -1),
            (2, 1),
        )
        for row, col in possible_moves:
            new_row, new_col = current_row + row, current_col + col
            if Position.is_valid(new_row, new_col):
                position = Position(new_row, new_col)
                square = board.get_square(position)
                if square.is_empty() or square.has_enemy_piece(self.color):
                    moves.append(position)
        return moves
