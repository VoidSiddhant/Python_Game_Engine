import pygame
class deactivateLoadingScreen:
    def __init__(self):
        self.name = "Action Loading Screen Deactivate"
        self.types = ["loop"]
        self.entity = []
        self.children = []

    def condition_to_act(self,data):
        if self.entity == None:
            return False
        return True

    def act(self,data):
        if self.condition_to_act(data):
            self.loop()
        return

    def loop(self):
        timElapsed = pygame.time.get_ticks() - self.entity.startTime
        if timElapsed > 2000 and self.entity.isGameOver == False:
            self.entity.active = False
