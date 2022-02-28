from bank import Bank
from state import State
from move import Move
from solver import Solver

state = State(Bank(3, 3, True), Bank(0, 0, False))
moves = [
  Move("c-lr", "At least one cannibal and the boat on the left bank",
     "Move one cannibal to the right bank"),
  Move("c-rl", "At least one cannibal and the boat on the right bank",
     "Move one cannibal to the left bank"),
  Move("m-lr", "At least one missionary and the boat on the left bank",
     "Move one missionary to the right bank"),
  Move("m-rl", "At least one missionary and the boat on the right bank",
     "Move one missionary to the left bank"),
  Move("cc-lr", "At least two cannibals and the boat on the left bank",
     "Move two cannibals to the right bank"),
  Move("cc-rl", "At least two cannibals and the boat on the right bank",
     "Move two cannibals to the left bank"),
  Move("mm-lr", "At least two missionaries and the boat on the left bank",
     "Move two missionaries to the right bank"),
  Move("mm-rl", "At least two missionaries and the boat on the right bank",
     "Move two missionaries to the left bank"),
  Move("mc-lr", "At least one missionary and one cannibal on the left bank with the boat",
     "Move one missionary and one cannibal to the right bank"),
  Move("mc-rl", "At least one missionary and one cannibal on the right bank with the boat",
     "Move one missionary and one cannibal to the left bank")
]

mc_solver = Solver(state, moves)
