# ascii_generator.py

import sys
import random
from PIL import Image

def show_frame(image_path):
    img = None
    try: img = Image.open(image_path)
    except: return "Invalid path."

    width, height = img.size
    pixels = list(img.getdata())

    space_detector = 0
    for pixel_clump in pixels:

        avg_color = int(sum(pixel_clump) / len(pixel_clump))
        if avg_color == 0: avg_color = random.randint(100, 105)
        print(f"\033[48;5;{avg_color}m  \033[0m", end = "")
        if space_detector % width == 0: print()
        space_detector += 1

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for index, arg in enumerate(sys.argv):
            sys.argv[index] += " "
        img_path = "".join(sys.argv[1:]).rstrip()

    else:
        img_path = input("Enter an image path: ")

    possible_error = show_frame(img_path)
    if possible_error is not None:
        print(possible_error)
    else:
        print("\n")
