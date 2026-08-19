import mcpi.minecraft as minecraft
import mcpi.block as block
import datetime

ballPosX = 0
ballPosY = 1
ballPosZ = 0
yelloScore = 0
blueScore = 0

preTime = 0

def buildField():
	mc.setBlocks (-29,0,-19,29,15,19,block.AIR.id)
	
	mc.setBlocks(-29,0,-19,29,0,19,block.WOOL.id,0)
	mc.setBlocks(-28,0,-18,28,0,18,block.WOOL.id,13)
	mc.setBlocks(ballPosX,0,-19,ballPosX,0,19,block.WOOL.id,0)
	mc.setBlocks(-29,0,-8,-18,0,8,block.WOOL.id,0)
	mc.setBlocks(29,0,-8,-18,0,8,block.WOOL.id,0)
	mc.setBlocks(-28,0,-7,-19,0,7,block.WOOL.id,13)
	mc.serBlocks(28,0,-7,19,0,7,block.WOOL.id,13)

	mc.setBlocks(29,3,-5,29,3,5,block.WOOL.id,4)
	mc.setBlocks(-29,3,-5,-29,3,5,block.WOOL.id,4)

	showYelloScore(29,5,-1,yelloScore)
	showBlueScore(-29,5,1,blueScore)

def showYelloScore(baseX,baseY,baseZ,num):
        if num >= 0 and num <= 9 :
                FNAME = "num"+str(num)+".csv"
                f = open(FNAME,"r")
                offsetY = 4
                offsetZ = 0
            for line in f.readlines ():
                 data = line.split(",")
                 for cell in data ：
                        if cell == "1":
                                 mc.setBlocks(baseX,baseY+offsetY,baseZ+offsetZ,block.WOOL.id,4)
                         else:
                                 mc.setBlocks(baseX,baseY+offsetY,baseZ+offsetZ,block.AIR.id)

                                 offsetZ = offsetZ + 1

                 offsetY = offsetY - 1
                 offsetZ = 0

def showBlueScore(baseX,baseY,baseZ,num):
        if num >= 0 and num <= 9 :
                FNAME = "num"+str(num)+".csv"
                f = open(FNAME,"r")
                offsetY = 4
                offsetZ = 0
                for line in f.readlines():
                        data = line.split(",")
                        for cell in data:
                               if  cell == "1":  
                                mc.setBlocks(baseX,baseY+offsetY,baseZ+offsetZ,block.WOOL.id,11)
                        else:
                                mc.setBlocks(baseX,baseY+offsetY,baseZ+offsetZ,block.AIR.id)

                                offsetZ = offsetZ - 1


                offsetY = offsetY -1
                offsetZ = 0

def showNum(baseX,baseY,baseZ,num) :
        if num >= 0 and num <= 9 :
                FNAME = "num"+str(num)+".csv"
                f = open(FNAME,"r")
                offsetY = 4
                offsetZ = 0
                for line in f.readlines():
                        data = line.split(",")
                        for cell in data:
                               if  cell == "1":  
                                mc.setBlocks(baseX,baseY+offsetY,baseZ+offsetZ,block.WOOL.id,15)
                        else:
                                mc.setBlocks(baseX,baseY+offsetY,baseZ+offsetZ,block.AIR.id)

                                offsetX = offsetX + 1


                offsetY = offsetY -1
                offsetX = 0


mc = minecraft.Minecraft.create()

mc.postToChat("Welcome to new world")

buildField()

while True:
        if mc.getBlock(ballPosX,ballPosY,ballPosZ) == block.AIR.id:
                mc.setBlocks(ballPosX,ballPosY,ballPosZ,block.WOOL.id,1)

        timeNow = datetime.datetime.now()
        if preTime ! =timeNow.minute:
                preTime = timeNow.minute
        if timeNow.hour/10 ! = 0:
                showNum(-8,3,-20,timeNow.hour/10)
        else:
                mc.setBlocks(-8,3,-20,-6,7,-20,block.AIR.id)
        showNum(-4,3,-20,timeNow.hour%10)
        mc.setBlocks(0,4,-20,block.WOOL.id,15)
        mc.setBlocks(0,6,-20,block.WOOL.id,15)
        showNum(2,3,-20,timeNow.minute/10)
        showNum(6,3,-20,timeNow.minute%10)

    events = mc.events.pollBlockHits()

    for e in events:
            if e.pos.x == ballPosX and e.pos.y == ballPosY and e.pos.z == ballPosZ:

                    if e.face == 5:
                            mc.setBlocks(e.pos.x,e.pos.y,e.pos.z,block.AIR.id)
                            mc.setBlocks(e.pos.x-1,e.pos.y,e.pos.z,block.WOOL.id,1)
                            ballPosX = ballPosX -1
                    if e.face == 3:
                            mc.setBlocks(e.pos.x,e.pos.y,e.pos.z,block.AIR.id)
                            mc.setBlocks(e.pos.x,e.pos.y,e.pos.z,block.WOOL.id,1)
                            ballPosZ = ballPosZ -1
                    if e.face == 4:
                            mc.setBlocks(e.pos.x,e.pos.y,e.pos.z,block.AIR.id)
                            mc.setBlocks(e.pos.x+1,e.pos.y,e.pos.z,block.WOOL.id,1)
                            ballPosX = ballPosX +1
                    if e.face == 2:
                            mc.setBlocks(e.pos.x,e.pos.y,e.pos.z,block.AIR.id)
                            mc.setBlocks(e.pos.x,e.pos.y,e.pos.z,block.WOOL.id,1)
                            ballPosZ = ballPosZ +1


    if ballPosX <-29 or ballPosX > 29 or ballPosZ <-19 or ballPosZ > 19:
            mc.setBlocks(ballPosX,ballPosY,ballPosZ,block.TNT.id,1)
            if ballPosZ >= -5 and ballPosZ <= 5 :
                    mc.postToChat('GOAL')
                    if ballPosX <-29 :
                            yelloScore = yelloScore + 1

                    if ballPosX > 29 :
                            blueScore = blueScore + 1

                    mc.PostToChat('YELLO:' + str(yelloScore) + ' BLUE:'+str(blueScore))
            else:
                    mc.posToChat('OUT')
            ballPosX = yelloScore - blueScore
            if ballPosX > 15 :
                    ballPosX = 15
            if ballPosX < -15 :
                    ballPosX = -15
            ballPosZ = 0
            buildField()
