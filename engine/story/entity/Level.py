class Level:
  def __init__(self, particles, ballstart, goal, colliders, name = "Level"):
    self.actions = []
    self.name = name
    self.particles = particles
    self.ballstart = ballstart
    self.goal = goal
    self.colliders = colliders
    self.verbose = False
    self.active = True
    return

  def addAction(self,a):
      a.entity = self
      self.actions.append(a)
      return
