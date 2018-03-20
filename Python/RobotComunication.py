import nxt.locator
from nxt.motor import *
from nxt.sensor import *


class ntx_robot():
    # INPUT
    portUltrasonic = PORT_1
    portLight = PORT_2
    portColor = PORT_3
    portGyroscope = PORT_4
    # OUTPUT
    portMotorL = PORT_A
    portMotorR = PORT_B

    def __int__(self):
        self.b = nxt.locator.find_one_brick()

    def input_sensor(self):
        # Ultrasonic
        # Light sensor
        # Color sensor
        # Gyroscope
        # Port used for sensor
        valueUltrasonic = Ultrasonic(self.b, self.portUltrasonic).get_sample
        valueLight = Light(self.b, self.portLight).get_sample
        valueColor = Color20(self.b, self.portColor).get_sample
        valueGyroscope = HTGyro(self.b, self.portGyroscope).get_sample

        return [valueUltrasonic, valueLight, valueColor, valueGyroscope]

    def output_motor(self, speedL, speedR):
        # Right Motor
        # Left Motor
        motor_L = Motor(self.b, self.portMotorL)
        motor_R = Motor(self.b, self.portMotorR)

        motor_L.turn(speedL, 360)
        motor_R.turn(speedR, 360)
        return
