from typing import Protocol, TYPE_CHECKING

from enums import PieceColor
from position import Position

if TYPE_CHECKING:
    from board import Board


class Mover(Protocol):
    color: PieceColor

    def can_move(self, board: "Board", from_: Position, to: Position) -> bool: ...

    def get_possible_moves(
        self, current_position: Position, board: "Board"
    ) -> list[Position]: ...
