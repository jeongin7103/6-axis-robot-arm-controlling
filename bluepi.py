from __future__ import division

from bluetooth import *
import time
import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685()

# servo_min = 130
# servo_mid = 380
# servo_max = 630

# init
a1 = 380
a2 = 380
a3 = 380
a4 = 380
a5 = 380
a6 = 380

def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    pulse_length //= 4096     # 12 bits of resolution
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)
    
pwm.set_pwm_freq(60)

server_socket= BluetoothSocket(RFCOMM)

port = 1
server_socket.bind(("",port))
server_socket.listen(1)

client_socket, address = server_socket.accept()
print("Accepted connection from ", address)

client_socket.send("bluetooth connected!")

while 1:
    data = client_socket.recv(1024)
    
    if data == b'Reset':
        print('Reset!')
        a1 = 380
        a2 = 380
        a3 = 380
        a4 = 380
        a5 = 380
        a6 = 380
        pwm.set_pwm(0, 0, a1)
        pwm.set_pwm(1, 0, a2)
        pwm.set_pwm(2, 0, a3)
        pwm.set_pwm(3, 0, a4)
        pwm.set_pwm(4, 0, a5)
        pwm.set_pwm(5, 0, a6)
        
    elif data== b'left1':
        a1 = a1+25
        if a1>=630:
            a1 = 630
        print('1DOF Left')
        print(a1)
        print(a2)
        print(a3)
        print(a4)
        print(a5)
        print(a6)
        pwm.set_pwm(0, 0, a1)
            
    elif data== b'right1':
        a1 = a1-25
        if a1<=130:
            a1 = 130
        print('1DOF Right')
        print(a1)
        print(a2)
        print(a3)
        print(a4)
        print(a5)
        print(a6)
        pwm.set_pwm(0, 0, a1)
    elif data== b'left2':
        a2 = a2+25
        if a2>=630:
            a2 = 630
        print('2DOF Left')
        print(a1)
        print(a2)
        print(a3)
        print(a4)
        print(a5)
        print(a6)
        pwm.set_pwm(1, 0, a2)
    elif data== b'right2':
        a2 = a2-25
        if a2<=130:
            a2 = 130
        print('2DOF Right')
        print(a1)
        print(a2)
        print(a3)
        print(a4)
        print(a5)
        print(a6)
        pwm.set_pwm(1, 0, a2)
    elif data== b'left3':
        a3 = a3+25
        if a3>=630:
            a3 = 630
        print('3DOF Left')
        print(a1)
        print(a2)
        print(a3)
        print(a4)
        print(a5)
        print(a6)
        pwm.set_pwm(2, 0, a3)
    elif data== b'right3':
        a3 = a3-25
        if a3<=130:
            a3 = 130
        print('3DOF Right')
        print(a1)
        print(a2)
        print(a3)
        print(a4)
        print(a5)
        print(a6)
        pwm.set_pwm(2, 0, a3)
    elif data== b'left4':
        a4 = a4+25
        if a4>=630:
            a4 = 630
        print('4DOF Left')
        print(a1)
        print(a2)
        print(a3)
        print(a4)
        print(a5)
        print(a6)
        pwm.set_pwm(3, 0, a4)
    elif data== b'right4':
        a4 = a4-25
        if a4<=130:
            a4 = 130
        print('4DOF Right')
        print(a1)
        print(a2)
        print(a3)
        print(a4)
        print(a5)
        print(a6)
        pwm.set_pwm(3, 0, a4)
    elif data== b'left5':
        a5 = a5+25
        if a5>=630:
            a5 = 630
        print('5DOF Left')
        print(a1)
        print(a2)
        print(a3)
        print(a4)
        print(a5)
        print(a6)
        pwm.set_pwm(4, 0, a5)
    elif data== b'right5':
        a5 = a5-25
        if a5<=130:
            a5 = 130
        print('5DOF Right')
        print(a1)
        print(a2)
        print(a3)
        print(a4)
        print(a5)
        print(a6)
        pwm.set_pwm(4, 0, a5)
    elif data== b'left6':
        a6 = a6+25
        if a6>=630:
            a6 = 630
        print('6DOF Left')
        print(a1)
        print(a2)
        print(a3)
        print(a4)
        print(a5)
        print(a6)
        pwm.set_pwm(5, 0, a6)
    elif data== b'right6':
        a6 = a6-25
        if a6<=130:
            a6 = 130
        print('6DOF Right')
        print(a1)
        print(a2)
        print(a3)
        print(a4)
        print(a5)
        print(a6)
        pwm.set_pwm(5, 0, a6)

client_socket.close()
server_socket.close()