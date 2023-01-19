import pygame

class drawRec():
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
                print("drawing box "+self.name+" activation should be "+str(self.entity.active))
        return

    def draw(self, screen):

        r = pygame.Rect(self.entity.ll[0], self.entity.ll[1], self.entity.ur[0]-self.entity.ll[0], self.entity.ur[1]-self.entity.ll[1])
        pygame.draw.rect(screen, self.entity.color, r)

        return
