import importlib as il

class buildLevel:
    def __init__(self, name = "build level"):
        self.types = ["event"]
        self.entity = None
        self.name = name
        self.verbose = False
        self.children = []
        self.altChildren = []
        return

    def shouldAct(self,data):


        return True

    def act(self, data):
        if self.shouldAct(data):
            import engine.story.entity as st
            #import numerical data from level data file
            from engine.story.entity.LevelData import allLevelData

            #as long as we have more levels, when this action is called, load the next level
            if self.entity.counter < len(allLevelData):
                #LOAD LEVEL
                c = self.entity.counter
                currentlevel = st.Level(self.entity.particles, allLevelData[c][0], allLevelData[c][1], allLevelData[c][2])

                #PARTICLE POS AND VELOCITY
                currentlevel.particles.pos[0] = currentlevel.ballstart
                currentlevel.particles.vel[0] = [0, 0]

                #CREATE GOAL
                self.entity.winzone.ll = currentlevel.goal[0]
                self.entity.winzone.ur = currentlevel.goal[1]

                #CREATE COLLIDERS
                self.entity.colliders.colliders = currentlevel.colliders

                #For the last (hidden) level, set ball at 40,710 to prevent winloop
                if self.entity.counter == len(allLevelData)-1:
                    currentlevel.particles.pos[0] = [40,710]

                for c in self.children:
                    c.act(self.entity.counter)
                if self.verbose:
                    print (self.entity.name + ": " + str(self.entity.counter))
