class isStill:
    def __init__(self, name = "check particle motion action"):
        self.types = ["child"]
        self.entity = None
        self.name = name
        self.verbose = False
        self.children = []
        return

    def shouldAct(self,data):
        if self.entity == None:
            return False
        return True

    def act(self, data):
        if self.shouldAct(data):
            self.entity.particleMoving = False

            for c in self.children:
                c.act(data)

            if self.verbose:
                print("\"Still\" says particle moving is "+str(self.entity.particleMoving))
