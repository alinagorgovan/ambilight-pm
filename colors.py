import pyscreenshot as ImageGrab
import time
import os
from colour import Color
import serial

# Define the total numberof leds
LED_COUNT = 36
# Number of leds per width
WIDTH = 11
# Number of leds per height
HEIGHT = 7

# Open the serial port with the right configurations
ser = serial.Serial()
ser.baudrate = 9600
ser.port = '/dev/ttyUSB2'
ser.parity = 'E'
ser.open()
ser.timeout = 0.3

while True:
    colors= []

    # take a screenshot
    image = ImageGrab.grab()

    width = image.size[0]
    height = image.size[1]

    # compute for lower leds
    for i in range(WIDTH):
        counter = 0
        red = 0
        green = 0
        blue = 0
        chunk_start = i * width / WIDTH
        chunk_end = (i + 1) * width / WIDTH
        # Compute the sum of colours of the pixels from the current area
        for x in range(int(round(chunk_start)), int(round( chunk_end)), 5):
            for y in range(0, int(round(height / 2)), 10):
                color = image.getpixel((x, y))
                red += color[0]
                green += color[1]
                blue += color[2]
                counter += 1

        red = (int(round(red / counter)))
        green = (int(round(green / counter)))
        blue = (int(round(blue / counter)))
        # Add computed color to list
        colors += [red, green, blue]

    # compute for right margin leds
    for i in range(HEIGHT):
        counter = 0
        red = 0
        green = 0
        blue = 0
        chunk_start = i * height / HEIGHT
        chunk_end = (i + 1) * height / HEIGHT
        # Compute the sum of colours of the pixels from the current area
        for x in range(int(round(width / 2)), int(round(width)), 10):
            for y in range(int(round(chunk_start)), int(round(chunk_end)), 5):
                color = image.getpixel((x, y))
                red += color[0]
                green += color[1]
                blue += color[2]
                counter += 1

        red = (int(round(red / counter)))
        green = (int(round(green / counter)))
        blue = (int(round(blue / counter)))
        # Add computed color to list
        colors += [red, green, blue]

    # compute for upper leds
    for i in range(WIDTH - 1, -1, -1):
        counter = 0
        red = 0
        green = 0
        blue = 0
        chunk_start = i * width / WIDTH
        chunk_end = (i + 1) * width / WIDTH
        # Compute the sum of colours of the pixels from the current area
        for x in range(int(round(chunk_start)), int(round(chunk_end)), 5):
            for y in range(int(round(height / 2)), int(round(height)), 10):
                color = image.getpixel((x, y))
                red += color[0]
                green += color[1]
                blue += color[2]
                counter += 1

        red = (int(round(red / counter)))
        green = (int(round(green / counter)))
        blue = (int(round(blue / counter)))
        # Add computed color to list
        colors += [red, green, blue]

    # compute for left leds
    for i in range(HEIGHT - 1, -1, -1):
        counter = 0
        red = 0
        green = 0
        blue = 0
        chunk_start = i * height / HEIGHT
        chunk_end = (i + 1) * height / HEIGHT
        # Compute the sum of colours of the pixels from the current area
        for x in range(0, int(round(width / 2)), 10):
            for y in range(int(round(chunk_start)), int(round( chunk_end)), 5):
                color = image.getpixel((x, y))
                red += color[0]
                green += color[1]
                blue += color[2]
                counter += 1

        red = (int(round(red / counter)))
        green = (int(round(green / counter)))
        blue = (int(round(blue / counter)))
        # Add computed color to list
        colors += [red, green, blue]

    ser.write(colors)
    ser.flush()