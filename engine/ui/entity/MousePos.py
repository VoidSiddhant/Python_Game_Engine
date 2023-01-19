class MousePos:
  def __init__(self, name = "Mouse Position"):
    self.actions = []
    self.name = name
    self.verbose = False
    self.active = True
    self.pos = [0,0]
    self.isLeftPressed = False
    return

  def addAction(self,a):
      a.entity = self
      self.actions.append(a)
      return
