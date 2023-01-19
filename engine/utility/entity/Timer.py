import pygame as pg
class Timer:
    def __init__(self, t = 5, name = "Timer" ):
        self.actions = []
        self.name = name
        self.startTime = pg.time.get_ticks()
        self.currTime = 0
        self.alarmVal = t
        self.verbose = False
        self.active = True
        return

    def addAction(self,a):
          a.entity = self
          self.actions.append(a)
          return

    def tick(self):
        self.currTime = pg.time.get_ticks()
        if self.verbose:
            print(self.currTime - self.startTime)

    def elapsedTime(self):
        return self.currTime - self.startTime
