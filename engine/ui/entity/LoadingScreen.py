class LoadingScreen:
    def __init__(self,nL = 2, bounds=(0,0,10,20),color=(255,255,255),name= "Loading Screen"):
        self.actions = []
        self.name = name
        self.color = color
        self.bounds = bounds
        self.active = True
        self.text_loading = "Loading Level........."
        self.text_credits = "Made by Eric DiNicolantonio, Blake Pritchard, Siddhant Gupta"
        self.text_levelIndex = "0"
        self.numLevels = nL
        self.isGameOver = False
        self.startTime = 0
        return

    def addAction(self,a):
        a.entity = self
        self.actions.append(a)
        return

# class LoadingScreenActivate:
#     def __init__(self):
#         self.name = "Action Loading Screen Activate"
#         self.types = ["custom_event"]
#         self.entity = []
#         self.children = []
#
#     def condition_to_act(self,data):
#         if self.entity == None:
#             return False
#         return True
#
#     def act(self,data):
#         if self.condition_to_act(data):
#             self.entity.active = True
#             print("Activating Loading Screen..............")
#         return
#
# class LoadingScreenDeactivate:
#     def __init__(self):
#         self.name = "Action Loading Screen Deactivate"
#         self.types = ["custom_event"]
#         self.entity = []
#         self.children = []
#
#     def condition_to_act(self,data):
#         if self.entity == None:
#             return False
#         return True
#
#     def act(self,data):
#         if self.condition_to_act(data):
#             print("Deactivating Loading Screen..............")
#             self.entity.active = False
#         return
#
