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
    if fwd == True:
        left_drive.run(100,distance)
        right_drive.run(95,distance)
    else:
        left_drive.run(-100,distance)
        right_drive.run(-95,distance)
    sys.sleep(5)

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
drivePower(left_drive,right_drive,True,120)
# turn right
dt.turn_until(80,-56)
#Inital Lift raising
lift.raise_lift(50)
drivePower(left_drive,right_drive,True,488)
#+1 point
#go backwards
drivePower(left_drive,right_drive,False,40)
#turn left
dt.turn_until(80,56)
drivePower(left_drive,right_drive,True,30)
dt.turn_until(80,-56)
drivePower(left_drive,right_drive,True,30)
#Grabbing the double risers
claw.run_until(100,10)
lift.raise_lift(40)
dt.turn_until(100,-28)
lift.raise_lift(-10)
claw.run_raw_until(100,-10)
drivePower(left_drive,right_drive,False,30)

#move on to middle riser
dt.turn_until(100,84)
drivePower(left_drive,right_drive,True,300)
dt.turn_until(100,56)
drivePower(left_drive,right_drive,True,40)
dt.turn_until(100,-56)
drivePower(left_drive,right_drive,True,40)
dt.turn_until(100,-56)
drivePower(left_drive,right_drive,True,80)

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
