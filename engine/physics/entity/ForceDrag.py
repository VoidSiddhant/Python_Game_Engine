class ForceDrag:
  def __init__(self, name = "Drag Force Action"):
    self.dragK = 0.1

    self.actions = []
    self.name = name
    self.verbose = False
    self.active = True
    return

  def addAction(self,a):
      a.entity = self
      self.actions.append(a)
      return
