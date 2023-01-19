import pygame as pg

class display():
    def __init__(self):
        self.types = ["display"]
        self.entity = None
        self.verbose = False
        self.name = "draw viewer act"
        self.children = []
        return

    def shouldAct(self,data):
        if self.entity == None:
            return False
        if data == True:
            return True
        if self.entity.active == False:
            return False
        if data == None:
            return False
        return True

    def act(self,data):
        if self.shouldAct(data):
            self.draw(data)
            if self.verbose:
                print("display called" )

            for c in self.children:
                c.act(data)
        return

    def draw(self, data):
        #Establish white background

        self.entity.screen.fill((0, 0, 0))

        return
