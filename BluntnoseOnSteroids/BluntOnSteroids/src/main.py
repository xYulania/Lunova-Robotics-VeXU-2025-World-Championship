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

frontLeftMotor = Motor(Ports.PORT17, GearSetting.RATIO_6_1, True)
topFrontLeftMotor = Motor(Ports.PORT18, GearSetting.RATIO_6_1, False)
backLeftMotor = Motor(Ports.PORT19, GearSetting.RATIO_6_1, True)
topBackLeftMotor = Motor(Ports.PORT20, GearSetting.RATIO_6_1, False)

frontRightMotor = Motor(Ports.PORT11, GearSetting.RATIO_6_1, True)
topFrontRightMotor = Motor(Ports.PORT12, GearSetting.RATIO_6_1, False)
backRightMotor = Motor(Ports.PORT13, GearSetting.RATIO_6_1,True)
topBackRightMotor = Motor(Ports.PORT14, GearSetting.RATIO_6_1, False)

leftMotors = MotorGroup(frontLeftMotor, topFrontLeftMotor, backLeftMotor, topBackLeftMotor)
rightMotors = MotorGroup(frontRightMotor, topFrontRightMotor, backRightMotor, topBackRightMotor)

allMotors = MotorGroup(frontLeftMotor, topFrontLeftMotor, backLeftMotor, topBackLeftMotor, frontRightMotor, topFrontRightMotor, backRightMotor, topBackRightMotor)


intake = Motor(Ports.PORT16, GearSetting.RATIO_18_1, False)
intake.set_velocity(200, RPM)

frontIntake = Motor(Ports.PORT15)

climbLeft = Motor(Ports.PORT2, GearSetting.RATIO_36_1, False)
climbRight = Motor(Ports.PORT3, GearSetting.RATIO_36_1, True)

climb = MotorGroup(climbLeft, climbRight)

digOut1 = DigitalOut(brain.three_wire_port.a)
digOut1.set(True)

digOut2 = DigitalOut(brain.three_wire_port.b)
digOut2.set(True)

def autonomous():
    brain.screen.clear_screen()
    brain.screen.print("autonomous code")
    # place automonous code here

def user_control():
    brain.screen.clear_screen()
    brain.screen.print("driver control")
    # place driver control in this while loop

    digOut1State = True
    digOut2State = True
    buttonState = False

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

        # climbRPM = 100
    
        # climbState = False
        if controller.buttonA.pressing():
            # climb.spin(FORWARD, 100, RPM)
            climbLeft.spin(FORWARD, 100, RPM)
            climbRight.spin(FORWARD, 100, RPM)

        if not controller.buttonA.pressing():
            climbState = False


        if controller.buttonRight.pressing() and not buttonState:
            digOut1State = not digOut1State
            digOut2State = not digOut2State
            digOut1.set(digOut1State)
            digOut2.set(digOut2State)
            buttonState = True
            
            if not controller.buttonRight.pressing():
                buttonState = False

        wait(20, MSEC)

# create competition instance
comp = Competition(user_control, autonomous)

# actions to do when the program starts
brain.screen.clear_screen()

                                                    # ARCHIVE


        # buttonUpState = False  
        # buttonDownState = False

        # if controller.buttonUp.pressing() and not buttonUpState:
        #     digOut1State = not digOut1State
        #     digOut1.set(digOut1State)
        #     if digOut1State:
        #         brain.screen.set_cursor(3, 1)
        #         brain.screen.print("Pneumatic Opened")
        #     else:
        #         brain.screen.set_cursor(3, 1)
        #         brain.screen.print("Pneumatic Closed")
        #     buttonUpState = True

        # if not controller.buttonUp.pressing():
        #     buttonUpState = False

        # if controller.buttonDown.pressing() and not buttonDownState:
        #     digOut2State = not digOut2State
        #     digOut2.set(digOut2State)
        #     if digOut2State:
        #         brain.screen.set_cursor(4, 1)
        #         brain.screen.print("Pneumatic Opened")
        #     else:
        #         brain.screen.set_cursor(4, 1)
        #         brain.screen.print("Pneumatic Closed")
        #     buttonDownState = True
        
        # if not controller.buttonDown.pressing():
        #     buttonDownState = False

