from pygame.locals import *

class windowClose:
    def __init__(self):
        self.types = ["event"]
        self.entity = None
        self.name = "window closed"
        self.children = []

    def shouldAct(self, event):
        if self.entity == None:
            return False
        if self.entity.active == False:
            return False
        for e in event:
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
            # check whether the mouse button is down inside the button area
                    return True
        return False

    def act(self, event):
        if self.shouldAct(event):
            self.entity.active = False
            # print( self.name + " for " + self.entity.name + " at " + str(event[0].pos))
        return
