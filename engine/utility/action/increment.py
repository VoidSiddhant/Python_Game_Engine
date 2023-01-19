class increment:
    def __init__(self, name = "increment counter"):
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
        if data == True:
            return True

        #check other things

        return True

    def act(self, data):
        if self.shouldAct(data):
            self.entity.counter +=1

            #since increment needs to work for both trackers, let children know
            #which values to update. This gets sent to "generateMessage"
            for c in self.children:
                c.act(self.entity.counter)
            if self.verbose:
                # print(self.name +"triggered for "+ self.entity.name)
                print (self.entity.name + ": " + str(self.entity.counter))
