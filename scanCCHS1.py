
# date 15/12/2022
# after lots of editting for unrecognised characters 
import machine
# RPi PICO uses pins 8,9 for sda,scl
# esp8266 uses pins 4,5
sda=machine.Pin(4)
scl=machine.Pin(5)
i2c=machine.I2C(sda=sda, scl=scl, freq=100000)

print('Scan i2c bus...')
devices = i2c.scan()

if len(devices) == 0:
 print("no i2c device !")
else:
 print('i2c devices found:', len(devices))

for device in devices:
    print("Decimal address: ", device," | hexa address: ",hex(device))
    
