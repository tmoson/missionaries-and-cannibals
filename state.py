from bank import Bank
from typing import TypedDict

class State:
  def __init__(self, left_bank: Bank, right_bank: Bank):
    self.left_bank = left_bank
    self.right_bank = right_bank

  def equals(self, state2):
    return self.left_bank.equals(state2.left_bank) and self.right_bank.equals(state2.right_bank)

  def goal(self):
    return self.right_bank.missionaries == 3 and self.right_bank.cannibals == 3 and self.right_bank.boat

  def feast(self):
    return self.left_bank.feast() or self.right_bank.feast()
  
  def display(self):
    print("Left Bank:\n")
    self.left_bank.display()
    print("\nRight Bank:\n")
    self.right_bank.display()

