#!/usr/bin/python3
# -*- coding: utf-8 -*- 
import smbus
import datetime
from time import sleep

last_dt_str = ''

def showtime():
    global last_dt_str
    dt_now = datetime.datetime.now()
    dt_str = dt_now.strftime('%H%M')
    if last_dt_str != dt_str:
        last_dt_str = dt_str
        bus = smbus.SMBus(1)
        for i, c in enumerate(list(dt_str)):
            # set pattern
            bus.write_word_data(21 + i, 1, 2)

            # set duration
            bus.write_word_data(21 + i, 2, 1000)

            # set number
            bus.write_word_data(21 + i, 3, int(c))

            # set start
            bus.write_word_data(21 + i, 0, 0)
        bus.close()

def app_main():
    while True:
        showtime()
        sleep(1)
  
if __name__ == '__main__':
	app_main()
