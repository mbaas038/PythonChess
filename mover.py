from typing import Protocol

from board import Board
from position import Position


class Mover(Protocol):

    def can_move(self, board: Board, from_: Position, to: Position) -> bool:
        ...

    def get_possible_moves(self, current_position: Position, board: Board) -> list[Position]:
        ...