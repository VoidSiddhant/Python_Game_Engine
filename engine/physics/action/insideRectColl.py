class insideRectColl:
    def __init__(self, name = " is inside collider"):
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
        if data == None:
            return False
        return True

    def act(self, data):
        if self.shouldAct(data):
            for i in range(0,len(data.pos)):
                if data.active_particle[i]:
                    if data.pos[i][0] < self.entity.ll[0]:                                      #return halved velocity to reduce crazy bouncing
                        data.pos[i][0] = 2.0 * self.entity.ll[0] - data.pos[i][0]
                        data.vel[i][0] = -data.vel[i][0] / 2
                    elif data.pos[i][0] > self.entity.ur[0]:
                        data.pos[i][0] = 2.0*self.entity.ur[0] - data.pos[i][0]
                        data.vel[i][0] = -data.vel[i][0] / 2
                    elif data.pos[i][1] < self.entity.ll[1]:
                        data.pos[i][1] = 2.0*self.entity.ll[1] - data.pos[i][1]
                        data.vel[i][1] = -data.vel[i][1] / 2
                    elif data.pos[i][1] > self.entity.ur[1]:
                        data.pos[i][1] = 2.0*self.entity.ur[1] - data.pos[i][1] + 0.5
                        data.vel[i][1] = -data.vel[i][1] / 2
                        data.vel[i][0] *= 0.9                                                   #add drag if paricle is touching ground

            for c in self.children:
                c.act(data)

            if self.verbose:
                print(self.name +"triggered for "+ self.entity.name)
