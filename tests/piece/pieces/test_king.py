import pytest

from board import Board
from enums import PieceColor
from piece.pieces import Pawn, King
from position import Position


@pytest.mark.parametrize(
    ("starting_position", "expected_move_coords"),
    [
        (
            (0, 0),
            {
                (0, 1),
                (1, 1),
                (1, 0),
            },
        ),
        (
            (4, 4),
            {
                (4, 3),
                (4, 5),
                (3, 4),
                (5, 4),
                (3, 3),
                (5, 5),
                (5, 3),
                (3, 5),
            },
        ),
    ],
)
def test_king_moves_on_empty_board(
    board: Board,
    starting_position: tuple[int, int],
    expected_move_coords: set[tuple[int, int]],
) -> None:
    # GIVEN a white king somewhere on an empty board
    row, col = starting_position
    position = Position(row, col)
    king = King(PieceColor.WHITE)
    board.set_piece(position, king)

    # WHEN the possible moves for the king are retrieved
    moves = king.get_possible_moves(position, board)
    # THEN the possible moves of the king are as expected
    assert {(pos.row, pos.col) for pos in moves} == expected_move_coords


def test_king_can_not_move_to_friendly_squares(
    board: Board,
) -> None:
    # GIVEN a white king in the top left of the board
    position = Position(0, 0)
    king = King(PieceColor.WHITE)
    board.set_piece(position, king)

    # AND two white pawns on the diagonal and row that
    # the king can move to
    board.set_piece(Position(1, 1), Pawn(PieceColor.WHITE))
    board.set_piece(Position(0, 1), Pawn(PieceColor.WHITE))

    # WHEN the possible moves for the king are retrieved
    moves = king.get_possible_moves(position, board)
    # THEN the king can only move down
    assert {(pos.row, pos.col) for pos in moves} == {
        (1, 0),
    }
