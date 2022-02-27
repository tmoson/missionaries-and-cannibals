from typing import TypedDict
from state import State
from bank import Bank

class Move:
  def __init__(self, name: str, precondition: str, desc: str):
    self.name = name
    self.precondidion = precondition
    self.desc = desc

  def applicable_c_lr(self, state: State):
    return state.left_bank.boat and state.left_bank.cannibals > 0

  def applicable_c_rl(self, state: State):
    return state.right_bank.boat and state.right_bank.cannibals > 0

  def applicable_m_lr(self, state: State):
    return state.left_bank.boat and state.left_bank.missionaries > 0

  def applicable_m_rl(self, state: State):
    return state.right_bank.boat and state.right_bank.missionaries > 0

  def applicable_cc_lr(self, state: State):
    return state.left_bank.boat and state.left_bank.cannibals > 1

  def applicable_cc_rl(self, state: State):
    return state.right_bank.boat and state.right_bank.cannibals > 1

  def applicable_mm_lr(self, state: State):
    return state.left_bank.boat and state.left_bank.missionaries > 1

  def applicable_mm_rl(self, state: State):
    return state.right_bank.boat and state.right_bank.missionaries > 1

  def applicable_mc_lr(self, state: State):
    return state.left_bank.boat and state.left_bank.missionaries > 0 and state.left_bank.cannibals > 0

  def applicable_mc_rl(self, state: State):
    return state.right_bank.boat and state.right_bank.missionaries > 0 and state.right_bank.cannibals > 0

  def applicable(self, state: State):
    moves = {"c-lr": self.applicable_c_lr,
         "c-rl": self.applicable_c_rl,
         "m-lr": self.applicable_m_lr,
         "m-rl": self.applicable_m_rl,
         "cc-lr": self.applicable_cc_lr,
         "cc-rl": self.applicable_cc_rl,
         "mm-lr": self.applicable_mm_lr,
         "mm-rl": self.applicable_mm_rl,
         "mc-lr": self.applicable_mc_lr,
         "mc-rl": self.applicable_mc_rl}
    return moves[self.name](state)

  def c_lr(self, state: State):
    left_bank = Bank(state.left_bank.missionaries,
             state.left_bank.cannibals - 1, False)
    right_bank = Bank(state.right_bank.missionaries,
              state.right_bank.cannibals + 1, True)
    return State(left_bank, right_bank)

  def c_rl(self, state: State):
    left_bank = Bank(state.left_bank.missionaries,
             state.left_bank.cannibals + 1, True)
    right_bank = Bank(state.right_bank.missionaries,
              state.right_bank.cannibals - 1, False)
    return State(left_bank, right_bank)

  def m_lr(self, state: State):
    left_bank = Bank(state.left_bank.missionaries - 1,
             state.left_bank.cannibals, False)
    right_bank = Bank(state.right_bank.missionaries + 1,
              state.right_bank.cannibals, True)
    return State(left_bank, right_bank)

  def m_rl(self, state: State):
    left_bank = Bank(state.left_bank.missionaries + 1,
             state.left_bank.cannibals, True)
    right_bank = Bank(state.right_bank.missionaries - 1,
              state.right_bank.cannibals, False)
    return State(left_bank, right_bank)

  def cc_lr(self, state: State):
    left_bank = Bank(state.left_bank.missionaries,
             state.left_bank.cannibals - 2, False)
    right_bank = Bank(state.right_bank.missionaries,
              state.right_bank.cannibals + 2, True)
    return State(left_bank, right_bank)

  def cc_rl(self, state: State):
    left_bank = Bank(state.left_bank.missionaries,
             state.left_bank.cannibals + 2, True)
    right_bank = Bank(state.right_bank.missionaries,
              state.right_bank.cannibals - 2, False)
    return State(left_bank, right_bank)

  def mm_lr(self, state: State):
    left_bank = Bank(state.left_bank.missionaries - 2,
             state.left_bank.cannibals, False)
    right_bank = Bank(state.right_bank.missionaries + 2,
              state.right_bank.cannibals, True)
    return State(left_bank, right_bank)

  def mm_rl(self, state: State):
    left_bank = Bank(state.left_bank.missionaries + 2,
             state.left_bank.cannibals, True)
    right_bank = Bank(state.right_bank.missionaries - 2,
              state.right_bank.cannibals, False)
    return State(left_bank, right_bank)

  def mc_lr(self, state: State):
    left_bank = Bank(state.left_bank.missionaries - 1,
             state.left_bank.cannibals - 1, False)
    right_bank = Bank(state.right_bank.missionaries + 1,
              state.right_bank.cannibals + 1, True)
    return State(left_bank, right_bank)

  def mc_rl(self, state: State):
    left_bank = Bank(state.left_bank.missionaries + 1,
             state.left_bank.cannibals + 1, True)
    right_bank = Bank(state.right_bank.missionaries - 1,
              state.right_bank.cannibals - 1, False)
    return State(left_bank, right_bank)

  def move(self, state: State):
    moves = {"c-lr": self.c_lr,
         "c-rl": self.c_rl,
         "m-lr": self.m_lr,
         "m-rl": self.m_rl,
         "cc-lr": self.cc_lr,
         "cc-rl": self.cc_rl,
         "mm-lr": self.mm_lr,
         "mm-rl": self.mm_rl,
         "mc-lr": self.mc_lr,
         "mc-rl": self.mc_rl}
    return moves[self.name](state)
