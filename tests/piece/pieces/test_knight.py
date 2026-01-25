import pytest

from board import Board
from enums import PieceColor
from piece.pieces import Knight
from position import Position


@pytest.mark.parametrize(
    ("starting_position", "expected_move_coords"),
    [
        ((0, 0), {(1, 2), (2, 1)}),
        ((0, 1), {(2, 0), (2, 2), (1, 3)}),
        ((4, 0), {(2, 1), (6, 1), (3, 2), (5, 2)}),
        ((4, 1), {(6, 2), (2, 2), (2, 0), (3, 3), (6, 0), (5, 3)}),
        ((4, 4), {(5, 6), (5, 2), (6, 3), (6, 5), (3, 6), (3, 2), (2, 3), (2, 5)}),
    ],
)
def test_knight_moves_on_empty_board(
    board: Board,
    starting_position: tuple[int, int],
    expected_move_coords: set[tuple[int, int]],
) -> None:
    # GIVEN a white knight somewhere on an empty board
    row, col = starting_position
    position = Position(row, col)
    knight = Knight(PieceColor.WHITE)
    board.set_piece(position, knight)

    # WHEN the possible moves for the knight are retrieved
    moves = knight.get_possible_moves(position, board)
    # THEN the possible moves of the knight are as expected
    assert {(pos.row, pos.col) for pos in moves} == expected_move_coords


def test_knight_can_not_move_to_friendly_squares(
    board: Board,
) -> None:
    # GIVEN a white knight in the middle of the board
    position = Position(4, 4)
    knight = Knight(PieceColor.WHITE)
    board.set_piece(position, knight)

    # AND another white knight in a position the first
    # knight can move to
    another_position = Position(5, 6)
    another_knight = Knight(PieceColor.WHITE)
    board.set_piece(another_position, another_knight)

    # WHEN the possible moves for the knight are retrieved
    moves = knight.get_possible_moves(position, board)
    # THEN the possible moves of the knight are as expected
    assert {(pos.row, pos.col) for pos in moves} == {
        (5, 2),
        (6, 3),
        (6, 5),
        (3, 6),
        (3, 2),
        (2, 3),
        (2, 5),
    }
