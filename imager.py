""" NAME:   imager.py
    AUTHOR: John Graham
    DATE:   04/27/23    """


from PIL import Image
from utilities import (
    color_tuple,
    get_dimensions
)



def encode_to_image(filepath: str, imgpath: str, color: str="all"):
    """given a 'filepath', converts the file to an image (name specified by 'imgpath'),
    based on the value of its bytes. Default is a random multicolor image ("all"),
    can be set to red("r)" green ("g") or blue ("b") only\n
    RAISES:     AssertionError"""
    assert color in ("r", "g", "b", "all")

    every_byte=[]

    with open(filepath, "r") as file:
        byte=file.read(1)
        while byte!="":
            byte_val=ord(byte)
            rgb_val=color_tuple(byte_val, color)
            every_byte.append(rgb_val)
            byte=file.read(1)

    total_bytes=len(every_byte)
    dimensions=get_dimensions(total_bytes)
    counter=0
    with Image.new("RGB", dimensions) as img:
        w,h=dimensions
        for i in range(w):
            for j in range(h):
                if counter >= total_bytes: break
                img.putpixel((i,j), every_byte[counter])
                counter+=1
        split_path=imgpath.split(".")
        ext = "png" if len(split_path)==1 else split_path[1]
        img.save(imgpath, format=ext)


def decode_to_text(imgpath: str, filepath: str):
    """given an image 'imgpath', converts it back to a file (name specified by 'filepath')"""
    with Image.open(imgpath, "r") as img, open(filepath, "w") as file:
        w,h=img.size
        for i in range(w):
            for j in range(h):
                pix=img.getpixel((i,j))
                char=chr(sum(pix))
                if ord(char)!=0: file.write(char)
