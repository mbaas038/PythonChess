from typing import TYPE_CHECKING
from enums import PieceColor
from position import Position

if TYPE_CHECKING:
    from board import Board


class BishopMover:
    def __init__(self, color: PieceColor) -> None:
        self.color = color

    def can_move(self, board: "Board", from_: Position, to: Position) -> bool:
        return to in self.get_possible_moves(from_, board)

    def get_possible_moves(
        self, current_position: Position, board: "Board"
    ) -> list[Position]:
        moves = []
        row, col = current_position.row, current_position.col
        directions = ((-1, -1), (-1, 1), (1, -1), (1, 1))
        for direction in directions:
            next_row, next_col = row + direction[0], col + direction[1]
            while True:
                if not Position.is_valid(next_row, next_col):
                    break

                position = Position(next_row, next_col)
                square = board.get_square(position)
                if square.has_friendly_piece(self.color):
                    break

                moves.append(position)
                if square.has_enemy_piece(self.color):
                    break

                next_row, next_col = next_row + direction[0], next_col + direction[1]

        return moves
