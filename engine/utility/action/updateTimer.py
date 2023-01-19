class updateTimer:
    def __init__(self, name = "update timer action"):
        self.types = ["event"]
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
            self.entity.tick()

            for c in self.children:
                c.act(self.entity.elapsedTime())

            if self.verbose:
                # print(self.name +"triggered for "+ self.entity.name)
                print("timer curr time: "+str(self.entity.elapsedTime()))
