from binascii import a2b_hex
from time import sleep

from serial import Serial
import threading

com = Serial(port='COM5', baudrate=3000000, stopbits=1, bytesize=8)
com.set_buffer_size(2048,2048)


def worker1():
    while True:
        if com.in_waiting > 0:
            msg = com.read(size=com.in_waiting)
            print(msg)



def worker2():
    com.write(data=a2b_hex('7573657220656e7465725f756172745f'))
    sleep(0.1)
    com.write(data=a2b_hex('746573740d'))
    sleep(0.5)
    com.flushInput()
    com.write(data=a2b_hex('TL_DUT_REBOOT'.encode().hex()))


t1 = threading.Thread(target=worker1)
t2 = threading.Thread(target=worker2)
t1.start()
t2.start()
t1.join()
t2.join()
