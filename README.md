# Elo World

This repository contains a few algorithms for playing chess. Most of them are terrible at playing chess, but have other interesting properties. Based on [this video](https://www.youtube.com/watch?v=DpXy041BIlA).

## Usage

Requires Python. Only works on Windows. 

```
git clone https://github.com/mdnestor/elo-world.git
pip install -r requirements.txt
python3 main.py
```

## Agents

Chess agents are implemented as functions that take [FEN string](https://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation) as input, and return [UIC string](https://en.wikipedia.org/wiki/Universal_Chess_Interface) as output.
