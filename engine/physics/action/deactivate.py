class deactivate:
    def __init__(self, name = "deactivation action"):
        self.types = ["child"]
        self.entity = None
        self.name = name
        self.verbose = False
        self.children = []
        return

    def shouldAct(self,data):
        if self.entity == None:
            return False
        if data == True:
            return True
        return True

    def act(self, data):
        if self.shouldAct(data):
            self.entity.active = False

            for c in self.children:
                c.act(data)

            if self.verbose:
                print(self.name +"triggered for "+ self.entity.name)
