import pytest
from position import Position


@pytest.mark.parametrize(
    ("row", "col"),
    [
        (0, 0),
        (7, 7),
    ],
)
def test_position_initialization_valid(row: int, col: int) -> None:
    pos = Position(row, col)
    assert pos.row == row
    assert pos.col == col


@pytest.mark.parametrize(
    ("row", "col"),
    [
        (-1, 0),
        (0, -1),
        (8, 0),
        (0, 8),
    ],
)
def test_position_initialization_invalid(row: int, col: int) -> None:
    with pytest.raises(ValueError):
        Position(row, col)


def test_position_equality() -> None:
    pos1 = Position(3, 4)
    pos2 = Position(3, 4)
    pos3 = Position(4, 3)

    assert pos1 == pos2
    assert pos1 != pos3


def test_position_repr() -> None:
    pos = Position(3, 4)
    assert repr(pos) == "<Position (3, 4)>"


def test_position_str() -> None:
    pos = Position(3, 4)
    assert str(pos) == "e5"


@pytest.mark.parametrize(
    ("row", "col", "expected_notation"),
    [
        (0, 0, "a8"),
        (7, 7, "h1"),
        (3, 4, "e5"),
        (7, 0, "a1"),
        (0, 7, "h8"),
    ],
)
def test_position_to_chess_notation(row, col, expected_notation):
    pos = Position(row, col)
    assert pos.to_chess_notation() == expected_notation


@pytest.mark.parametrize(
    ("row", "col", "expected_valid"),
    [
        (0, 0, True),
        (7, 7, True),
        (-1, 0, False),
        (0, -1, False),
        (8, 0, False),
        (0, 8, False),
        (4, 4, True),
    ],
)
def test_position_is_valid(row, col, expected_valid):
    assert Position.is_valid(row, col) == expected_valid
