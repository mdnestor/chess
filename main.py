import chess
import random

from agents import Random, Alphabetical, Upward
from stockfish import Stockfish, NegativeStockfish


def play_game(white, black, watch=False):
  board = chess.Board()

  if watch:
    print(board, "\n")

  while not board.outcome():
    player = [black, white][board.turn]
    
    move_str = player.move(board.fen())
    move = chess.Move.from_uci(move_str)

    board.push(move)

    if watch:
      print(board, "\n")

  if watch:
    print(board.outcome())
  return board


def play_games(white, black, n_games=1, watch=False):
  score = {True: 0, False: 0, None: 0}
  for _ in range(n_games):
    board = play_game(white, black, watch=watch)
    outcome = board.outcome()
    score[outcome.winner] += 1
  return score


if __name__ == "__main__":
  score = play_games(white=Random(), black=Random(), n_games=3, watch=True)
  print(score)
