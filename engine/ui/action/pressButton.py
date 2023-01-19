from pygame.locals import *

class pressButton:
    def __init__(self):
        self.types = ["event"]
        self.entity = None
        self.name = "button_pressed_action"
        self.children = []
        self.verbose = False

    def shouldAct(self, event):
        if self.entity == None:
            return False
        if self.entity.active == False:
            return False
        for e in event:
            if e.type == MOUSEBUTTONDOWN:
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
                print( "Button pressed at " + str(self.entity.x)+", "+str(self.entity.y))
                print(pos)
                # for c in self.children:
                #     print("children: "+c.name+"\n")
        return
