import chess
import chess.engine

import numpy
import re

from agents import Agent

class Stockfish(Agent):
  def __init__(self, path_to_stockfish):
    self.engine = chess.engine.SimpleEngine.popen_uci(path_to_stockfish)
        
  def move(self, board_str):
    board = chess.Board(board_str)
    result = self.engine.play(board, chess.engine.Limit(time=0.1))
    return(result.move.uci())


class NegativeStockfish(Agent):
    def __init__(self, path_to_stockfish):
        self.engine = chess.engine.SimpleEngine.popen_uci(path_to_stockfish)
        
    def move(self, board_str):
      board = chess.Board(board_str)
      scores = []
      for move in board.legal_moves:
        board.push(move)
        res = self.engine.analyse(board, chess.engine.Limit(time=.1))
        scores.append(res.get('score'))
        board.pop()
            
      scores = re.findall("\+?\-?\d+", str(scores))
        
      # get worst possible move (best move from black's pov)
      index = numpy.argmax([int(s) for s in scores])
      move = list(board.legal_moves)[index]
      return(move.uci())