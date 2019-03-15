from PIL import Image
import os
import sys

directory = 'F:\ACM GROUP\Phyton\OpenCv and Image\image'
t = 1

for file_name in os.listdir(directory):
    print(file_name[4])
    print("Processing %s" % file_name)
    image = Image.open(os.path.join(directory, file_name))

    output = image.resize((32, 32), Image.ANTIALIAS)

    if file_name[0] == '0':
        output_file_name = os.path.join(directory, "img_" + str(t) + file_name)
        output.save(output_file_name, "JPEG", quality=95)
        output.rename()
    else:
        output_file_name = os.path.join(directory, "small_" + file_name)
        output.save(output_file_name, "JPEG", quality=95)



    t += 1

print("All done")