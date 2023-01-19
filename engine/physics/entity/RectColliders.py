class RectColliders:
  def __init__(self, colliders, name = "Rectangle Colliders"):
    self.colliders = colliders
    self.actions = []
    self.name = name
    self.verbose = False
    self.active = True
    return

  def addAction(self,a):
      a.entity = self
      self.actions.append(a)
      return
