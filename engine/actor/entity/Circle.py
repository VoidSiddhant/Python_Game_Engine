class Circle:
  def __init__(self, x=0, y=0, r=10, color=[0,0,0],name = "Circle"):
    self.actions = []
    self.name = name
    self.verbose = False
    self.active = True
    self.pos = [x,y]
    self.r=r
    self.color = color
    return

  def addAction(self,a):
      a.entity = self
      self.actions.append(a)
      return
