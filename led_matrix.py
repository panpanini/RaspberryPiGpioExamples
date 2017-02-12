import time
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from Adafruit_LED_Backpack import BicolorMatrix8x8

display = BicolorMatrix8x8.BicolorMatrix8x8()
#init display
display.begin()

font = ImageFont.load_default()
finc = "FiNC "
x = "x "
iot = "IoT"

# create a new image with RGB colour space, width, height
image = Image.new('RGB', (6 * (len(finc) + len(x) + len(iot)), 8))
draw = ImageDraw.Draw(image)

# draw FiNC text in red
draw.text((-1,-2), finc, font=font, fill=(255,0,0))
# draw x text in green
draw.text((-1 + 6*len(finc), -2), x, font=font, fill=(0,255,0))
# draw IoT text in yellow(orange)
draw.text((-1 + 6*(len(finc)+len(x)), -2), iot, font=font, fill=(255,255,0))

# create a series of images to display on the matrix from our long image
scrollable = display.horizontal_scroll(image)
# animate the series of images on the display
display.animate(scrollable)
