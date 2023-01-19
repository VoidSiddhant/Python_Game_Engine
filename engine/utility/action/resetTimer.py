class resetTimer:
    def __init__(self, name = "reset timer action"):
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

        if data == True:
            return True
        for i in range(0,len(data.vel)):
            if abs(data.vel[i][0]) > 0.5 or abs(data.vel[i][1]) > 0.5:
                return True

        return False

    def act(self, data):
        if self.shouldAct(data):
            self.entity.startTime = self.entity.currTime

            for c in self.children:
                c.act(data)

            if self.verbose:
                print(self.name +"triggered for "+ self.entity.name)
