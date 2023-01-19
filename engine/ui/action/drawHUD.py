import pygame as pg

class drawHUD:
    def __init__(self, name = "Basic Action Name"):
        self.types = ["display child"]
        self.entity = None
        self.name = name
        self.verbose = False
        self.children = []
        return

    def shouldAct(self,data):
        if self.entity == None:
            return False
        if self.entity.active == False:
            return False

        #check other things

        return True

    def act(self, data):
        if self.shouldAct(data):
            self.entity.temp = data

            font = pg.font.Font('freesansbold.ttf', 18)

            #retrieve and display the two strings in HUD
            successString = self.entity.sMsg
            msg = font.render(successString,True, (255,255,255))
            bounds = msg.get_rect()
            bounds.center=(100,20)
            data.blit(msg, bounds)

            totalString = self.entity.tMsg
            msg = font.render(totalString,True, (255,255,255))
            bounds = msg.get_rect()
            bounds.center=(100,50)
            data.blit(msg, bounds)


            for c in self.children:
                c.act(data)

            if self.verbose:
                print(self.name +"triggered for "+ self.entity.name)
