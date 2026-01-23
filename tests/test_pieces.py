import pytest

from board import Board
from enums import PieceColor
from mover import WHITE_PAWN_START_ROW
from pieces import Pawn
from position import Position


@pytest.fixture(name="starting_position")
def _starting_position() -> Position:
    return Position(WHITE_PAWN_START_ROW, 4)


@pytest.fixture(name="non_starting_position")
def _non_starting_position() -> Position:
    return Position(WHITE_PAWN_START_ROW + 1, 4)


@pytest.fixture(name="white_pawn")
def _white_pawn() -> Pawn:
    return Pawn(PieceColor.WHITE)


@pytest.fixture(name="board_white_pawn_on_starting_row")
def _board_white_pawn_on_starting_row(white_pawn: Pawn, starting_position: Position) -> Board:
    board = Board()
    board.set_piece(starting_position, white_pawn)
    return board


@pytest.fixture(name="board_white_pawn_on_non_starting_row")
def _board_white_pawn_on_non_starting_row(white_pawn: Pawn, non_starting_position: Position) -> Board:
    board = Board()
    board.set_piece(non_starting_position, white_pawn)
    return board


def test_pawn_piece_forward_moves_from_starting_position(
    board_white_pawn_on_starting_row: Board,
    white_pawn: Pawn,
    starting_position: Position
) -> None:
    # GIVEN a board with a white pawn in its starting position

    # WHEN the possible moves for the pawn are retrieved
    moves = white_pawn.get_possible_moves(starting_position, board_white_pawn_on_starting_row)

    # THEN the pawn can move forward one step or two steps
    starting_row, starting_col = starting_position.row, starting_position.col
    assert moves == [Position(starting_row + 1, starting_col), Position(starting_row + 2, starting_col)]


def test_enemy_piece_in_front_blocks_forward_movement(
    board_white_pawn_on_starting_row: Board,
    white_pawn: Pawn,
    starting_position: Position
) -> None:
    # GIVEN a board with a white pawn in its starting position
    # AND a black pawn blocking forward movement
    board_white_pawn_on_starting_row.set_piece(Position(starting_position.row + 1, starting_position.col), Pawn(PieceColor.BLACK))

    # WHEN the possible moves for the pawn are retrieved
    moves = white_pawn.get_possible_moves(starting_position, board_white_pawn_on_starting_row)

    # THEN the pawn can move forward one step or two steps
    starting_row, starting_col = starting_position.row, starting_position.col
    assert not moves


def test_pawn_piece_forward_moves_from_non_starting_position(
    board_white_pawn_on_non_starting_row: Board,
    white_pawn: Pawn,
    non_starting_position: Position
) -> None:
    # GIVEN a board with a white pawn not in its starting position

    # WHEN the possible moves for the pawn are retrieved
    moves = white_pawn.get_possible_moves(non_starting_position, board_white_pawn_on_non_starting_row)

    # THEN the pawn can only move forward one step
    assert moves == [Position(non_starting_position.row + 1, non_starting_position.col)]


@pytest.mark.parametrize(
    "enemy_positions",
    [
        [],
        [Position(WHITE_PAWN_START_ROW + 1, 3)],
        [Position(WHITE_PAWN_START_ROW + 1, 5)],
        [Position(WHITE_PAWN_START_ROW + 1, 3), Position(WHITE_PAWN_START_ROW + 1, 5)],
    ]
)
def test_pawn_piece_diagonal_moves(
    board_white_pawn_on_starting_row: Board,
    white_pawn: Pawn,
    starting_position: Position,
    enemy_positions: list[Position],
) -> None:
    # GIVEN a board with a white pawn in its starting position
    # AND a black pawn blocking forward movement
    board_white_pawn_on_starting_row.set_piece(Position(starting_position.row + 1, starting_position.col), Pawn(PieceColor.BLACK))
    # AND some black pawns diagonally adjacent to the white pawn
    for enemy_position in enemy_positions:
        board_white_pawn_on_starting_row.set_piece(enemy_position, Pawn(PieceColor.BLACK))

    # WHEN the possible moves for the pawn are retrieved
    moves = white_pawn.get_possible_moves(starting_position, board_white_pawn_on_starting_row)

    # THEN movement forward is not possible
    # AND the squares of the diagonally adjacent pawns can be moved to
    assert moves == enemy_positions

