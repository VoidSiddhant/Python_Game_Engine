import pygame
class activateLoadingScreen:
    def __init__(self):
        self.name = "Action Loading Screen Activate"
        self.types = ["custom_event"]
        self.entity = []
        self.children = []
        self.verbose = False

    def condition_to_act(self,data):
        if self.entity == None:
            return False
        if data == self.entity.numLevels:
            return True
        return False

    def act(self,data):
        if self.condition_to_act(data):
            self.entity.active = True
            if data == self.entity.numLevels:
                self.entity.text_levelIndex = ""
            else:
                self.entity.text_levelIndex = data
            self.entity.startTime = pygame.time.get_ticks()
            if self.verbose:
                print("Activating Loading Screen..............")
        return
