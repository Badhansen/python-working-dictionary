from PIL import Image
import numpy as np

col = Image.open("1.jpg")
gray = col.convert('L')

# Let numpy do the heavy lifting for converting pixels to pure black or white
bw = np.asarray(gray).copy()

# Pixel range is 0...255, 256/2 = 128
bw[bw < 128] = 1    # Black
bw[bw >= 128] = 0 # White

# Now we put it back in Pillow/PIL land
for i in bw:
    for j in i:
        print(j, end="")

    print()
imfile = Image.fromarray(bw)
imfile.save("result_bw.png")