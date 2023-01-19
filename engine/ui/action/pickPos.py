class pickPos:
    def __init__(self, name = "ui pickpos"):
        self.types = ["position"]
        self.entity = None
        self.name = name
        self.verbose = False
        self.children = []
        return

    def shouldAct(self,data):
        # if self.entity == None:
        #     return False
        # if self.entity.active == False:
        #     return False
        if data[0] == True:
            return True

        #check other things

        return False

    def act(self, data):
        # print("pickpos "+ str(data))
        if self.shouldAct(data):
            #action specific stuff

            for c in self.children:
                c.act(self.entity.pos)

            if self.verbose:
                try:
                    print(self.name +" triggered for  "+self.entity.name)
                except:
                    print(self.name + " is an orphan :(")
