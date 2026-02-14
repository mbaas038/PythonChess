from board import Board
from enums import PieceColor
from position import Position


def get_straight_moves(
    board: Board,
    position: Position,
    directions: list[tuple[int, int]],
    color: PieceColor,
    stop_after: int | None = None,
) -> list[Position]:
    moves = []
    row, col = position.row, position.col
    for direction in directions:
        next_row, next_col = row + direction[0], col + direction[1]
        steps = 0
        while True:
            if stop_after is not None and steps >= stop_after:
                break
            if not Position.is_valid(next_row, next_col):
                break

            position = Position(next_row, next_col)
            square = board.get_square(position)
            if square.has_friendly_piece(color):
                break

            moves.append(position)
            if square.has_enemy_piece(color):
                break

            next_row, next_col = next_row + direction[0], next_col + direction[1]
            steps += 1

    return moves
