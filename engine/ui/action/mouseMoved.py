from pygame.locals import *

class mouseMoved:
    def __init__(self):
        self.types = ["event"]
        self.entity = None
        self.name = "update end of line action"
        self.children = []
        self.verbose = False

    def shouldAct(self, event):
        if self.entity == None:
            return False
        if self.entity.active == False:
            return False
        if self.entity.isLeftPressed == False:
            return False
        if event == False:
            return False
        for e in event:
            if e.type == MOUSEMOTION and e.buttons[0] == 1:
                # check whether the mouse button is down inside the button area
                return [True,e.pos]
        return False

    def act(self, event):

        data = self.shouldAct(event)
        # self.shouldAct(event) != False:

        if data:

            for c in self.children:
                c.act(data)
            if self.verbose:
                print( "mousemove" + str(self.entity.pos))
                # for c in self.children:
                #     print("children: "+c.name+"\n")
        return
