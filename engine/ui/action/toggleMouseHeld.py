class toggleMouseHeld:
    def __init__(self, name = " action to update Mouse.isleftpressed"):
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
        # print("toggle"+str(data))
        if self.shouldAct(data):
            if self.entity.isLeftPressed == True:
                self.entity.isLeftPressed = False
            else:
                self.entity.isLeftPressed = True

            for c in self.children:
                c.act(data)

            if self.verbose:
                print("togglemouse: "+str(self.entity.isLeftPressed))
