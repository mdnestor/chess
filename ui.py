import chess
import chess.svg
import pygame
from cairosvg import svg2png
import time
from agents import Random, MinOpptMoves

pygame.init()
screen = pygame.display.set_mode((390, 390))

board = chess.Board()
white = MinOpptMoves()
black = Random()

done = False
while not done:
  svg_string = chess.svg.board(board, size=390) 
  svg2png(bytestring=svg_string, write_to='board.png')
  surface = pygame.image.load('board.png')

  screen.blit(surface, (0, 0))
  pygame.display.flip()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True

  time.sleep(.5)

  player = [black, white][board.turn]
  move_str = player.move(board.fen())
  move = chess.Move.from_uci(move_str)
  print(board.san(move))
  board.push(move)

  if board.outcome():
    done = True
