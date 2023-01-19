class solveEuler:
    def __init__(self, name = "Euler solver"):
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
        if len(self.children) < 2:
            return False
        return True

    def act(self, data):
        if self.shouldAct(data):
            self.children[0].dt = float(self.dt)
            self.children[1].dt = float(self.dt)
            self.children[0].act(data)
            self.children[1].act(data)

            for c in self.children[2:]:
                c.act(data)

            if self.verbose:
                print(self.name +"triggered for "+ self.entity.name)
