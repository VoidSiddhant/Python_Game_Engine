class dragAct:
    def __init__(self, name = "drag force ACTION"):
        self.types = ["force"]
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

            if self.children !=[]:
                self.children[1].act(data)

            for i in range(0,len(data.acc)):
                if data.active_particle[i]:
                    data.acc[i][0] = data.acc[i][0] + data.vel[i][0] * self.entity.dragK
                    data.acc[i][1] = data.acc[i][1] + data.vel[i][1] * self.entity.dragK

            self.children[0].act(data)

            if self.verbose:
                print(self.name +" triggered for "+ self.entity.name)
