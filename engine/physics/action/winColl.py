class winColl:
    def __init__(self, particles, name = " is win collider"):
        self.types = ["event"]
        self.entity = None
        self.particles = particles
        self.name = name
        self.verbose = False
        self.children = []
        return

    def shouldAct(self,data):
        
        for i in range(0,len(self.particles.pos)):
            if self.particles.active_particle[i] and self.particles.pos[i][0] > self.entity.ll[0]-10 and self.particles.pos[i][0] < self.entity.ur[0]+10 and self.particles.pos[i][1] > self.entity.ll[1]-10 and self.particles.pos[i][1] < self.entity.ur[1]+10:
                return True
        return False

    def act(self, data):
        if self.shouldAct(data):
            for c in self.children:
                c.act(data)

            if self.verbose:
                print(self.name +"triggered for "+ self.entity.name)
