import pytest

from board import Board
from enums import PieceColor
from piece.pieces import Queen, Pawn
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
                (1, 1),
                (2, 2),
                (3, 3),
                (4, 4),
                (5, 5),
                (6, 6),
                (7, 7),
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
def test_queen_moves_on_empty_board(
    board: Board,
    starting_position: tuple[int, int],
    expected_move_coords: set[tuple[int, int]],
) -> None:
    # GIVEN a white queen somewhere on an empty board
    row, col = starting_position
    position = Position(row, col)
    queen = Queen(PieceColor.WHITE)
    board.set_piece(position, queen)

    # WHEN the possible moves for the queen are retrieved
    moves = queen.get_possible_moves(position, board)
    # THEN the possible moves of the queen are as expected
    assert {(pos.row, pos.col) for pos in moves} == expected_move_coords


def test_rook_can_not_move_to_friendly_squares(
    board: Board,
) -> None:
    # GIVEN a white queen in the top left of the board
    position = Position(0, 0)
    queen = Queen(PieceColor.WHITE)
    board.set_piece(position, queen)

    # AND two white pawns on the diagonal and row that
    # the queen can move to
    board.set_piece(Position(1, 1), Pawn(PieceColor.WHITE))
    board.set_piece(Position(0, 1), Pawn(PieceColor.WHITE))

    # WHEN the possible moves for the queen are retrieved
    moves = queen.get_possible_moves(position, board)
    # THEN the queen can only move down
    assert {(pos.row, pos.col) for pos in moves} == {
        (1, 0),
        (2, 0),
        (3, 0),
        (4, 0),
        (5, 0),
        (6, 0),
        (7, 0),
    }
