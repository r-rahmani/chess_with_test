import pytest
from chess import *

@pytest.fixture 

def board():
    return Board() 

# We test whether the nut is in the correct coordinates and whether it moves correctly or not
def test_pawn_checker(board):
    pawn = Pawn(0)
    result = pawn.checker(1, 2, 2, 2) # Current and next coordinates
    print("test_pawn_checker Result:", result)
    assert result == True

def test_king_checker(board):
    king = King(0, 0, 4)
    result = king.checker(0, 4, 1, 4)
    print("test_king_checker Result:", result)
    assert result == True

def test_quinn_checker(board):
    quinn = Quinn(0)
    result = quinn.checker(0, 3, 4, 7)
    print("test_quinn_checker Result:", result)
    assert result == False

def test_ladya_checker(board):
    ladya = Ladya(0)
    result = ladya.checker(0, 0, 1, 0)
    print("test_ladya_checker Result:", result)
    assert result == True

def test_horse_checker(board):
    horse = Horse(0)
    result = horse.checker(0, 1, 2, 0)
    print("test_horse_checker Result:", result)
    assert result == True

def test_bishop_checker(board):
    bishop = Bishop(0)
    result = bishop.checker(0, 2, 2, 0)
    print("test_bishop_checker Result:", result)
    assert result == False

def test_shashka_shcan_beat(board):
    shashka = Shashka(0)
    result = shashka.shcan_beat(2, 2, 4, 4)
    print("test_shashka_shcan_beat Result:", result)
    assert result == (False, 1, 1)

def test_shashka_shcan_move(board):
    shashka = Shashka(0)
    result = shashka.shcan_move(2, 2, 3, 2)
    print("test_shashka_shcan_move Result:", result)
    assert result == True

def test_board_checker(board):
    result = board.checker(6, 3, 5, 3)
    print("test_board_checker Result:", result)
    assert result == True

def test_board_can_beat(board):
    result = board.can_beat(0, 0)
    print("test_board_can_beat Result:", result)
    assert result == False

