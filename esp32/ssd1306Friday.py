from machine import I2C, Pin
i2c=I2C(scl=Pin(4), sda=Pin(5))
devices = i2c.scan()

import ssd1306
#import itoa
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
oled.text("Hello", 0, 0, 1)
oled.show()

oled_right = ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3D)
oled_right.text("World", 0, 0, 1)
oled_right.text("ZZ", 10, 10, 1)   #oled_right.text(i2c.scan(), 10, 10, 1)
oled_right.show()

if len(devices) == 0:
  oled.text("no i2c device !", 0, 0, 1)
#else:
# oled.text("i2c devices\n found:",20,20,1)     # len(devices))
#oled_right.text(itoa(len(devices))), 20,20,1)
#oled.text(str(9), 30,30,1)
# https://www.freecodecamp.org/news/python-new-line-and-how-to-python-print-without-a-newline/
for num in range(len(devices)):
    oled.text(str(devices[num]), 20,20+(num*10),1)
oled.show()
oled_right.show()
print("see oled display")
print(devices)


 
 
