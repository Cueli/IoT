from bsp import board
from libs import lcd
from components.dht11 import dht11
import adc
import serial
import gpio

serial.serial()
ptz_pin=34
led=D23
led1=D21
dhtPin=D18

gpio.mode(ptz_pin, INPUT_ANALOG)
gpio.mode(led, OUTPUT)
gpio.mode(led1, OUTPUT)
try:
    lcd=lcd.LCD(I2C0)
except Exception as e:
        print(e)

# loop forever
while True:
    # acquiring the analog signal from a pin
    value=adc.read(ptz_pin)
    tempe, hum = dht11.read(dhtPin)
    gpio.set(led1, HIGH)
    #LEER DATOS FROM POTENCIOMETRO
    temp=0
    if(value==0):
        temp=0
    else:
        temp=round(value/100)
    

    #apagar / encender led 
    if(temp>tempe):
        gpio.set(led, HIGH)
    else:
        gpio.set(led, LOW)

    if tempe!=None and hum!=None:
        print("Temperature: %-3.1f C" % tempe)
        print("Humidity: %-3.1f %%" % hum)
    #mostrar lcd
    try:
        lcd.setCursorPosition(0, 1)
        lcd.writeString("T: "+str(int(temp))+" C")
        lcd.setCursorPosition(0, 0)
        lcd.writeString("T: "+str(int(tempe))+" C")
        lcd.setCursorPosition(11, 0)
        lcd.writeString("H: "+str(int(hum)))
        print()
    except Exception as e:
        print(e) 

   
    print("The current heating system is set to  %(C)d C" %{"C":temp})
    
    sleep(1000)