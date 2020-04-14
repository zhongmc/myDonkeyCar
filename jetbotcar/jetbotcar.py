#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import json
import time
from Adafruit_MotorHAT import Adafruit_MotorHAT
from .motor import Motor

class JetbotCar:
    def __init__(self,  addr=0x60, i2c_bus = 1, left_motor_channel = 1, right_motor_channel=2, left_alpha = 1, left_beta = 0,right_alpha=1, right_beta = 0):
        print("init jetbot car addr: ", addr, "bus: ", i2c_bus)
        if i2c_bus is not None:
            from Adafruit_GPIO import I2C
            #replace the get_bus function with our own
            def get_bus():
                return i2c_bus
            I2C.get_default_bus = get_bus        
        self.motor_driver = Adafruit_MotorHAT(addr, i2c_bus)
        self.left_alpha = left_alpha
        self.left_beta = left_beta
        self.right_alpha = right_alpha
        self.right_beta = right_beta
        self.left_motor = Motor(self.motor_driver, channel=left_motor_channel, alpha=left_alpha, beta = left_beta )
        self.right_motor = Motor(self.motor_driver, channel= right_motor_channel, alpha=right_alpha, beta = right_beta )
    #   atexit.register(self._release)
       
    def set_motors(self, left_speed, right_speed):
        self.left_motor.set_speed( left_speed )
        self.right_motor.set_speed( right_speed )
    
    def forward(self, speed=1.0, duration=None):
        self.left_motor.set_speed( speed )
        self.right_motor.set_speed( speed )

    def backward(self, speed=1.0):
        self.left_motor.set_speed( -speed )
        self.right_motor.set_speed( -speed )

    def left(self, speed=1.0):
        self.left_motor.set_speed( -speed )
        self.right_motor.set_speed( speed )

    def right(self, speed=1.0):
        self.left_motor.set_speed( speed )
        self.right_motor.set_speed( -speed )

    def stop(self):
        self.left_motor.set_speed( 0 )
        self.right_motor.set_speed( 0  )

 
# donkeyCar api
    def update(self):
        pass

    def run(self, throttle, angle):
        left_motor_speed = throttle
        right_motor_speed = throttle
        if angle < 0:
            left_motor_speed *= (1.0 - (-angle))
        elif angle > 0:
            right_motor_speed *= (1.0 - angle)
        self.set_motors(left_motor_speed, right_motor_speed)
        pass

    def run_threaded(self):
        return self.x,self.y,self.theta, self.w, self.v
        pass

    def shutdown(self):
        self.shutdown = True 