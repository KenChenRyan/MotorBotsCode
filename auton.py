# VEX IQ Python-Project
import sys
import vexiq

#region config
claw        = vexiq.Motor(1)
left_lift   = vexiq.Motor(2, True) # Reverse Polarity
left_drive  = vexiq.Motor(6)
right_lift  = vexiq.Motor(8)
right_drive = vexiq.Motor(12, True) # Reverse Polarity

import drivetrain
dt          = drivetrain.Drivetrain(left_drive, right_drive, 200, 180)
#endregion config

#functions
def drivePower(left_drive,right_drive,fwd,distance):
    time = 1;
    temp_distance = distance;
    if distance > 300:
        while temp_distance > 300:
            time = time + 0.5;
            temp_distance = temp_distance - 300;
    if fwd == True:
        left_drive.run(100,distance)
        right_drive.run(85,distance)
    else:
        left_drive.run(-100,distance)
        right_drive.run(-85,distance)
    sys.sleep(time)

class LiftTrain:
    def __init__(self,left_motor,right_motor):
        self.left = left_motor
        self.right = right_motor
    def raise_lift(self,height):
        self.left.run(100,height)
        self.right.run(100,height)
        sys.sleep(0.25)

lift = LiftTrain(left_lift,right_lift)
#main function
#move forward
drivePower(left_drive,right_drive,True,160)
# turn right
dt.turn_until(80,-65)
#Inital Lift raising
lift.raise_lift(100)
drivePower(left_drive,right_drive,True,510)
#+1 point


#go for middle risers
#go backwards
drivePower(left_drive,right_drive,False,345)
#turn left
dt.turn_until(80,60)
drivePower(left_drive,right_drive,True,790)
dt.turn_until(80,-52)
drivePower(left_drive,right_drive,True,370)

#move on to last set of purple
drivePower(left_drive,right_drive,False,320)
dt.turn_until(100,55)
drivePower(left_drive,right_drive,True, 850)
dt.turn_until(100,-50)
drivePower(left_drive,right_drive,True,300)
drivePower(left_drive,right_drive,False,200)


#move on to last set of purple
drivePower(left_drive,right_drive,False,-40)
#turn left to face the position of last set of risers
dt.turn_until(100,56)
drivePower(left_drive,right_drive,True,200)
dt.turn_until(100,-56)
drivePower(left_drive,right_drive,True,30)
claw.run_raw_until(100,10)
lift.raise_lift(40)
drivePower(left_drive,right_drive,False,30)
dt.turn_until(100,112)
drivePower(left_drive,right_drive,True,30)
dt.turn_until(100,-56)
drivePower(left_drive,right_drive,True,30)
dt.turn_until(100,-56)
drivePower(left_drive,right_drive,True,80)
