class deactivateParticle:
    def __init__(self, pos, name = "deactivation for particle"):
        self.types = ["child"]
        self.entity = None
        self.name = name
        self.verbose = False
        self.children = []
        self.position = pos
        return

    def shouldAct(self,data):

        if data != None:
            return True

        return False

    def act(self, data):
        if self.shouldAct(data):
            for i in range(0,len(data.acc)):
                if self.position < 0:
                    if data.pos[i][0] >= -self.position:
                        data.active_particle[i] = False
                else:
                    if data.pos[i][0] < self.position:
                        data.active_particle[i] = False


            for c in self.children:
                c.act(data)

            if self.verbose:
                print(self.name +"triggered for " + data.name)
