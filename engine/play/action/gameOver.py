class gameOver:
  def __init__(self, name = "gameOver action"):
    self.types = ["event"]
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


    return False
    #check other things

    # return False

  def act(self, data):
    if self.shouldAct(data):
        if (self.entity.correct == len(self.entity.word.letters)):
            self.entity.endMsg.letters[-1].letter = ")"
        for i in range(0,len(self.entity.endMsg.letters)):
            self.entity.endMsg.activity[i] = 2
        for i in range(0,len(self.entity.word.letters)):
            self.entity.word.activity[i] = 2
    #action specific stuff

    for c in self.children:
        c.act(data)

    if self.verbose:
        print(self.name +"triggered for "+ self.entity.name)

    return
