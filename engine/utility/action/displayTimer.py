class displayTimer:
    def __init__(self, name = "show timer value"):
        self.types = ["child"]
        self.entity = None
        self.name = name
        self.verbose = False
        self.children = []
        self.message = "Level complete in "
        return

    def shouldAct(self,data):
        if self.entity == None:
            return False
        if self.entity.active == False:
            return False

        return True

    def act(self, data):
        if self.shouldAct(data):
            t = self.entity.elapsedTime()/1000

            print (self.message + str(t)+" seconds!")

            for c in self.children:
                c.act(True)

            if self.verbose:
                print(self.name +" triggered for "+ self.entity.name)
