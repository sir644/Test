
# Importing
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# Intializing Hub
hub = PrimeHub()

# Defining Motors
# Drive Motors
left_drive_motor = Motor(Port.E, positive_direction=Direction.COUNTERCLOCKWISE)
right_drive_motor = Motor(Port.F)

# Arm Motors
left_arm_motor = Motor(Port.A)
right_arm_motor = Motor(Port.B)

# Renaming DriveBase for Ease
robot = DriveBase(left_drive_motor, right_drive_motor, wheel_diameter=56, axle_track=110)
robot.settings(500, 250, 250, 250) #(speed, acceleration, turn speed, turn acceleration)
robot.use_gyro(True)

# Color Sensors
right_color_sensor = (Port.D)
left_color_sensor = (Port.C)

robot.straight(300)