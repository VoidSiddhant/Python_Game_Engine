from pygame.locals import *

class depressButton:
    def __init__(self):
        self.types = ["event"]
        self.entity = None
        self.name = "button_released_action"
        self.children = []
        self.verbose = False

    def shouldAct(self, event):
        if self.entity == None:
            return False
        if self.entity.active == False:
            return False
        for e in event:
            if e.type == MOUSEBUTTONUP:
                # check whether the mouse button is down inside the button area
                pos = e.pos
                return [self.entity.is_inside(pos),pos]
        return False

    def act(self, event):
        data = self.shouldAct(event)
        if data:
            for c in self.children:
                c.act(data)
            if self.verbose:
                print( "Button depressed at " + str(self.entity.x)+", "+str(self.entity.y))
                print("children: "+str(self.children))
        return
