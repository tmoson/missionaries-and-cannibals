from typing import TypedDict
from bank import Bank
from state import State
from move import Move
from node import Node

class Solver:
  def __init__(self, state: State, moves: TypedDict):
    self.root = Node(state, None, 0, None)
    self.moves = moves

  def explored_state(self, comp_state: Node, explored: TypedDict):
    for node in explored:
      if(comp_state.equals(node)):
        print("skipping state")
        return True
    return False

  def solve(self):
    num_nodes = 0
    explored = []
    unexplored = [self.root]
    while(unexplored != []):
      node = unexplored.pop()
      explored.append(node)
      # uncomment this region for easier tracing
      # print("E-node >>>>>>>>>>>>>>>>>>>>")
      # node.display()
      # print(">>>>>>>>>>>>>>>>>>>>>>>>>>>")
      if(node.state.goal()):
        node.display_solution()
        return
      for move in self.moves:
        if(move.applicable(node.state)):
          num_nodes += 1
          child = Node(move.move(node.state), move, num_nodes, node)
          if(not self.explored_state(child, explored) and not child.state.feast()):
            unexplored.append(child)
      # uncomment this region for easier tracing
      # print("UNEXPLORED: >>>>>>>>>>>>>>>>>>>>")
      # for node in unexplored:
      #   node.display()
      # print(">>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("There is no solution")
