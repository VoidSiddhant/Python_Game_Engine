class shootAct:
    def __init__(self, name = "shoot force ACTION"):
        self.types = ["child"]
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
        if self.entity.particleMoving:
            return False
        return True


    def act(self, data):
        if self.shouldAct(data):
            for i in range(0,len(data.acc)):
                if data.active_particle[i]:
                        data.acc[i][0] = data.acc[i][0] + (self.entity.target[0]-data.pos[i][0]) * self.entity.dragK
                        data.acc[i][1] = data.acc[i][1] + (self.entity.target[1]-data.pos[i][1]) * self.entity.dragK

            for c in self.children:
                c.act(data)

            if self.verbose:
                print(self.name +" triggered for "+ self.entity.name)
