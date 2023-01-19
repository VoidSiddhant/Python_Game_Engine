class LevelCount:
  def __init__(self, particles, winzone, colliders, name = "Level tracker"):
    self.actions = []
    self.name = name
    self.counter = 0 #current level number
    # self.levels = []
    self.particles = particles
    self.winzone = winzone
    self.colliders = colliders
    self.verbose = False
    self.active = True
    return

  def addAction(self,a):
      a.entity = self
      self.actions.append(a)
      return

  def addLevel(self,a):
      a.entity = self
      # self.levels.append(a)
      return
