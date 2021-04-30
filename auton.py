# VEX IQ Python-Project
import sys
import vexiq

#region config
left_lift_motor  = vexiq.Motor(2)
claw_motor       = vexiq.Motor(3)
left_drive       = vexiq.Motor(6)
right_lift_motor = vexiq.Motor(8, True) # Reverse Polarity
right_drive      = vexiq.Motor(12, True) # Reverse Polarity

import drivetrain
dt          = drivetrain.Drivetrain(left_drive, right_drive, 200, 180)
#endregion config

#main function
drivePower(left_drive,right_drive,True,100)
lift = LiftTrain(left_lift_motor,right_lift_motor)
# turn right
dt.drive_until(100,20)
dt.turn_until(80,-100)
dt.drive_until(100, 488)
#+1 point
#go backwards
dt.drive_until(-100, 380)
#turn left
dt.turn_until(80,90)
dt.drive_until(100,799)
dt.turn_until(80,-85)
dt.drive_until(100,420)
dt.drive_until(100,-450)
dt.turn_until(100,85)
dt.drive_until(100,700)
dt.turn_until(100,-80)
dt.drive_until(100,400)
