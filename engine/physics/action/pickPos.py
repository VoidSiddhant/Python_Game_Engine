class pickPos:
    def __init__(self, index):
        self.index = index
        self.types = ["position"]
        self.entity = None
        self.name = "pick position action"
        self.verbose = False
        self.children = []
        return

    def shouldAct(self,data):
        if self.entity == None:
            return False
        if self.entity.active == False:
            return False
        if self.index >= len(self.entity.pos):
            return False
        return True

    def act(self, data):
        if self.shouldAct(data):
            data2 = list(self.entity.pos[self.index])
            for c in self.children:
                c.act(data2)

            if self.verbose:
                print(self.name +"triggered for "+ self.entity.name)
