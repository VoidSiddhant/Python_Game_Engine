class activateParticle:
    def __init__(self, pos, name = "activation for particle"):
        self.types = ["child"]
        self.entity = None
        self.name = name
        self.verbose = False
        self.children = []
        self.position = pos
        return

    def shouldAct(self,data):
        if data != None :
            return True

        return False

    def act(self, data):

        if self.shouldAct(data):
            for i in range(0,len(data.acc)):
                data.active_particle[i] = True

            for c in self.children:
                c.act(data)

            if self.verbose:
                print(self.name +" triggered for "+ data.name)
