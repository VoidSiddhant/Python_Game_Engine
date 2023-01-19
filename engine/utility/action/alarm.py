class alarm:
    def __init__(self, name = "alarm action"):
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
        if type(data) == int:
            return data >= self.entity.alarmVal
        return False

    def act(self, data):
        if self.shouldAct(data):
    #action specific stuff
            
            for c in self.children:
                c.act(True)

            if self.verbose:
                print(self.name +"triggered for "+ self.entity.name)
                print("Alarm amount: " + str(self.entity.alarmVal))
        # else:
        #     for c in self.children:
        #         c.act(True)
