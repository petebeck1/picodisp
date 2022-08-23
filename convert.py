import sys
from PIL import Image

# Check syntax
if len(sys.argv) < 3:
    print("Usage: convert source dest")
    exit(1)

# Pico Display size
w = 240
h = 135

# Load image and convert to RGB
img = Image.open(sys.argv[1])
conv = img.convert("RGB")

# Get bounding box
x1 = 0
x2 = img.width
y1 = 0
y2 = img.height

if (w * y2) > (h * x2):
    lines = x2 * h / w
    y1 = (y2 - lines) / 2
    y2 = y1 + lines
else:
    cols = y2 * w / h
    x1 = (x2 - cols) / 2
    x2 = x1 + cols

box = (x1, y1, x2, y2)

# Scale to 240x135
res = conv.resize((w,h), Image.ANTIALIAS, box)

# Save
#res.save("test.png", "PNG")

# Convert to RGB565
pixels = list()
for y in range(h):
    for x in range(w):
        (r, g, b) = res.getpixel((x, y))
        rgb = ((r & 0xf8) << 8) + ((g & 0xfc) << 3) + (b >> 3)
        pixels.append(rgb >> 8)
        pixels.append(rgb & 255)
        
# Save
data = bytes(pixels)
f = open(sys.argv[2], "wb")
f.write(data)
f.close()

