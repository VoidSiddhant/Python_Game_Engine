class HUD:
  def __init__(self, name = "HUD entity"):
    self.actions = []
    self.name = name
    self.successes = 0
    self.totals = 0
    self.sMsg = ""
    self.tMsg = ""
    self.verbose = False
    self.active = True
    return

  def addAction(self,a):
      a.entity = self
      self.actions.append(a)
      return
