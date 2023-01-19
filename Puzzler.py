import pygame as pg

import random

import engine.actor as act
import engine.play as pla
import engine.ui as ui
import engine.utility as ut
import engine.sound as snd
import engine.physics as phys
import engine.story as st

#import level data for use in constructing levels
from engine.story.entity.LevelData import allLevelData


##Game settings
WIDTH = 1280
HEIGHT = 720
BUTTONW = 30
BUTTONH = 30
NUMPARTICLES = 1
CIRCLERADIUS = 10
SPAWNWINDOW = [200,100]

#get number of levels from level data file
NUMLEVELS = len(allLevelData)-1


#locations for forces to be active. Negative value means force is active to the left
#of said value. positive is to the right. We want gravity and drag always
gravLoc = -WIDTH
dragLoc = -WIDTH


#generate our ball object
def makeCircles(x,y,n):
    circles = []
    #generate random location initially, will be set to level location later
    for i in range(0,n):
        xpos = random.randint(0,x)
        ypos = random.randint(HEIGHT/2-y,HEIGHT/2+y)
        c = [0,0,0]
        # generate random ball color for variety
        for j in range(0,3):
            c[j] = random.randint(0,255)
        circ = act.Circle(xpos, ypos, CIRCLERADIUS, c)
        circ.name = "circle "+ str(i)
        circ.addAction(act.drawCirc())
        circ.addAction(circlePick)
        display.children.append(circ.actions[0])
        circles.append(circ)
    return circles

def getParticles(input):
    particles = []
    onePart = phys.Particles()
    particles.append(onePart)

    #make a particle for each circle
    #add pick and put actions
    for i in range(0,len(input)):
        p = list(input[i].pos)
        v = [0,0,0]
        m = 1.0
        onePart.addParticle(p,v,m)

        pick = phys.pickPos(i)
        put = act.putPos()
        onePart.addAction(pick)
        pickVel = phys.pickVel(i)
        pickVel.children.append(restInc)


        input[i].addAction(put)
        pick.children.append(put)
        game_content.append(onePart)

    #set up and attach solvers to particle
    psolve = phys.solvePos()
    onePart.addAction(psolve)
    vsolve = phys.solveVel()
    vsolve.children.append(ga)
    vsolve.children.append(shoot_a)
    vsolve.children.append(da)
    vsolve.children.append(restRst)

    vsolve.children.append(pickVel)
    esolve = phys.solveEuler()
    esolve.dt = 0.1
    esolve.children.append(psolve)
    esolve.children.append(vsolve)
    esolve.types.append("loop")

    onePart.addAction(vsolve)
    onePart.addAction(esolve)

    #set up and attach window collider
    windcol = phys.RectCollider([CIRCLERADIUS,CIRCLERADIUS],[WIDTH-CIRCLERADIUS,HEIGHT-CIRCLERADIUS])
    inCollision = phys.insideRectColl()
    windcol.addAction(inCollision)
    psolve.children.append(inCollision)

    #set up and attach barrier colliders for levels
    collidergroup = phys.RectColliders([[[300, 300], [400, 400]], [[600, 600], [700, 700]]])
    colliderscollisions = phys.outsideRectsColl()
    collidergroup.addAction(colliderscollisions)
    psolve.children.append(colliderscollisions)

    #scuffed colliders
    particles.append(collidergroup)
    particles.append(windcol)

    return particles


###############################################################################
#                            Create Entites & Actions
###############################################################################

##Viewer Entites & actions
viewer = pla.Viewer(WIDTH, HEIGHT)
game_content = [viewer]

udV = pla.getViewUpdate()
display = pla.display()
closed = pla.windowClose()

# timers for each level, whole game, and tracking if ball is at rest
levelTimer = ut.Timer()
gameTimer = ut.Timer()
lTimeInc = ut.updateTimer()
gTimeInc = ut.updateTimer()
lTimeRst = ut.resetTimer()
dispLTimer = ut.displayTimer()
dispGTimer = ut.displayTimer()
dispGTimer.message = "Game completed in "
restTimer = ut.Timer(100)
restInc = ut.updateTimer()
restRst = ut.resetTimer()
restAlarm = ut.alarm()

#button entity and actions for full window "button"
booster = ui.Button((0,0,WIDTH,HEIGHT))
booster.verbose = False
bp = ui.pressButton()
bdp = ui.depressButton()


#mouse entity
mouse = ui.MousePos()
mousePick = ui.pickPos()
mouseMove = ui.mouseMoved()
shootPut = ui.putPos()
circlePick = ui.pickPos()

mPress = ui.toggleMouseHeld()

#check input action
check = pla.checkInput()
#set up force activators and deactivators
gravOn = phys.activateParticle(gravLoc)
gravOn.name = "gravOn"
gravOff = phys.deactivateParticle(gravLoc)
gravOff.name = "gravOff"

dragOn = phys.activateParticle(dragLoc)
dragOn.name = "dragOn"
dragOff = phys.deactivateParticle(dragLoc)
dragOff.name = "dragOff"

#line entity and actions
line = act.Line()
dline = act.drawLine()
lineOff = phys.deactivate()
lineOn = phys.activate()
linePick = ui.pickPos()
linePut = ui.putPos()
putLineStart = act.putStart()
putLineEnd = act.putEnd()


#set up gravity force
g = phys.ForceGravity()
g.gravity = [0.0,2.0]
ga = phys.gravityAct()

#set up drag force
d = phys.ForceDrag()
da = phys.dragAct()
d.dragK = -0.02

#set up shoot force
shoot = phys.ForceShoot()
shoot.active = False
shoot.name = "shoot force"
shoot_a = phys.shootAct()
shoot_a.name = "shoot force action"
shoot_a.dragK = 0.003
shootActive = phys.activate()
shootDeactive = phys.deactivate()
moving = phys.isMoving()
still = phys.isStill()


circles = makeCircles(SPAWNWINDOW[0], SPAWNWINDOW[1], NUMPARTICLES)
particles = getParticles(circles)

shoot.particles = particles[0]
particleunfreeze = phys.activate()

#set up win collider, will be reset each level
posx = 0
posy = 0
sizex = 100
sizey = 100
winzone = phys.RectCollider([posx,posy],[sizex,sizey])
winzone.color = (0, 255, 0)
winCollision = phys.winColl(particles[0])
winZoneDraw = act.drawRec()

#collider drawing action
drawcolliders = act.drawObstacles()


#Set up level tracker and build level
levelCounter = st.LevelCount(particles[0], winzone, particles[1], particles[2])
incrementlevelact = ut.increment()
buildLevel = st.buildLevel()


#Credit screen entity and actions
loadLevelEnt = ui.LoadingScreen(NUMLEVELS,(WIDTH/2 - 100,HEIGHT/2,10,20))
loadLevelEnt.active = False
loadLevelDrawA = ui.drawLoadingScreen()
loadLevelActivateA = ui.activateLoadingScreen()
loadLevelDeactivateA = ui.deactivateLoadingScreen()
endScreenActivate = ui.activateEndScreen()


###############################################################################
#                            Add Actions to Entities
###############################################################################
viewer.addAction(udV)
viewer.addAction(display)

# Connect level actions
loadLevelEnt.addAction(loadLevelActivateA)
loadLevelEnt.addAction(loadLevelDrawA)
loadLevelEnt.addAction(loadLevelDeactivateA)
loadLevelEnt.addAction(endScreenActivate)
levelCounter.addAction(incrementlevelact)
levelCounter.addAction(buildLevel)
levelCounter.addAction(incrementlevelact)

# Connect timer actions
levelTimer.addAction(lTimeInc)
levelTimer.addAction(lTimeRst)
levelTimer.addAction(dispLTimer)
gameTimer.addAction(gTimeInc)
gameTimer.addAction(dispGTimer)
restTimer.addAction(restInc)
restTimer.addAction(restRst)
restTimer.addAction(restAlarm)

# Connect particle actions
particles[0].addAction(particleunfreeze)
particles[1].addAction(drawcolliders)

# Connect line actions
line.addAction(linePut)
line.addAction(putLineStart)
line.addAction(putLineEnd)
line.addAction(lineOn)
line.addAction(lineOff)
line.addAction(dline)


#button actions
booster.addAction(bp)
booster.addAction(bdp)

# Connect shoot force actions
shoot.addAction(shootPut)
shoot.addAction(shootDeactive)
shoot.addAction(shootActive)
shoot.addAction(moving)
shoot.addAction(still)

# Connect mouse actions
mouse.addAction(mPress)
mouse.addAction(mouseMove)

#gravity actions
g.addAction(ga)
d.addAction(da)
shoot.addAction(shoot_a)

# Connect goal actions
winzone.addAction(winCollision)
winzone.addAction(winZoneDraw)



###############################################################################
#                            Adopt Children
###############################################################################
# Set drawing actions as children of display to draw after background
display.children.append(dline)
display.children.append(winZoneDraw)
display.children.append(drawcolliders)
display.children.append(loadLevelDrawA)

#button press children
# -get circle location
# -set mouse held
# -activate line
# -set line endpoint
bp.children.append(circlePick)
bp.children.append(mPress)
bp.children.append(lineOn)
bp.children.append(putLineEnd)

# Mouse motion Children
# -set line endpoint, turn line on
# -set line start point
mouseMove.children.append(putLineEnd)
linePut.children.append(lineOn)
circlePick.children.append(putLineStart)

# Button depress children
# -turn line off
# -set shoot force location
# -set mouse held off
bdp.children.append(lineOff)
bdp.children.append(shootPut)
bdp.children.append(mPress)

# Shooting children
# -put shoot force location activates shoot force
# -shoot deactivates after shooting
shootPut.children.append(shootActive)
shoot_a.children.append(shootDeactive)

#gravity and drag force action chilrden
ga.children.append(gravOn)
ga.children.append(gravOff)

da.children.append(dragOn)
da.children.append(dragOff)


#Win collision children
# -increment level
# -build next level
winCollision.children.append(incrementlevelact)
winCollision.children.append(buildLevel)

#increment children
# -activate loading screen(if last level)
# -show level timer value
# -activate end screen (if last level)
incrementlevelact.children.append(loadLevelActivateA)
incrementlevelact.children.append(dispLTimer)
incrementlevelact.children.append(endScreenActivate)

#end screen child: display game timer value
endScreenActivate.children.append(dispGTimer)

#timer children
# -after displaying level timer, reset level timer
# -after updating resting timer, check resting alarm
# -if resting alarm is triggered, set particle is still
# -if resting alarm is reset, set particle is moving
dispLTimer.children.append(lTimeRst)
restInc.children.append(restAlarm)
restAlarm.children.append(still)
restRst.children.append(moving)

# Build level children
# when you build a level, deactivate a loading screen if there is one
buildLevel.children.append(loadLevelDeactivateA)


###############################################################################
#                            Set up Content, Loop, & Run
###############################################################################
game_content.append(loadLevelEnt)
game_content.append(booster)
game_content.append(mouse)
game_content.append(gameTimer)
game_content.append(levelTimer)
game_content.append(restTimer)

game_content.append(g)
game_content.append(d)
game_content.append(shoot)

game_content.append(winzone)
game_content.append(particles[1])

game_looper = pla.Looper( game_content )
game_looper.addAction(check)
game_looper.addAction(pla.stopLoop())

#build first level
buildLevel.act(1)
game_looper.loop()
