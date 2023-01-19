class Rectangle:
  def __init__(self, ll=[0,0], ur=[10,10], color=(255,255,255,255),name = "Rectangle"):
    self.actions = []
    self.name = name
    self.verbose = False
    self.active = True
    self.ll = ll
    self.ur = ur
    self.color = color
    return

  def addAction(self,a):
      a.entity = self
      self.actions.append(a)
      return
