import pygame
class drawLoadingScreen:
    def __init__(self,fontStyle = "Arial",fontSize = 20):
        self.name = "Action Loading Screen Draw"
        self.types = ["display_child"]
        self.drawLayer = 1
        self.entity = []
        self.children = []
        self.fontSize = fontSize
        self.fontStyle = fontStyle
        self.font = pygame.font.SysFont(fontStyle,fontSize)
        self.position = pygame.math.Vector2(0,0)
        return

    def SetPosition(self, font_pos):
        self.position = font_pos
        return

    def insert_children(self,a):
        self.children.append(a)

    def condition_to_act(self,data):
        if self.entity == None:
            return False
        if self.entity.active == False:
            return False

        return True

    def act(self,data):
        if self.condition_to_act(data):
            self.draw(data)

        return

    def draw(self,screen):
        if screen != None:
            #draw a fullscreen rect
            pygame.draw.rect(screen, (0, 0, 0), (0,0,1280,720))
            #draw font

            textBlit = self.font.render(str(self.entity.text_loading) + str(self.entity.text_levelIndex),True,[255,255,255])
            screen.blit(textBlit,(self.entity.bounds[0] + self.position.x - 100, self.entity.bounds[1] + self.position.y))
            textBlit = self.font.render(self.entity.text_credits,True,[255,255,255])
            screen.blit(textBlit,(self.entity.bounds[0] + self.position.x - 100, self.entity.bounds[1] + self.position.y+50))
