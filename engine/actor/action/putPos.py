class putPos:
    def __init__(self, name = "put position"):
        self.types = ["position"]
        self.entity = None
        self.name = name
        self.verbose = False
        self.children = []
        self.index = 0
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
            self.entity.pos[0] = data[0]
            self.entity.pos[1] = data[1]

            for c in self.children:
                c.act(data)

            if self.verbose:
                print(self.name +"triggered for "+ self.entity.name)
