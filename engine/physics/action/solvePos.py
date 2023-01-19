class solvePos:
    def __init__(self, name = "position solver"):
        self.dt = 1.0  #timestep value
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
            for i in range(0,len(self.entity.pos)):
        
                if self.entity.active_particle[i]:
                    self.entity.pos[i][0] = self.entity.pos[i][0] + self.dt * self.entity.vel[i][0]
                    self.entity.pos[i][1] = self.entity.pos[i][1] + self.dt * self.entity.vel[i][1]

            #do collisions
            for c in self.children:
                c.act(self.entity)

            if self.verbose:
                print(self.name +"triggered for "+ self.entity.name)
