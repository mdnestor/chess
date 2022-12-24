# Elo World

This repository contains a few algorithms for playing chess. Most of them are terrible at playing chess, but have other interesting properties. Based on [this video](https://www.youtube.com/watch?v=DpXy041BIlA).

## Usage

Requires Python. Only works on Windows. 

```
git clone https://github.com/mdnestor/eloworld.git
pip install -r requirements.txt
python3 main.py
```

## Agents

Agents are implemented as classes with a method `move` that takes the board as a [FEN string](https://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation) returns the move as a [UIC string](https://en.wikipedia.org/wiki/Universal_Chess_Interface).

### Implemented

- `Random` - selects a move uniformly at random from the set of legal moves.
- `Upward` - moves the pieces upward.
- `Alphabetical` - selects the first move ordered alphabetically according to the UCI notation.
- `SameColor` - moves white pieces to white squares, and black pieces to black squres.
- `OppositeColor` - moves white pieces to black squares, and... yeah, you get it.
- `MinOpptMoves` - selects the move which results in the opponent having the least number of legal moves.
- `Stockfish` - the classic Stockfish engine. Requires separate installation.
- `NegativeStockfish` - orders the moves via Stockfish's preferences, and selects the worst one. Basically tries to lose.

### Not implemented
- `Huddle` - moves pieces closes to their own king.
- `Swarm` - moves pieces towards the enemy king.
- `SymMirrorY` - prefers the board to be vertically symmetrical.
- `SymMirrorX` - prefers the board to be horizontally symmetrical.
- `ReverseStarting` - attempts to swap the starting positions of white and black.
- `CCCP` - checkmate, check, capture, push - in order of preference.
