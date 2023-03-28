from PIL import Image


def find_msg(image_path):
    """Find the message hidden in the image.
    :param image_path: path to the image
    :return: the message
    """
    image = Image.open(image_path)
    width, height = image.size
    bl_px = [chr(y) for x in range(width) for y in range(height) if image.getpixel((x,y)) == 1]
    return "".join(bl_px)


print(find_msg("code.png"))
