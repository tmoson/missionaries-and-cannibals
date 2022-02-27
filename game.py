from bank import Bank
from state import State
from move import Move
from typed import TypedDict

class Game:
  def __init__(self):
    self.state = State(Bank(3, 3, True), Bank(0, 0, False))
    self.moves = self.create_moves

  def create_moves(self):
    return {
      "c-lr": Move("c-lr", "At least one cannibal and the boat on the left bank", "Move one cannibal to the right bank"),
      "c-rl": Move("c-rl", "At least one cannibal and the boat on the right bank", "Move one cannibal to the left bank"),
      "m-lr": Move("m-lr", "At least one missionary and the boat on the left bank", "Move one missionary to the right bank"),
      "m-rl": Move("m-rl", "At least one missionary and the boat on the right bank", "Move one missionary to the left bank"),
      "cc-lr": Move("cc-lr", "At least two cannibals and the boat on the left bank", "Move two cannibals to the right bank"),
      "cc-rl": Move("cc-rl", "At least two cannibals and the boat on the right bank", "Move two cannibals to the left bank"),
      "mm-lr": Move("m-lr", "At least two missionaries and the boat on the left bank", "Move two missionaries to the right bank"),
      "mm-rl": Move("m-rl", "At least two missionaries and the boat on the right bank", "Move two missionaries to the left bank"),
      "mc-lr": Move("mc-lr", "At least one missionary and one cannibal on the left bank with the boat", "Move one missionary and one cannibal to the right bank"),
      "mc-rl": Move("mc-rl", "At least one missionary and one cannibal on the right bank with the boat", "Move one missionary and one cannibal to the left bank")
    }

  def ask_move(self):
    try:
      return self.moves[input("Enter move (e.g. m-lr): ")]
    except:
      print("That's not a move I recognize, try something like \'m-lr\' to move a missionary from the left to right bank, or \'mm-lr\' to move two missionaries from the left to right bank")
      self.ask_move()

  def manual_move(self):
    move: Move = self.ask_move
    move_applicable: bool = move.applicable(self.state)
    while(not move_applicable):
      print("Can't make that move, try again.")
      move = self.ask_move
      move_applicable = move.applicable
    self.state = move.move(self.state)

  def manual_game(self):
    while(not self.state.goal() and not self.state.feast()):
      self.manual_move()
      print("Left Bank:")
      self.state.left_bank.display()
      print("Right Bank:")
      self.state.right_bank.display()
    if(self.state.goal):
      print("Great job! Everyone made it safely across!")
    else:
      print("Oh no! Now the cannibals have a full meal!")
