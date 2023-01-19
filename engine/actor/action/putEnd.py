class putEnd:
    def __init__(self, name = " putpos for line end"):
        self.types = ["position"]
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
            self.entity.target = data[1]
            
            for c in self.children:
                c.act(data)

            if self.verbose:
                print(self.name +" triggered for "+ self.entity.name)
