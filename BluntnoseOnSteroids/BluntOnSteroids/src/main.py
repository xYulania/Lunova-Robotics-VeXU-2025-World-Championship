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

frontLeftMotor = Motor(Ports.PORT1, GearSetting.RATIO_6_1, True)
topFrontLeftMotor = Motor(Ports.PORT2, GearSetting.RATIO_6_1, False)
backLeftMotor = Motor(Ports.PORT3, GearSetting.RATIO_6_1, True)
topBackLeftMotor = Motor(Ports.PORT4, GearSetting.RATIO_6_1, False)

frontRightMotor = Motor(Ports.PORT5, GearSetting.RATIO_6_1, False)
topFrontRightMotor = Motor(Ports.PORT6, GearSetting.RATIO_6_1, True)
backRightMotor = Motor(Ports.PORT7, GearSetting.RATIO_6_1,False)
topBackRightMotor = Motor(Ports.PORT8, GearSetting.RATIO_6_1, True)

leftMotors = MotorGroup(frontLeftMotor, topFrontLeftMotor, backLeftMotor, topBackLeftMotor)
rightMotors = MotorGroup(frontRightMotor, topFrontRightMotor, backRightMotor, topBackRightMotor)

allMotors = MotorGroup(frontLeftMotor, topFrontLeftMotor, backLeftMotor, topBackLeftMotor, frontRightMotor, topFrontRightMotor, backRightMotor, topBackRightMotor)

inertial = Inertial(Ports.PORT9)

def calibrateInertialSensor():
    while True:
        inertial.calibrate()

        if inertial.is_calibrating():
            controller.screen.clear_line(3)
            controller.screen.print("Calibrating")
        else:
            controller.screen.print("Done")
            controller.rumble("...")
            wait(10, MSEC)

def preAuton():
    calibrateInertialSensor()

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

        leftJSspeed = ForwardBackwardJS - TurningJS
        rightJSspeed = ForwardBackwardJS + TurningJS

        leftMotors.spin(FORWARD, leftJSspeed, RPM)
        rightMotors.spin(FORWARD, rightJSspeed, RPM)

        wait(20, MSEC)

# create competition instance
comp = Competition(user_control, autonomous)

# actions to do when the program starts
brain.screen.clear_screen()