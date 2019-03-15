from PIL import Image
import os
import sys

directory = 'F:\ACM GROUP\Phyton\OpenCv and Image\image'
d0 = 'F:\ACM GROUP\Phyton\OpenCv and Image\d0'
d1 = 'F:\ACM GROUP\Phyton\OpenCv and Image\d1'
d2 = 'F:\ACM GROUP\Phyton\OpenCv and Image\d2'
d3 = 'F:\ACM GROUP\Phyton\OpenCv and Image\d3'
d4 = 'F:\ACM GROUP\Phyton\OpenCv and Image\d4'
d5 = 'F:\ACM GROUP\Phyton\OpenCv and Image\d5'
d6 = 'F:\ACM GROUP\Phyton\OpenCv and Image\d6'
d7 = 'F:\ACM GROUP\Phyton\OpenCv and Image\d7'
d8 = 'F:\ACM GROUP\Phyton\OpenCv and Image\d8'
d9 = 'F:\ACM GROUP\Phyton\OpenCv and Image\d9'

t0 = t1 = t2 = t3 = t4 = t5 = t6 = t7 = t8 = t9 = 2001


for file_name in os.listdir(directory):

    # print(file_name[4])
    # print("Processing %s" % file_name)

    image = Image.open(os.path.join(directory, file_name))

    output = image.resize((32, 32), Image.ANTIALIAS)

    if file_name[0] == '0':
        output_file_name = os.path.join(d0, "img_0_" + str(t0) + ".jpg")
        t0 += 1
        output.save(output_file_name, "JPEG", quality=95)
    elif file_name[0] == '1':
        output_file_name = os.path.join(d1, "img_1_" + str(t1) + ".jpg")
        t1 += 1
        output.save(output_file_name, "JPEG", quality=95)
    elif file_name[0] == '2':
        output_file_name = os.path.join(d2, "img_2_" + str(t2) + ".jpg")
        t2 += 1
        output.save(output_file_name, "JPEG", quality=95)
    elif file_name[0] == '3':
        output_file_name = os.path.join(d3, "img_3_" + str(t3) + ".jpg")
        t3 += 1
        output.save(output_file_name, "JPEG", quality=95)
    elif file_name[0] == '4':
        output_file_name = os.path.join(d4, "img_4_" + str(t4) + ".jpg")
        t4 += 1
        output.save(output_file_name, "JPEG", quality=95)
    elif file_name[0] == '5':
        output_file_name = os.path.join(d5, "img_5_" + str(t5) + ".jpg")
        t5 += 1
        output.save(output_file_name, "JPEG", quality=95)
    elif file_name[0] == '6':
        output_file_name = os.path.join(d6, "img_6_" + str(t6) + ".jpg")
        t6 += 1
        output.save(output_file_name, "JPEG", quality=95)
    elif file_name[0] == '7':
        output_file_name = os.path.join(d7, "img_7_" + str(t7) + ".jpg")
        t7 += 1
        output.save(output_file_name, "JPEG", quality=95)
    elif file_name[0] == '8':
        output_file_name = os.path.join(d8, "img_8_" + str(t8) + ".jpg")
        t8 += 1
        output.save(output_file_name, "JPEG", quality=95)
    else:
        output_file_name = os.path.join(d9, "img_9_" + str(t9) + ".jpg")
        t9 += 1
        output.save(output_file_name, "JPEG", quality=95)


print("All done")