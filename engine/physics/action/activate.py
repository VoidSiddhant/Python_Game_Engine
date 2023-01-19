class activate:
    def __init__(self, name = "activation action"):
        self.types = ["child"]
        self.entity = None
        self.name = name
        self.verbose = False
        self.children = []
        return

    def shouldAct(self,data):
        if self.entity == None:
            return False
        if data[0] == True:
            return True

        return False

    def act(self, data):
        if self.shouldAct(data):
            self.entity.active = True

            for c in self.children:
                c.act(data)
                print(c.name)

            if self.verbose:
                print(self.name +" triggered for "+ self.entity.name)
                # print(self.entity.active)
