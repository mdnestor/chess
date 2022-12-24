import chess
import random
import numpy as np

class Agent():
  def move(self, board_str: str) -> str:
    # takes board as FEN string; returns move as UCI string
    pass

class Random(Agent):
  def move(self, board_str):
    board = chess.Board(board_str)
    move = random.sample(list(board.legal_moves), 1)[0]
    return move.uci()

class SameColor(Agent):
  # likes to put white pieces on white squares and vice versa
  def move(self, board_str):
    board = chess.Board(board_str)
    moves = list(board.legal_moves)
    same_color_moves = [move for move in moves if (move.to_square + move.to_square//8) % 2 == board.turn]
    if same_color_moves:
      move = random.sample(same_color_moves, 1)[0]
    else:
      move = random.sample(moves, 1)[0]
    return move.uci()

class OppositeColor(Agent):
  # likes to put white pieces on black squares and vice versa
  def move(self, board):
    moves = list(board.legal_moves)
    opp_color_moves = [move for move in moves if (move.to_square + move.to_square//8) % 2 == 1 - board.turn]
    if opp_color_moves:
      move = random.sample(opp_color_moves, 1)[0]
    else:
      move = random.sample(moves, 1)[0]
    return move.uci()

class Huddle(Agent):
  # likes to move pieces close to their own king
  pass

class Swarm(Agent):
  # likes to move pieces close to the enemy king
  pass

class SymMirrorY(Agent):
  # try to make board symmetric
  pass

class SymMirrorX(Agent):
  # try to make board symmetric
  pass

class Sym180(Agent):
  # try to make board symmetric
  pass

class ReverseStarting(Agent):
  # try to reverse starting positions
  pass

class CCCP(Agent):
  # checkmate check capture push
  pass

class Alphabetical():
  def move(self, board_str):
    board = chess.Board(board_str)
    move = sorted(board.legal_moves, key=lambda x: str(x).lower())[0]
    return move.uci()

class FirstMove(Agent):
  pass

class Safe(Agent):
  pass

class Popular(Agent):
  pass

class Dangerous(Agent):
  pass

class Rare(Agent):
  pass

class Survivalist(Agent):
  pass

class Fatalist(Agent):
  pass

class Pacifist(Agent):
  # avoids checkmate, checking, and capturing
  pass

class Generous(Agent):
  # offers up pieces to capture
  pass

class NoIInsist(Agent):
  pass

class SuicideKing(Agent):
  # tries to move king closest to enemy king
  pass

class MinOpptMoves(Agent):
  def move(self, board_str):
    board = chess.Board(board_str)
    oppt_moves = []
    moves = list(board.legal_moves)
    for move in moves:
      board.push(move)
      oppt_moves.append(len(list(board.legal_moves)))
      board.pop()
    move = moves[np.argmin(oppt_moves)]
    return move.uci()

class Upward():
  def play(self, board_str):
    board = chess.Board(board_str)
    move = sorted(board.legal_moves, key=lambda x: x.to_square)[0]
    return move.uci()
        

