from pygame.locals import *

class stopLoop:
    def __init__(self):
        self.types = ["loop"]
        self.entity = None
        self.name = "loopkiller"
        self.children = []

    def shouldAct(self, event):
        if self.entity == None:
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
        return
