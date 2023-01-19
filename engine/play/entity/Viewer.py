import pygame as pg

class Viewer:
    def __init__(self, w=1280, h=720, t="Whackbox"):
        self.w = w
        self.h = h
        self.title = t
        self.screen = None
        # self.bg = None
        self.actions = []
        self.name = "Viewer"
        self.active = True
        self.update = True


        #initialize pygame
        pg.init()
        self.screen = pg.display.set_mode((self.w ,self.h))
        pg.display.set_caption(self.name)
        return

    def addAction(self, a):
        self.actions.append(a)
        a.entity = self
        return
