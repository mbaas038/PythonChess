import pytest
from enums import PieceColor
from piece.pieces import Pawn
from position import Position
from square import Square


def test_square_initialization():
    pos = Position(0, 0)
    square = Square(pos)
    assert square.position == pos
    assert square.piece is None
    assert square.is_empty()

    pawn = Pawn(PieceColor.WHITE)
    square_with_piece = Square(pos, pawn)
    assert square_with_piece.position == pos
    assert square_with_piece.piece == pawn
    assert not square_with_piece.is_empty()


def test_square_set_piece():
    pos = Position(0, 0)
    square = Square(pos)
    pawn = Pawn(PieceColor.WHITE)
    
    square.set_piece(pawn)
    assert square.piece == pawn
    assert not square.is_empty()


def test_square_remove_piece():
    pos = Position(0, 0)
    pawn = Pawn(PieceColor.WHITE)
    square = Square(pos, pawn)
    
    square.remove_piece()
    assert square.piece is None
    assert square.is_empty()


def test_square_has_enemy_piece():
    pos = Position(0, 0)
    white_pawn = Pawn(PieceColor.WHITE)
    square = Square(pos, white_pawn)
    
    assert square.has_enemy_piece(PieceColor.BLACK)
    assert not square.has_enemy_piece(PieceColor.WHITE)
    
    square.remove_piece()
    assert not square.has_enemy_piece(PieceColor.BLACK)


def test_square_has_friendly_piece():
    pos = Position(0, 0)
    white_pawn = Pawn(PieceColor.WHITE)
    square = Square(pos, white_pawn)
    
    assert square.has_friendly_piece(PieceColor.WHITE)
    assert not square.has_friendly_piece(PieceColor.BLACK)
    
    square.remove_piece()
    assert not square.has_friendly_piece(PieceColor.WHITE)


def test_square_str():
    pos = Position(0, 0)
    square = Square(pos)
    assert str(square) == "a8: Empty"
    
    pawn = Pawn(PieceColor.WHITE)
    square.set_piece(pawn)

    assert "a8" in str(square)
    assert "Empty" not in str(square)
