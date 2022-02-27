#=====================================================================================
#motor_drive_funcs.py V1.0
#Functions for Driving four motors by PWM control using Adafruit_PCA9685 module.
#
#Copyright (c) 2022 Weekly Engineering
#
#Released under the MIT license.
#see https://opensource.org/licenses/MIT
#=====================================================================================

import PCA9685

PWM_MIN = 0  # Min pulse length out of 4096
PWM_MAX = 4096  # Max pulse length out of 4096

def init_PCA9685():
    # Initialise the PCA9685 using the default address (0x40).
    pwm_address = PCA9685.PCA9685()
    
    # Alternatively specify a different address and/or bus:
    #pwm_address = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)
    
    pwm_address.set_pwm_freq(40)

    return pwm_address

def robot_go_forward(pwm_address, pwm_val):
    pwm_address.set_pwm(0, 0, PWM_MIN)
    pwm_address.set_pwm(1, 0, pwm_val)
    pwm_address.set_pwm(2, 0, pwm_val)
    pwm_address.set_pwm(3, 0, PWM_MIN)
    pwm_address.set_pwm(4, 0, pwm_val)
    pwm_address.set_pwm(5, 0, PWM_MIN)
    pwm_address.set_pwm(6, 0, PWM_MIN)
    pwm_address.set_pwm(7, 0, pwm_val)

def robot_go_backward(pwm_address, pwm_val):
    pwm_address.set_pwm(0, 0, pwm_val)
    pwm_address.set_pwm(1, 0, PWM_MIN)
    pwm_address.set_pwm(2, 0, PWM_MIN)
    pwm_address.set_pwm(3, 0, pwm_val)
    pwm_address.set_pwm(4, 0, PWM_MIN)
    pwm_address.set_pwm(5, 0, pwm_val)
    pwm_address.set_pwm(6, 0, pwm_val)
    pwm_address.set_pwm(7, 0, PWM_MIN)

def robot_turn_right(pwm_address, pwm_val):
    pwm_address.set_pwm(0, 0, pwm_val)
    pwm_address.set_pwm(1, 0, PWM_MIN)
    pwm_address.set_pwm(2, 0, pwm_val)
    pwm_address.set_pwm(3, 0, PWM_MIN)
    pwm_address.set_pwm(4, 0, pwm_val)
    pwm_address.set_pwm(5, 0, PWM_MIN)
    pwm_address.set_pwm(6, 0, pwm_val)
    pwm_address.set_pwm(7, 0, PWM_MIN)

def robot_turn_left(pwm_address, pwm_val):
    pwm_address.set_pwm(0, 0, PWM_MIN)
    pwm_address.set_pwm(1, 0, pwm_val)
    pwm_address.set_pwm(2, 0, PWM_MIN)
    pwm_address.set_pwm(3, 0, pwm_val)
    pwm_address.set_pwm(4, 0, PWM_MIN)
    pwm_address.set_pwm(5, 0, pwm_val)
    pwm_address.set_pwm(6, 0, PWM_MIN)
    pwm_address.set_pwm(7, 0, pwm_val)

def robot_stop(pwm_address):
    pwm_address.set_pwm(0, 0, PWM_MIN)
    pwm_address.set_pwm(1, 0, PWM_MIN)
    pwm_address.set_pwm(2, 0, PWM_MIN)
    pwm_address.set_pwm(3, 0, PWM_MIN)
    pwm_address.set_pwm(4, 0, PWM_MIN)
    pwm_address.set_pwm(5, 0, PWM_MIN)
    pwm_address.set_pwm(6, 0, PWM_MIN)
    pwm_address.set_pwm(7, 0, PWM_MIN)

def robot_brake(pwm_address):
    pwm_address.set_pwm(0, 0, PWM_MAX)
    pwm_address.set_pwm(1, 0, PWM_MAX)
    pwm_address.set_pwm(2, 0, PWM_MAX)
    pwm_address.set_pwm(3, 0, PWM_MAX)
    pwm_address.set_pwm(4, 0, PWM_MAX)
    pwm_address.set_pwm(5, 0, PWM_MAX)
    pwm_address.set_pwm(6, 0, PWM_MAX)
    pwm_address.set_pwm(7, 0, PWM_MAX)
