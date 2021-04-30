# VEX IQ Python-Project
import sys
import vexiq
#region config
claw        = vexiq.Motor(1)
left_lift   = vexiq.Motor(2, True) # Reverse Polarity
left_drive  = vexiq.Motor(6)
right_lift  = vexiq.Motor(8)
right_drive = vexiq.Motor(12, True) # Reverse Polarity
joystick    = vexiq.Joystick()
#endregion config
claw.reset_position()
while True:
    #Controls Drive
    left_lift_positon = left_lift.position()
    right_lift_position = right_lift.position()
    #Prints to screen
    vexiq.lcd_write("Left lift pos: "+str(left_lift_positon))
    vexiq.lcd_write("Righ lift pos: "+str(right_lift_position),2)
    #Controls Tank Drive
    left_drive.run(joystick.axisA())
    right_drive.run(joystick.axisD())
    #controls lift up
    if joystick.bLup():
        left_lift.run(100)
        right_lift.run(100)
    #controls lift down
    elif joystick.bLdown():
        left_lift.run(-100)
        right_lift.run(-100)
    #controls lift 
    else:
        left_lift.hold()
        right_lift.hold()
    #controls claw
    if joystick.bRup():
        claw.run(100)
    elif joystick.bRdown():
        claw.run(-100)
    else:
        claw.hold()
