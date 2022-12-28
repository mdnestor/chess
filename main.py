import chess
import chess.pgn

import random
import time

from agents import (
  Agent,
  Random,
  SameColor,
  OppositeColor,
  CCCP,
  Alphabetical,
  Rational_pi,
  Rational_e,
  MinOpptMoves,
  Upward,
  Stockfish,
  NegativeStockfish,
)


def play_game(white: Agent, black: Agent, watch=False, delay=0):
  board = chess.Board()
  node = chess.pgn.Game.without_tag_roster()
  if watch: print(board, "\n")
  while not board.outcome():
    player = [black, white][board.turn]
    
    move_uci = player(board.fen())
    move = chess.Move.from_uci(move_uci)

    board.push(move)
    node = node.add_variation(move)

    if watch: print(board, "\n")
    if delay: time.sleep(delay)
  if watch: print(board.outcome())
  return str(node.game())


if __name__ == "__main__":
  white = Random()
  black = Random()
  pgn = play_game(white, black)
  print(pgn)