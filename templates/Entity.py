class Entity:
  def __init__(self, name = "Basic Entity Name"):
    self.actions = []
    self.name = name
    self.verbose = False
    self.active = True
    return

  def addAction(self,a):
      a.entity = self
      self.actions.append(a)
      return
