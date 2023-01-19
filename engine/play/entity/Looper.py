import pygame as pg

class Looper():
  def __init__(self,c):
    self.active = True
    self.content = c
    self.entity = None
    self.events = []
    self.dActs = []
    self.lActs = []
    self.eActs = []
    self.pActs = []
    self.fActs = []
    self.posActs = []
    self.verbose = False
    self.actions = []
    self.name = "Loop Entity"


    for c in self.content:
        for a in c.actions:
            # print(a.name + "in content, L21")
            if "loop" in a.types:
                self.lActs.append(a)
            elif "event" in a.types:
                self.eActs.append(a)
            elif "display" in a.types:
                self.dActs.append(a)
            elif "physics" in a.types:
                self.pActs.append(a)
            elif "position" in a.types:
                self.posActs.append(a)
            elif "force" in a.types:
                self.fActs.append(a)
            else:
                self.actions.append(a)
    return

  def addAction(self, a):
    a.entity = self
    # print(a.name + "added, L40")
    if "loop" in a.types:
        self.lActs.append(a)
    elif "event" in a.types:
        self.eActs.append(a)
    elif "display" in a.types:
        self.dActs.append(a)
    elif "physics" in a.types:
        self.pActs.append(a)
    elif "position" in a.types:
        self.posActs.append(a)
    elif "force" in a.types:
        self.fActs.append(a)
    else:
        self.actions.append(a)
    return

  def loop(self):
    while self.active:
        # if self.events !=[]:
        #     for e in self.events:
        #         print(e.type)


        for pa in self.posActs:
            if self.events !=[] and self.verbose:
                print("PA: "+pa.name)
            pa.act("bl")

            # print(pa.name)

        for ea in self.eActs:
            if self.events !=[] and self.verbose:
                print("EA: "+ ea.name)
            ea.act(self.events) #check input, should update self.events[], check if something has happened
        if self.events !=[] and self.verbose:
            print(self.events)


        for la in self.lActs:
            if self.events !=[] and self.verbose:
                print("LA: "+ la.name)
            la.act(self.events) #do all loop things (calculating position, )

        # print("pre loop blit")
        # self.content[0].screen.fill((0, 0, 0))
        for da in self.dActs:
            if self.events !=[] and self.verbose:
                print("DA: "+da.name)

            da.act(self.content[0].screen) #do all display actions after things have been changed
        if self.events !=[] and self.verbose:
            print("\n")
        pg.display.flip()

        # self.content[0].active = False
        # raise Exception("End one loop")


    return
