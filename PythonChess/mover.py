from typing import Protocol, TYPE_CHECKING

from enums import PieceColor
from position import Position

if TYPE_CHECKING:
    from board import Board


WHITE_PAWN_START_ROW = 1
BLACK_PAWN_START_ROW = 6


class Mover(Protocol):
    color: PieceColor

    def can_move(self, board: "Board", from_: Position, to: Position) -> bool:
        ...

    def get_possible_moves(self, current_position: Position, board: "Board") -> list[Position]:
        ...


class PawnMover:

    def __init__(self, color: PieceColor) -> None:
        self.color = color

    def can_move(self, board: "Board", from_: Position, to: Position) -> bool:
        return to in self.get_possible_moves(from_, board)

    def get_possible_moves(self, current_position: Position, board: "Board") -> list[Position]:
        forward_moves = self._forward_moves(board, current_position)
        diagonal_moves = self._diagonal_moves(board, current_position)
        return forward_moves + diagonal_moves

    @property
    def direction(self) -> int:
        return 1 if self.color == PieceColor.WHITE else -1

    def _has_moved(self, current_row: int) -> bool:
        return (
            (self.color == PieceColor.WHITE and current_row != WHITE_PAWN_START_ROW)
            or
            (self.color == PieceColor.BLACK and current_row != BLACK_PAWN_START_ROW)
        )

    def _forward_moves(self, board: "Board", position: Position) -> list[Position]:
        forward_moves = []
        current_row, current_col = position.row, position.col

        single_step_row = current_row + self.direction
        if Position.is_valid(single_step_row, current_col):
            single_step_position = Position(single_step_row, current_col)
            if board.get_square(single_step_position).is_empty():
                forward_moves.append(single_step_position)
                if not self._has_moved(current_row):
                    second_step_position = Position(single_step_row + self.direction, current_col)
                    if board.get_square(second_step_position).is_empty():
                        forward_moves.append(second_step_position)

        return forward_moves

    def _diagonal_moves(self, board: "Board", position: Position) -> list[Position]:
        diagonal_moves = []
        current_row, current_col = position.row, position.col

        diagonal_row = current_row + self.direction
        for diagonal_col in (current_col - 1, current_col + 1):
            if Position.is_valid(diagonal_row, diagonal_col):
                diagonal_position = Position(diagonal_row, diagonal_col)
                if board.get_square(diagonal_position).has_enemy_piece(self.color):
                    diagonal_moves.append(diagonal_position)

        return diagonal_moves
