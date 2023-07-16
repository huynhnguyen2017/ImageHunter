from PIL import Image
import os


def compress(image):

    print("Format : ", image.format)
    print("File path: ", image.filename)

    compressed_file_name = "results/image-file-compressed"
    result_image = os.path.join(os.getcwd(), compressed_file_name)
    image.save(result_image,
               "JPEG",
               optimize=True,
               quality=10)
    return result_image
