
import atexit
from Adafruit_MotorHAT import Adafruit_MotorHAT

class Motor:
    def __init__(self, driver, channel, alpha=1.0, beta = 0.0 ):
        self._driver = driver
        self.alpha =alpha
        self.beta = beta
        self._motor = self._driver.getMotor(channel)
        #atexit.register(self._release)
    def set_speed(self, speed = 0):
        mapped_value = int ( 255.0 * self.alpha * speed  +  self.beta)
        mapped_speed = min(max(abs(mapped_value), 0), 255)
        self._motor.setSpeed(mapped_speed)
        if( mapped_value < 0):
            self._motor.run(Adafruit_MotorHAT.FORWARD)
        else:
            self._motor.run(Adafruit_MotorHAT.BACKWARD)
    def _release(self):
        self._motor.run(Adafruit_MotorHAT.RELEASE)
