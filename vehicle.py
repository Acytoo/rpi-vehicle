import RPi.GPIO as gpio
import config

class Wheel(object):

    def __init__(self, en, pin1, pin2):
        '''
        param en: enable, pin1, pin2: control pin
        ret: None
        '''
        self.in1 = pin1
        self.in2 = pin2

        gpio.setup(en, gpio.OUT, initial = gpio.HIGH)
        gpio.setup(pin1, gpio.OUT, initial = gpio.LOW)
        gpio.setup(pin2, gpio.OUT, initial = gpio.LOW)

        self.pwm = gpio.PWM(en, 80)
        pwm.start(30)


    def speedup(self):
        self.pwm.ChangeDutyCycle(90)

    def slowdown(self):
        self.pwm.ChangeDutyCycle(30)

    def forward(self):
        gpio.output(self.in1, gpio.LOW)
        gpio.output(self.in2, gpio.HIGH)


    def backward(self):
        gpio.output(self.in1, gpio.HIGH)
        gpio.output(self.in2, gpio.LOW)

    def stop(self):
        gpio.output(self.in1, gpio.LOW)
        gpio.output(self.in2, gpio.LOW)


class Vehicle(object):

    def __init__(self):
        gpio.setmode(gpio.BCM)
        self.left_wheels = Wheel(config.PIN_ENABLE_L, config.PIN_L_IN1, config.PIN_L_IN2)
        self.right_wheels = Wheel(config.PIN_ENABLE_R, config.PIN_R_IN1, config.PIN_R_IN2)


    def forward(self):
        self.left_wheels.forward()
        self.right_wheels.forward()

    def backward(self):
        self.left_wheels.backward()
        self.right_wheels.backward()

    def left(self):
        self.left_wheels.backward()
        self.right_wheels.forward()

    def right(self):
        self.left_wheels.forward()
        self.right_wheels.backward()

    def stop(self):
        self.left_wheels.stop()
        self.right_wheels.stop()

    def quit(self):
        self.stop()
        gpio.cleanup()
