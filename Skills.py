# VEX IQ Python-Project
import sys
import vexiq
#region config
left_drive       = vexiq.Motor(1)
claw_motor       = vexiq.Motor(5)
left_lift_motor  = vexiq.Motor(6)
right_drive      = vexiq.Motor(7, True) # Reverse Polarity
right_lift_motor = vexiq.Motor(11, True) # Reverse Polarity
joystick         = vexiq.Joystick()
#endregion config
left_lift_motor.reset_position()
right_lift_motor.reset_position()
lift_max_height = 932 # this controls the max lift:
lift_min_height = -5
claw_motor.stall_timeout = 2
while True:
    #Controls Drive
    left_lift_positon = left_lift_motor.position()
    right_lift_position = right_lift_motor.position()
    #Prints to screen
    vexiq.lcd_write("Left lift pos: "+str(left_lift_positon))
    vexiq.lcd_write("Righ lift pos: "+str(right_lift_position),2)
    #Controls Tank Drive
    left_drive.run(joystick.axisA())
    right_drive.run(joystick.axisD())
    #controls lift up
    if joystick.bLup() and left_lift_positon < lift_max_height:
        left_lift_motor.run(100)
        right_lift_motor.run(100)
    #controls lift down
    elif joystick.bLdown():
        left_lift_motor.run(-100)
        right_lift_motor.run(-100)
    #controls lift 
    else:
        left_lift_motor.hold()
        right_lift_motor.hold()
    #controls claw
    if claw_motor.stalled():
        vexiq.lcd_write("claw_motor stalling",3)
        claw_motor.run(0)
    if joystick.bRup():
        claw_motor.run(100)
    elif joystick.bRdown():
        claw_motor.run(-100)
    else:
        claw_motor.hold()
