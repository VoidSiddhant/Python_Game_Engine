class Button:
    def __init__(self, bounds=(0,0,10,20), color=[128, 128, 128], name="button"):
        self.x = bounds[0]
        self.y = bounds[1]
        self.w = bounds[2]
        self.h = bounds[3]
        self.color = color            # (r,g,b)
        #self.message = msg            # Member variable for the message in a message button
        self.template = None          # Member variable for the image template in a template button
        self.actions = []
        self.name = name
        self.verbose = False
        self.active = True
        return

    def addAction(self, a):
        a.entity = self
        self.actions.append(a)
        return

    # Check whether a position is inside the bounds
    def is_inside( self, pos):
        if pos[0] < self.x:
            return False
        if pos[0] > self.w + self.x:
            return False
        if pos[1] < self.y:
            return False
        if pos[1] > self.h + self.y:
            return False
        return True
