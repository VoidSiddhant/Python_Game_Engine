class Line:
  def __init__(self, target = [0,0], start = [0,0], color=[255,255,255],name = "Line"):
    self.actions = []
    self.name = name
    self.verbose = False
    self.active = True
    self.target = target
    self.start = start
    self.color = color
    return

  def addAction(self,a):
      a.entity = self
      self.actions.append(a)
      return
