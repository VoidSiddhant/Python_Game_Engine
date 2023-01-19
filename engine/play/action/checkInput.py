import pygame as pg

class checkInput:
  def __init__(self, name = "Event input getter"):
    self.types = ["event"]
    self.entity = None
    self.click = False
    self.name = name
    self.verbose = False
    self.children = []
    return

  def shouldAct(self,data):
    if self.entity == None:
      return False
    if self.entity.active == False:
      return False
    return True

  def act(self, data):

    if self.shouldAct( data):
        events=pg.event.get()
        self.entity.events = events

        #print out if a key is pressed
        for e in events:
            if e.type == pg.KEYDOWN:
                guess = str(pg.key.name(e.key))
                if events != []:
                    print(guess + " key pressed")
                    # self.key = guess

        #if window is closed, will set Loop to false
            else:
                if e.type == pg.QUIT:
                    self.entity.active = False


        for c in self.children:
            if self.click:
              self.click = False

        if self.verbose:
          print(self.name +"triggered for "+ self.entity.name)

    return
