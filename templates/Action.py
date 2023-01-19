class action:
    def __init__(self, name = "basic action"):
        self.types = ["loop"]
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

        #check other things

        return False

    def act(self, data):
        if self.shouldAct(data):
            #action specific stuff

            for c in self.children:
                c.act(data)

            if self.verbose:
                print(self.name +" triggered for "+ self.entity.name)
