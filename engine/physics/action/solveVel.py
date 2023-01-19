#velocity solver action
class solveVel:
    def __init__(self, name = "velocity solver"):
        self.dt = 1.0
        self.types = ["physics"]
        self.entity = None
        self.name = name
        self.verbose = False
        self.children = []
        return

    def shouldAct(self,data):
        if self.entity == None:
            return False
        if self.entity.active == False:
            return False



        return True

    def act(self, data):
        if self.shouldAct(data):
            #reset acceleration for each particle
            for i in range(0,len(self.entity.acc)):
                if self.entity.active_particle[i]:
                    self.entity.acc[i][0] = 0.0
                    self.entity.acc[i][1] = 0.0
            #children compute acceleration
            for c in self.children:
                c.act(self.entity)
            #now update velocity

            for i in range(0,len(self.entity.vel)):
                if self.entity.active_particle[i]:
                    self.entity.vel[i][0] = self.entity.vel[i][0] + self.dt * self.entity.acc[i][0]
                    self.entity.vel[i][1] = self.entity.vel[i][1] + self.dt * self.entity.acc[i][1]



            if self.verbose:
                print(self.name +"triggered for "+ self.entity.name)
