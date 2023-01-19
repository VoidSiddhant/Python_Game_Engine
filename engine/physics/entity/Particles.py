class Particles:
  def __init__(self, name = "Particles Entity"):
    self.actions = []
    self.name = name
    self.verbose = False
    self.active = True

    self.pos = []
    self.vel = []
    self.acc = []
    self.mass = []
    self.active_particle = []
    #
    self.radius = 10
    return

  def addAction(self,a):
      a.entity = self
      self.actions.append(a)

      return

  def addParticle(self, p, v, m):
    self.pos.append(p)
    self.vel.append(v)
    self.acc.append([0.0,0.0])
    self.mass.append(m)
    self.active_particle.append(True)

  def addForce(self, f):
      self.forces_felt.update({f.name:True})

  def addForces(self, forces):
      for f in forces:
          self.forces_felt.update({f.name:True})
