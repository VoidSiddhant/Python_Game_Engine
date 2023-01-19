#LEVEL BUiLDING
# level start is the start location of the ball 
# level goal is the level goal
# lcollider group is a list of all colliders to be built in the level
#LEVEL 1 (BIG BLOCK GOAL)
level1start = [40, 710]
level1goal = [[400, 240],[880,720]]
collidergroup1 = []

#LEVEL 2 (ONE WALL)
level2start = [40, 710]
level2goal = [[1160, 600],[1280,720]]
collidergroup2 = [[[600,300],[680,720]]]

#LEVEL 3 (HARDER VERSION OF LEVEL 2)
level3start = [40, 710]
level3goal = [[1160, 600],[1280,720]]
collidergroup3 = [[[600,300],[680,720]], [[800, 300],[1280, 360]]]

#LEVEL 4 (HARDER VERSION OF LEVEL 3)
level4start = [40, 710]
level4goal = [[1160, 600],[1280,720]]
collidergroup4 = [[[600,300],[680,720]], [[800, 300],[1280, 360]], [[600,0],[680,200]]]

#LEVEL 5 (ONE WALL WITH HOLE)
level5start = [40, 710]
level5goal = [[1160, 600],[1280,720]]
collidergroup5 = [[[600,420],[680,720]], [[600, 0],[680, 300]]]

#LEVEL 6 (TWO WALLS WITH HOLES)
level6start = [40, 710]
level6goal = [[1160, 600],[1280,720]]
collidergroup6 = [[[400,300],[480,720]], [[400, 0],[480, 200]], [[800,600],[880,720]], [[800, 0],[880, 500]]]

#LEVEL 7 (THREE WALLS WITH HOLES)
level7start = [40, 710]
level7goal = [[1160, 600],[1280,720]]
collidergroup7 = [[[300,600],[380,720]], [[300, 0],[380, 500]], [[900,200],[980,720]], [[900, 0],[980, 100]], [[600,420],[680,720]], [[600, 0],[680, 300]]]

#LEVEL 8 (WALLBOUNCE 1x)
level8start = [640, 710]
level8goal = [[540, 0],[740, 200]]
collidergroup8 = [[[520, 200],[760, 280]],[[440,0],[480,400]],[[800,0],[840,400]]]

#LEVEL 9 (WALLBOUNCE 2x)
level9start = [640, 710]
level9goal = [[540, 0],[740, 200]]
collidergroup9 = [[[520, 200],[760, 240]],[[440,0],[480,400]],[[800,0],[840,400]], [[520, 360],[760, 400]]]

#LEVEL 10 (TEETH)
level10start = [40, 710]
level10goal = [[1160, 600],[1280,720]]
collidergroup10 = [[[300,520],[380,720]], [[300, 0],[380, 200]], [[900,520],[980,720]], [[900, 0],[980, 200]], [[600,520],[680,720]], [[600, 0],[680, 200]]]

#LEVEL 11 (GOAL WITH HOLE IN IT)
level11start = [40, 710]
level11goal = [[1000, 600],[1120,720]]
collidergroup11 = [[[920,520],[1000,720]], [[1120,520],[1200,720]], [[1000, 520], [1040, 600]], [[1080, 520], [1120, 600]]]

#LEVEL 12 (TWO HALLWAYS)
level12start = [40, 710]
level12goal = [[40, 220],[160,390]]
collidergroup12 = [[[0, 330],[1080, 390]]]

#LEVEL 13 (THREE HALLWAYS)
level13start = [40, 710]
level13goal = [[1120, 80],[1240,200]]
collidergroup13 = [[[200, 200],[1280, 280]], [[0, 440],[1080, 520]]]

#LEVEL 14 (VERTICAL SNAKE)
level14start = [40, 710]
level14goal = [[1000, 60],[1160,200]]
collidergroup14 = [[[400,200],[480,720]], [[800,0],[880,520]]]

#LEVEL 15 (SMALL TARGET)
level15start = [40, 710]
level15goal = [[630, 230],[650,250]]
collidergroup15 = []

#LEVEL 16 (HOLE IN WALL LARGE)
level16start = [40, 710]
level16goal = [[1040, 240],[1280, 320]]
collidergroup16 = [[[1040,0],[1280,240]], [[1040,320],[1280,720]]]

#LEVEL 17 (HOLE IN WALL SMALL)
level17start = [40, 710]
level17goal = [[1040, 260],[1280, 300]]
collidergroup17 = [[[1040,0],[1280,260]], [[1040,300],[1280,720]]]

#LEVEL 18 (HOLE IN WALL LARGE WITH OBSTACLE)
level18start = [40, 710]
level18goal = [[1040, 240],[1280, 320]]
collidergroup18 = [[[1040,0],[1280,240]], [[1040,320],[1280,720]], [[640 ,200], [880 , 600]]]

#LEVEL 19 (HOLE IN WALL SMALL WITH OBSTACLE)
level19start = [40, 710]
level19goal = [[1040, 260],[1280, 300]]
collidergroup19 = [[[1040,0],[1280,260]], [[1040,300],[1280,720]], [[640 ,200], [920 , 540]]]

#LEVEL 20 (OPEN PLATFORM LOW)
level20start = [40, 710]
level20goal = [[620, 300],[660, 340]]
collidergroup20 = [[[620,340],[660,720]], [[580,340],[700,380]]]

#LEVEL 21 (OPEN PLATFORM HIGH)
level21start = [40, 710]
level21goal = [[620, 200],[660, 240]]
collidergroup21 = [[[620,240],[660,720]], [[580,240],[700,280]]]

#LEVEL 22 (CLOSED PLATFORM LOW)
level22start = [40, 710]
level22goal = [[620, 300],[660, 340]]
collidergroup22 = [[[620,340],[660,720]], [[580,340],[700,380]], [[580,260],[700,300]]]

#LEVEL 23 (CLOSED PLATFORM HIGH)
level23start = [40, 710]
level23goal = [[620, 200],[660, 240]]
collidergroup23 = [[[620,240],[660,720]], [[580,240],[700,280]], [[580,160],[700,200]]]

level24start = [46,710]
level24goal = [[985,300],[1020,320]]
collidergroup24 = [[940,300],[985,320]],[[940,320],[1020,340]],[[940,280],[960,300]],[[1020,265],[1040,340]],[[1000,245],[1040,265]]

#END LEVEL. ALWAYS INCLUDE FOR TO PREVENT UNNECESSARY WINSTREAKS
endLevelStart = [40, 710]
endLevelGoal = [[620, 300],[660, 340]]
collidergroupEnd = []

allLevelData = [[level1start, level1goal, collidergroup1],
[level2start, level2goal, collidergroup2],
[level3start, level3goal, collidergroup3],
[level10start, level10goal, collidergroup10],
[level5start, level5goal, collidergroup5],
[level4start, level4goal, collidergroup4],
[level6start, level6goal, collidergroup6],
[level7start, level7goal, collidergroup7],
[level8start, level8goal, collidergroup8],
[level9start, level9goal, collidergroup9],
[level11start, level11goal, collidergroup11],
[level15start, level15goal, collidergroup15],
[level16start, level16goal, collidergroup16],
[level17start, level17goal, collidergroup17],
[level20start, level20goal, collidergroup20],
[level21start, level21goal, collidergroup21],
[level12start, level12goal, collidergroup12],
[level13start, level13goal, collidergroup13],
[level14start, level14goal, collidergroup14],
[level22start, level22goal, collidergroup22],
[level23start, level23goal, collidergroup23],
[level18start, level18goal, collidergroup18],
[level19start, level19goal, collidergroup19],
[level24start, level24goal, collidergroup24],
[endLevelStart, endLevelGoal, collidergroupEnd]]
