#!/usr/bin/env python3

# Raspberry Pi Python 3 TM1637 quad 7-segment LED display driver examples
from datetime import datetime
from time import sleep

import tm1637

CLK = 23     # 請更改至你實際接線的 GPIO 腳位 (BCM GPIO??)
DIO = 24     # 請更改至你實際接線的 GPIO 腳位 (BCM GPIO??)
DELAY = 0.5

try:
    tm = tm1637.TM1637(clk=CLK, dio=DIO)
    colon = True
    while True:
        now = datetime.now()
        tm.numbers(now.hour, now.minute, colon=colon)
        colon = not colon
        
        sleep(DELAY)
except KeyboardInterrupt:
    tm.write([0,0,0,0])