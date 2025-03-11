# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       yulania                                                      #
# 	Created:      3/6/2025, 1:26:01 AM                                         #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

brain = Brain()
controller = Controller()

frontLeftMotor = Motor(Ports.PORT13, GearSetting.RATIO_6_1, True)
topFrontLeftMotor = Motor(Ports.PORT14, GearSetting.RATIO_6_1, False)
backLeftMotor = Motor(Ports.PORT11, GearSetting.RATIO_6_1, True)
topBackLeftMotor = Motor(Ports.PORT12, GearSetting.RATIO_6_1, False)

frontRightMotor = Motor(Ports.PORT3, GearSetting.RATIO_6_1, True)
topFrontRightMotor = Motor(Ports.PORT4, GearSetting.RATIO_6_1, False)
backRightMotor = Motor(Ports.PORT1, GearSetting.RATIO_6_1,True)
topBackRightMotor = Motor(Ports.PORT2, GearSetting.RATIO_6_1, False)

leftMotors = MotorGroup(frontLeftMotor, topFrontLeftMotor, backLeftMotor, topBackLeftMotor)
rightMotors = MotorGroup(frontRightMotor, topFrontRightMotor, backRightMotor, topBackRightMotor)

allMotors = MotorGroup(frontLeftMotor, topFrontLeftMotor, backLeftMotor, topBackLeftMotor, frontRightMotor, topFrontRightMotor, backRightMotor, topBackRightMotor)


intake = Motor(Ports.PORT17, GearSetting.RATIO_18_1, False)
intake.set_velocity(200, RPM)

frontIntake = Motor(Ports.PORT18)

digOut = DigitalOut(brain.three_wire_port.g)
digOut.set(True)


def autonomous():
    brain.screen.clear_screen()
    brain.screen.print("autonomous code")
    # place automonous code here

def user_control():
    brain.screen.clear_screen()
    brain.screen.print("driver control")
    # place driver control in this while loop
    while True:
        maxRPM = 600
        ForwardBackwardJS = (controller.axis3.position() / 100) * maxRPM
        TurningJS = (controller.axis1.position() / 100) * maxRPM

        leftJSspeed = ForwardBackwardJS + TurningJS
        rightJSspeed = TurningJS - ForwardBackwardJS

        rightMotors.spin(FORWARD, rightJSspeed, RPM)
        leftMotors.spin(FORWARD, leftJSspeed, RPM)


        maxIntakeRPM = 150
        intakeInOut = (controller.buttonL2.pressing() - controller.buttonR2.pressing()) * maxIntakeRPM
        intake.spin(FORWARD, intakeInOut, RPM)

        maxFrontIntakeRPM = 200
        frontIntakeInOut = (controller.buttonL1.pressing() - controller.buttonR1.pressing()) * maxFrontIntakeRPM
        frontIntake.spin(FORWARD, frontIntakeInOut, RPM)


        if controller.buttonUp.pressing() and not buttonUpState:
            digOutState = not digOutState
            digOut.set(digOutState)
            if digOutState:
                brain.screen.set_cursor(3, 1)
                brain.screen.print("Pneumatic Opened")
            else:
                brain.screen.set_cursor(3, 1)
                brain.screen.print("Pneumatic Closed")
            buttonUpState = True

        if not controller.buttonUp.pressing():
            buttonUpState = False

        wait(20, MSEC)

# create competition instance
comp = Competition(user_control, autonomous)

# actions to do when the program starts
brain.screen.clear_screen()