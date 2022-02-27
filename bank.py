class Bank:
  def __init__(self, missionaries: int, cannibals: int, boat: bool):
    self.missionaries = missionaries
    self.cannibals = cannibals
    self.boat = boat

  def empty(self):
    return self.missionaries == 0 and self.cannibals == 0

  def feast(self):
    return self.missionaries < self.cannibals and self.missionaries != 0

  def equals(self, bank2):
    return self.missionaries == bank2.missionaries and self.cannibals == bank2.cannibals and self.boat == bank2.boat

  def display(self):
    print("Missionaries: ", end="")
    for i in range(self.missionaries):
      print(" M", end="")
    print("\nCannibals: ", end="")
    for i in range(self.cannibals):
      print(" C", end="")
    print("\nBoat: ", end="")
    if(self.boat):
      print(" B")
    else:
      print("")
