class pickVel:
    def __init__(self, index):
        self.index = index
        self.types = ["position"]
        self.entity = None
        self.name = "pick velocity action"
        self.verbose = False
        self.children = []
        return

    def shouldAct(self,data):
        if self.entity == None:
            return False
        if self.entity.active == False:
            return False
        if self.index >= len(self.entity.vel):
            return False
        return True

    def act(self, data):
        if self.shouldAct(data):
            data2 = list(self.entity.vel[self.index])
            for c in self.children:
                c.act(data2)
            if self.verbose:
                print(self.name +"triggered for "+ self.entity.name)
