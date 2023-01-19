class activateEndScreen:
    def __init__(self):
        self.name = "Action Loading Screen Deactivate"
        self.types = ["custom_event"]
        self.entity = []
        self.children = []

    def condition_to_act(self,data):
        if self.entity == None:
            return False
        return True

    def act(self,data):
        if self.condition_to_act(data):
            self.loop(data)
        return

    def loop(self,data):
        if data == self.entity.numLevels:
            self.entity.text_levelIndex = ""
            self.entity.text_loading = "Congratulations. You have completed all the levels!!!"
            self.entity.isGameOver = True
            self.entity.text_credits = "Made By : " \
                                        "Eric DiNicolantonio, Blake Pritchard and Siddhant Gupta"
            for c in self.children:
                c.act(True)
