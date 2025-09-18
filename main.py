from uqtpy.comm.ble.service import QtBLE
from uqtpy.comm.ble.service import QtBLEService

from uqtpy.actuators.motor import Motor
from uqtpy.actuators.argb import ARGB
from uqtpy.actuators.buzzer import Buzzer
from uqtpy.actuators.servo import Servo
from uqtpy.sensors.ultrasonic import UltraSonic
from uqtpy.sensors.tof import TOF


motor = Motor(ob=True)
argb = ARGB(ob=True)
buzzer = Buzzer(ob=True)
servoObj = Servo(ob=True)
us = UltraSonic(ob=True)
tof = TOF(ob=True)

components = None
qtservice = None

components = [ buzzer, motor, servoObj]
qtservice = QtBLEService(components=components,uuid='0x1011')

qtble = QtBLE(name='qtble', debug=True)
qtble.add_services(services=[qtservice])
qtble.start_advertising()
