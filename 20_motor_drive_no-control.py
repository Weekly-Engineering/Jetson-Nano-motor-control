#=====================================================================================
#20_motor_drive_no-control.py V1.0
#Driving four motors by PWM control using PCA9685.
#
#Copyright (c) 2022 Weekly Engineering
#
#Released under the MIT license.
#see https://opensource.org/licenses/MIT
#=====================================================================================
import time

import motor_drive_funcs

#initialize
pwm = motor_drive_funcs.init_PCA9685()

print('Moving servo on channel 0, press Ctrl-C to quit...')
while True:
    motor_drive_funcs.robot_go_forward(pwm, 3000)
    time.sleep(1)
    motor_drive_funcs.robot_brake(pwm)
    time.sleep(1)
    motor_drive_funcs.robot_go_backward(pwm, 3000)
    time.sleep(1)
    motor_drive_funcs.robot_brake(pwm)
    time.sleep(1)
    motor_drive_funcs.robot_turn_right(pwm, 4095)
    time.sleep(1)
    motor_drive_funcs.robot_brake(pwm)
    time.sleep(1)
    motor_drive_funcs.robot_turn_left(pwm, 4095)
    time.sleep(1)
    motor_drive_funcs.robot_brake(pwm)
    time.sleep(1)
    


