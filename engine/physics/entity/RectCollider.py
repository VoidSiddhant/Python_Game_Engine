class RectCollider:
  def __init__(self, ll = [0.0,0.0], ur = [100.0,100.0], name = "Rectangle Collider"):
    self.ll = ll
    self.ur = ur
    self.actions = []
    self.color = (255, 255, 255)
    self.name = name
    self.verbose = False
    self.active = True

    return

  def addAction(self,a):
      a.entity = self
      self.actions.append(a)
      return
