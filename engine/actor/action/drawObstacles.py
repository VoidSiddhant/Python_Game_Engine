import pygame

class drawObstacles():
    def __init__(self):
        self.types = ["display child"]
        self.entity = None
        self.verbose = False
        self.name = "draw_obstacles"
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
        for collider in self.entity.colliders:
            r = pygame.Rect(collider[0][0], collider[0][1], collider[1][0]-collider[0][0], collider[1][1]-collider[0][1])
            pygame.draw.rect(screen, (255, 255, 255), r)

        return
