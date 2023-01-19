class ForceShoot:
  def __init__(self, name = "Shoot Force "):
    self.dragK = 1
    self.target = [400,400] #where shoot force is pointing
    self.actions = []
    self.name = name
    self.verbose = False
    self.active = True
    self.particleMoving = True
    self.particles = []
    return

  def addAction(self,a):
      a.entity = self
      self.actions.append(a)
      return
