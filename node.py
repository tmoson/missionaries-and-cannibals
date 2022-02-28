from typing import TypedDict
from bank import Bank
from state import State
from move import Move

class Node:
  def __init__(self, state: State, move: Move, number: int, parent):
    self.name = "N%s" % number
    self.state = state
    self.move = move
    self.parent = parent

  def equals(self, node2):
    return self.state.equals(node2.state)
    
  def display(self):
    print(self.name)
    if(not self.parent == None):
      print("Parent: ", self.parent.name)
    if(not self.move == None):
      print(self.move.desc)
    print("State: ")
    self.state.display()

  def display_solution(self):
    if(self.parent == None):
      print("Starting State: ")
      self.state.display()
    else:
      self.parent.display_solution()
      self.display()
