class ForceGravity:
  def __init__(self, name = "Gravity Force"):
    self.gravity = [0.0,1.0]

    self.actions = []
    self.name = name
    self.verbose = False
    self.active = True
    return

  def addAction(self,a):
      a.entity = self
      self.actions.append(a)
      return
