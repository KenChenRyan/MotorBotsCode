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

#threads
#executor_fred = ThreadPoolExecutor(max_workers=2)

#functions
def drivePower(left_drive,right_drive,fwd,distance):
    if fwd == True:
        left_drive.run_until(100,distance)
        right_drive.run_until(-95,distance)
    else:
        left_drive.run_until(-100,distance)
        right_drive.run_until(95,distance)

# class LiftTrain:
#     def __init__():
        

# class DriveTrainPower:
#     def __init__(self,left,right,left_p,right_p):
#         self.leffDrive = left
#         self.rightDrive = right
#         self.left_power = left_p
#         self.right_power = right_p
#     def drive(fwd,distance):
#         if fwd == True:
#             self.leftDrive.run_until(self.left_power,distance)
#             self.rightDrive.run_until(-self.right_power,distance)
#         else:
#             self.leftDrive.run_until(-self.left_power,distance)
#             self.rightDrive.run_until(self.right_power,distance)

#main function
# drivePower(left_drive,right_drive,True,100)
# turn right
# dt.drive_until(100,20)
# dt.turn_until(80,-100)
# dt.drive_until(100, 488)
# #+1 point
# #go backwards
# dt.drive_until(-100, 380)
# #turn left
# dt.turn_until(80,90)
# dt.drive_until(100,799)
# dt.turn_until(80,-85)
# dt.drive_until(100,420)
# dt.drive_until(100,-450)
# dt.turn_until(100,85)
# dt.drive_until(100,700)
# dt.turn_until(100,-80)
# dt.drive_until(100,400)
print "Not thread"
hood = sys.thread_id()
print hood
sys.run_in_thread(print(hood))
sys.run_in_thread(drivePower(left_drive,right_drive,True,100))
sys.exit()
#sys.run_in_thread(print("Thread"))
# sys.run_in_thread(left_lift.run_until(100,50))
# sys.run_in_thread(right_lift.run_until(100,50))
#left_future = executor_fred.submit(left_lift.run_until(100,20))
#right_future = executor_fred.submit(right_lift.run_until(-100,20))
# class LiftTrain:
#     def __init__(self, leftLift, rightLift):
#         self.leftLift = leftLift
#         self.rightLeft = rightLift
#     def lift(power,distance):
#         self.leftLift.run(100)
#         self.rightLift.run(100)
    
jack = lambda x: x*x;

jack(8)
