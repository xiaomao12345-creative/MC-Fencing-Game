# MC Fencing Game
This is the minecraft fencing game  
Please run main.py while running mc 


Partial code:  
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
        showNum(6,3,-20,timeNow.minute%10  

Welcome to download and use  
This took me a long time, can you give it a star?  
