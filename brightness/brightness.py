#!/usr/bin/python3

import math
import sys
import os

brightness_file = "/sys/class/backlight/amdgpu_bl0/brightness"

def read_brightness():
    with open(brightness_file, mode='r') as _f:
        return int(_f.read())

def write_brightness(_b):
    
    _b = math.ceil(_b)

    if _b < 10: _b = 10
    if _b > 255: _b = 255

    os.system(f'echo "{_b}" | sudo /usr/bin/tee {brightness_file}')

args = sys.argv[1:]

brightness = read_brightness()

if len(args) == 0:
    print(brightness)
else:

    operation = args[0]

    if operation == '-inc':
        write_brightness(brightness + int(args[1]))
    elif operation == "-dec":
        write_brightness(brightness - int(args[1]))



