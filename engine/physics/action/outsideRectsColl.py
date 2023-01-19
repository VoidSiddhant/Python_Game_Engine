class outsideRectsColl:
    def __init__(self, name = " is outside colliders"):
        self.types = ["physics"]
        self.entity = None
        self.name = name
        self.verbose = False
        self.children = []
        return

    def shouldAct(self,data):
        return True

    def act(self, data):
        if self.shouldAct(data):
            for test in self.entity.colliders:
                collider = [[0,0],[0,0]]
                collider[0][0] =test[0][0]-10    #offset by 10 to make ball collide on edge not center
                collider[0][1] =test[0][1]-10
                collider[1][0] =test[1][0]+10
                collider[1][1] =test[1][1]+10
                for i in range(0,len(data.pos)):
                    if data.active_particle[i] and data.pos[i][0] > collider[0][0] and data.pos[i][0] < collider[1][0] and data.pos[i][1] > collider[0][1] and data.pos[i][1] < collider[1][1] and data.vel[i][0] != 0 and data.vel[i][1] != 0:


                        rightTime = (data.pos[i][0] - collider[0][0])/data.vel[i][0]
                        if rightTime < 0.0:
                            rightTime = 100000000.0
                        leftTime = (data.pos[i][0] - collider[1][0])/data.vel[i][0]
                        if leftTime < 0.0:
                            leftTime = 100000000.0
                        topTime = (data.pos[i][1] - collider[0][1])/data.vel[i][1]
                        if topTime < 0.0:
                            topTime = 100000000.0
                        botTime = (data.pos[i][1] - collider[1][1])/data.vel[i][1]
                        if botTime < 0.0:
                            botTime = 100000000.0
                        minTime = min(rightTime,leftTime,topTime, botTime)

                        if rightTime == minTime: #hits right side
                            data.pos[i][0] = 2.0*collider[0][0] - data.pos[i][0]        #return halved velocity to reduce crazy bouncing
                            data.vel[i][0] = -data.vel[i][0] / 2
                        elif leftTime == minTime: #hits left side
                            data.pos[i][0] = 2.0*collider[1][0] - data.pos[i][0]
                            data.vel[i][0] = -data.vel[i][0] / 2
                        elif topTime == minTime: #hits top
                            data.pos[i][1] = 2.0*collider[0][1] - data.pos[i][1]
                            data.vel[i][1] = -data.vel[i][1] / 2
                            data.vel[i][0] *= 0.9                                       #add drag when particle touches ground
                        else:                   #hits bottom
                            data.pos[i][1] = 2.0*collider[1][1] - data.pos[i][1]
                            data.vel[i][1] = -data.vel[i][1] / 2


            for c in self.children:
                c.act(data)

            if self.verbose:
                print(self.name +"triggered for "+ self.entity.name)
