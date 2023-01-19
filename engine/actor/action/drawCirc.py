import pygame

class drawCirc():
    def __init__(self):
        self.types = ["display child"]
        self.entity = None
        self.verbose = False
        self.name = "circle draw action"
        return

    def shouldAct(self,data):
        if self.entity == None:
            return False
        if self.entity.active == False:
            return False
        if data == None:
            return False
        return True

    def act(self,data):

        if self.shouldAct(data):
            self.draw(data)
            if self.verbose:
                print(self.name + " for " + self.entity.name)
        return

    def draw(self, screen):
        pygame.draw.circle(screen, self.entity.color, (self.entity.pos[0],self.entity.pos[1]), self.entity.r)
