import pytest

from board import Board
from enums import PieceColor
from piece.pieces import Rook
from position import Position


@pytest.mark.parametrize(
    ("starting_position", "expected_move_coords"),
    [
        (
            (0, 0),
            {
                (0, 1),
                (0, 2),
                (0, 3),
                (0, 4),
                (0, 5),
                (0, 6),
                (0, 7),
                (1, 0),
                (2, 0),
                (3, 0),
                (4, 0),
                (5, 0),
                (6, 0),
                (7, 0),
            },
        ),
        (
            (1, 1),
            {
                (1, 0),
                (1, 2),
                (1, 3),
                (1, 4),
                (1, 5),
                (1, 6),
                (1, 7),
                (0, 1),
                (2, 1),
                (3, 1),
                (4, 1),
                (5, 1),
                (6, 1),
                (7, 1),
            },
        ),
        (
            (4, 0),
            {
                (4, 1),
                (4, 2),
                (4, 3),
                (4, 4),
                (4, 5),
                (4, 6),
                (4, 7),
                (0, 0),
                (1, 0),
                (2, 0),
                (3, 0),
                (5, 0),
                (6, 0),
                (7, 0),
            },
        ),
        (
            (4, 4),
            {
                (4, 0),
                (4, 1),
                (4, 2),
                (4, 3),
                (4, 5),
                (4, 6),
                (4, 7),
                (0, 4),
                (1, 4),
                (2, 4),
                (3, 4),
                (5, 4),
                (6, 4),
                (7, 4),
            },
        ),
    ],
)
def test_rook_moves_on_empty_board(
    board: Board,
    starting_position: tuple[int, int],
    expected_move_coords: set[tuple[int, int]],
) -> None:
    # GIVEN a white rook somewhere on an empty board
    row, col = starting_position
    position = Position(row, col)
    rook = Rook(PieceColor.WHITE)
    board.set_piece(position, rook)

    # WHEN the possible moves for the rook are retrieved
    moves = rook.get_possible_moves(position, board)
    # THEN the possible moves of the rook are as expected
    assert {(pos.row, pos.col) for pos in moves} == expected_move_coords


def test_rook_can_not_move_to_friendly_squares(
    board: Board,
) -> None:
    # GIVEN a white rook in the top left of the board
    position = Position(0, 0)
    rook = Rook(PieceColor.WHITE)
    board.set_piece(position, rook)

    # AND another white rook on the diagonal that the
    # first rook can move to
    another_position = Position(0, 1)
    another_rook = Rook(PieceColor.WHITE)
    board.set_piece(another_position, another_rook)

    # WHEN the possible moves for the rook are retrieved
    moves = rook.get_possible_moves(position, board)
    # THEN the rook can only move down
    assert {(pos.row, pos.col) for pos in moves} == {
        (1, 0),
        (2, 0),
        (3, 0),
        (4, 0),
        (5, 0),
        (6, 0),
        (7, 0),
    }
