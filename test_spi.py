import spidev
import time

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 5000

# setup max7921
spi.xfer([0x0C,0x01]) # Normal Operation
spi.xfer([0x09,0x00]) # No Decode Mode
spi.xfer([0x0B,0x07]) # Scan limit 8 digits

#while True:
#    spi.xfer([0x0F,0x01])
#    time.sleep(1)
#    spi.xfer([0x0F,0x00])
#    time.sleep(1)

while True:
    for i in range(1,9):
        for j in range(0xFF):
            spi.xfer([i,j+1])
            time.sleep(.1)
