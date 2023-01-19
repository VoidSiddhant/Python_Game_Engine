import pygame

class drawButton():
    def __init__(self):
        self.types = ["display child"]
        self.entity = None
        self.verbose = False
        self.name = "draw_rect_button_action"
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
        bounds = (self.entity.x, self.entity.y, self.entity.w, self.entity.h)
        pygame.draw.rect(screen, self.entity.color, bounds )
        return
