#!/usr/bin/env python3

import sys
import math

FOLDER_PATH = "/sys/class/backlight/intel_backlight/"
BRIGHTNESS_FILE_PATH = FOLDER_PATH + "brightness"
MAX_BRIGHTNESS_FILE_PATH = FOLDER_PATH + "max_brightness"

MIN_PERCENT = 1
MAX_PERCENT = 100

def brightnessToPercent(brightness, maximum_brightness):
	return (brightness * 100) / maximum_brightness

def percentToBrightness(percent, maximum_brightness):
	return (percent * maximum_brightness) / 100

def main():
    brightness_file = open(BRIGHTNESS_FILE_PATH, "r+")
    max_brightness_file = open(MAX_BRIGHTNESS_FILE_PATH)

    brightness = brightness_file.read()
    max_brightness = max_brightness_file.read()

    brightness = int(brightness)
    max_brightness = int(max_brightness)

    percent = brightness

    if len(sys.argv) > 1:
        percent = int(sys.argv[1])

        if percent < MIN_PERCENT:
            print("Use {} brightness instead of {}.".format(MIN_PERCENT, percent))
            percent = MIN_PERCENT
        elif percent > MAX_PERCENT:
            print("Use {} brightness instead of {}.".format(MAX_PERCENT, percent))
            percent = MAX_PERCENT
    else:
        percent = int(input("Enter percent : "))

        while percent > MAX_PERCENT or percent < MIN_PERCENT:
                percent = int(input("Please enter the number that betweens 1-100 : "))

    result = percentToBrightness(percent, max_brightness)

    actual_result = math.floor(result)
    brightness_file.write(str(actual_result))

    brightness_file.close()
    max_brightness_file.close()


if __name__ == "__main__":
    main()

