import pytest

from board import Board
from enums import PieceColor
from piece.pieces import Bishop
from position import Position


@pytest.mark.parametrize(
    ("starting_position", "expected_move_coords"),
    [
        ((0, 0), {(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)}),
        (
            (1, 1),
            {(0, 0), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (2, 0), (0, 2)},
        ),
        (
            (4, 0),
            {
                (3, 1),
                (2, 2),
                (1, 3),
                (0, 4),
                (5, 1),
                (6, 2),
                (7, 3),
            },
        ),
        (
            (4, 4),
            {
                (0, 0),
                (1, 1),
                (2, 2),
                (3, 3),
                (5, 5),
                (6, 6),
                (7, 7),
                (7, 1),
                (6, 2),
                (5, 3),
                (3, 5),
                (2, 6),
                (1, 7),
            },
        ),
    ],
)
def test_bishop_moves_on_empty_board(
    board: Board,
    starting_position: tuple[int, int],
    expected_move_coords: set[tuple[int, int]],
) -> None:
    # GIVEN a white bishop somewhere on an empty board
    row, col = starting_position
    position = Position(row, col)
    bishop = Bishop(PieceColor.WHITE)
    board.set_piece(position, bishop)

    # WHEN the possible moves for the bishop are retrieved
    moves = bishop.get_possible_moves(position, board)
    # THEN the possible moves of the bishop are as expected
    assert {(pos.row, pos.col) for pos in moves} == expected_move_coords


def test_knight_can_not_move_to_friendly_squares(
    board: Board,
) -> None:
    # GIVEN a white bishop in the top left of the board
    position = Position(0, 0)
    bishop = Bishop(PieceColor.WHITE)
    board.set_piece(position, bishop)

    # AND another white bishop on the diagonal that the
    # first bishop can move to
    another_position = Position(1, 1)
    another_bishop = Bishop(PieceColor.WHITE)
    board.set_piece(another_position, another_bishop)

    # WHEN the possible moves for the bishop are retrieved
    moves = bishop.get_possible_moves(position, board)
    # THEN the bishop has no possible moves
    assert not moves
