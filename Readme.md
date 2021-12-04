# **NXYI2C Python sample (for Raspberry Pi)**

This is a sample of a clock using NXYI2C.
It just shows the system time to 4 nixie tubes.
Displays hours and minutes to the four NXYI2C at I2C addresses 21 through 24.


# Setup as service

Run the following command on your Raspberry Pi.

```
curl https://www.nixielive.com/setup-nxyi2c-python-clock.sh | bash
```

This command will install the following tools at first

* git
* python3-smbus:armhf

Then, copy files

* Copy `nxyi2c-python-clock.py` to `/usr/local/bin`.
* Copy `nixielive-clock.service` to `/etc/systemd/system`.

Then, register `nixielive-clock.service` as a service


# Program description (nxyi2c-python-clock.py)

This is a really simple program that just gets the system time as a string in the format HHMM (00:00-23:59) and sends it to NXYI2C for each digit.

## Time string

In the following program, the system time is formatted by `%H%M`. If you change this to `%m%d`, it may become a calendar.

```
dt_now = datetime.datetime.now()
dt_str = dt_now.strftime('%H%M')
```

## I2C address

Since the I2C address is used from 21 (HEX:15), 21 is hard-coded. If you want to use a different I2C address, please change this part.

```
# set pattern
bus.write_word_data(21 + i, 1, 2)
```

Also, check [Default firmware sketch of NXYI2C](https://github.com/nixielive/nxyi2c-default-firmware#readme) for more information about the values used for each argument of `write_word_data`.

## Display pattern

When changing the number to be displayed, it is shown in a fade-in pattern. The following code has the following meaning

```
# set pattern
bus.write_word_data(21 + i, 1, 2)
```

* command = 1 : set pattern
* value = 2 : Fade in


## Duration

Specifies how long it will take to complete the pattern.

```
# set duration
bus.write_word_data(21 + i, 2, 1000)
```

* command = 2 : set duration
* value = 1000 : ms

## Display number

Specifies the number to be displayed on the Nixie tube.

```
# set number
bus.write_word_data(21 + i, 3, int(c))
```

* command = 3 : set number
* value : Numbers to be displayed on Nixie tubes

## Start changing the numbers

Start changing the numbers to be displayed with what you have specified in the previous commands.

```
# set start
bus.write_word_data(21 + i, 0, 0)
```

* command = 0 : start
* value : ignored
