class putPos:
    def __init__(self, name = "ui putpos"):
        self.types = ["position"]
        self.entity = None
        self.name = name
        self.verbose = False
        self.children = []
        return

    def shouldAct(self,data):
        if self.entity == None:
            return False
        # if self.entity.active == False:
        #     return False
        if self.entity.particleMoving:
            return False
        if data[0] == True:
            return True
        #check other things

        return False

    def act(self, data):
        if self.shouldAct(data):
            self.entity.target = data[1]
            # print("target" + str(self.entity.target))

            for c in self.children:
                c.act(data)

            if self.verbose:
                print(self.name +" triggered for "+ self.entity.name)
