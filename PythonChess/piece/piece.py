from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
from enums import PieceColor
from position import Position

if TYPE_CHECKING:
    from board import Board


class Piece(ABC):
    def __init__(self, color: "PieceColor") -> None:
        self.color = color
        self.has_moved = False

    @abstractmethod
    def can_move(self, board: "Board", from_: Position, to: Position) -> bool: ...

    @abstractmethod
    def get_possible_moves(
        self, current_position: Position, board: "Board"
    ) -> list[Position]: ...
