import pytest

from board import Board


@pytest.fixture(name="board")
def _board() -> Board:
    return Board()
