from gpiozero import LED, Button
from time import sleep


georgcenter_power = LED(17)
georgcenter_reset = LED(27)
georgcenter_on = Button(16)

voldbymc_power = LED(26)
voldbymc_reset = LED(13)
voldbymc_on = Button(12)



while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1) 

