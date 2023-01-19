class deactivateButton:
    def __init__(self, name = "deactivate button"):
        self.types = ["EVENT"]
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

        return data

    def act(self, data):
        if self.shouldAct(data):
            self.entity.active = False

            for c in self.children:
                c.act(data)

            if self.verbose:
                print(self.name +"triggered for "+ self.entity.name)
