import utime
import picodisplay as display  


def pic(s):
    # Set up and initialise Pico Display
    width = display.get_width()
    height = display.get_height()

    # Load image
    f = open(s + ".bin", "rb")
    buf = bytearray(f.read(width * height * 2))
    f.close()

    display.init(buf)
    display.set_backlight(0.8)


    # Display
    display.update()
    utime.sleep(1.0)

pic("ape0")

while True:
    if display.is_pressed(display.BUTTON_A):
        pic("ape0")
    elif display.is_pressed(display.BUTTON_B):
        pic("ape1")
    elif display.is_pressed(display.BUTTON_X):
        pic("ape2")
    elif display.is_pressed(display.BUTTON_Y):
        pic("ape3")

