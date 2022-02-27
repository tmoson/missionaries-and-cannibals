from typing import TypedDict
from bank import Bank
from state import State
from move import Move
from node import Node

class Solver:
  def __init__(self, state: State, moves: TypedDict):
    self.root = Node(state, None, None)
    self.moves = moves

  def explored_state(self, comp_state: State, explored: TypedDict):
    for state in explored:
      if(comp_state.equals(state)):
        return True
    return False

  def solve(self):
    num_explored = 0
    explored = []
    unexplored = [self.root]
    while(unexplored != []):
      node = unexplored.pop()
      explored.append(node)
      print("Exploring State: ")
      node.state.display()
      if(not node.state.feast()):
        for move in self.moves:
          if(move.applicable(node.state)):
            child = Node(move.move(node.state), move, node)
            if(child.state.goal()):
              print("Found a goal state!")
              child.display_solution()
              return
            if(not self.explored_state(child, explored)):
              print("appended unexplored state!")
              unexplored.append(child)
    print("There is no solution")
