from binascii import a2b_hex
from time import sleep

from serial import Serial


com = Serial(port='COM4', baudrate=3000000, stopbits=1, bytesize=8)
com.write(data=a2b_hex('7573657220656e7465725f756172745f'))
sleep(0.1)
com.write(data=a2b_hex('746573740d'))
