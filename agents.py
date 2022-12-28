import chess
import chess.engine

import math
import random
import re

import numpy


class Agent():
  def __call__(self, board_str: str) -> str:
    # takes board as FEN string; returns move as UCI string
    pass

class Random(Agent):
  def __call__(self, board_str):
    board = chess.Board(board_str)
    move = random.sample(list(board.legal_moves), 1)[0]
    return move.uci()

class SameColor(Agent):
  # likes to put white pieces on white squares and vice versa
  def __call__(self, board_str):
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
  def __call__(self, board):
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
  # checkmate > check > capture > push
  def __call__(self, board_str):
    board = chess.Board(board_str)
    moves = list(board.legal_moves)
    scores = [self.score(board_str, move.uci()) for move in moves]
    best_moves = [m for (m, s) in zip(moves, scores) if s == max(scores)]
    move = random.sample(best_moves, 1)[0]
    return move.uci()

  def score(self, board_str, move_str):
    board = chess.Board(board_str)
    move = chess.Move.from_uci(move_str)
    board.push(move)
    if board.is_checkmate(): return 3
    if board.is_check(): return 2
    board.pop()
    if board.is_capture(move): return 1
    return 0
    
class Arithmetic(Agent):
  def __init__(self, const = 0):
    self.const = const % 1
  def __call__(self, board_str):
    board = chess.Board(board_str)
    legal_moves = list(board.legal_moves)
    idx = int(self.const * len(legal_moves))
    move = sorted(legal_moves, key=lambda x: str(x).lower())[idx]
    return move.uci()

class Alphabetical(Arithmetic):
  def __init__(self):
    super().__init__(const=0)

class Rational_pi(Arithmetic):
  def __init__(self):
    super().__init__(const=math.pi)

class Rational_e(Arithmetic):
  def __init__(self):
    super().__init__(const=math.e)

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
  def __call__(self, board_str):
    board = chess.Board(board_str)
    oppt_moves = []
    moves = list(board.legal_moves)
    for move in moves:
      board.push(move)
      oppt_moves.append(len(list(board.legal_moves)))
      board.pop()
    move = moves[numpy.argmin(oppt_moves)]
    return move.uci()

class Upward(Agent):
  def __call__(self, board_str):
    board = chess.Board(board_str)
    move = sorted(board.legal_moves, key=lambda x: x.to_square)[0]
    return move.uci()

class Stockfish(Agent):
  def __init__(self, path_to_stockfish, time_limit = 0.1):
    self.engine = chess.engine.SimpleEngine.popen_uci(path_to_stockfish)
    self.time_limit = time_limit
        
  def move(self, board_str):
    board = chess.Board(board_str)
    result = self.engine.play(board, chess.engine.Limit(time=self.time_limit))
    return(result.move.uci())

class NegativeStockfish(Agent):
    def move(self, board_str):
      board = chess.Board(board_str)
      scores = []
      for move in board.legal_moves:
        board.push(move)
        res = self.engine.analyse(board, chess.engine.Limit(time=self.time_limit))
        scores.append(res.get("score"))
        board.pop()
            
      scores = re.findall("\+?\-?\d+", str(scores))
        
      # get worst possible move (best move from black's pov)
      index = numpy.argmax([int(s) for s in scores])
      move = list(board.legal_moves)[index]
      return(move.uci())