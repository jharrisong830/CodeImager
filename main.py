""" NAME:   main.py
    AUTHOR: John Graham
    DATE:   04/27/23    """


from imager import encode_to_image, decode_to_text
import sys, os

USAGE = "CodeImager Usage:\n" \
        "<python script> <mode: -i | -t> <source/path/> <dest/path/> [color mode: all | r | g | b]\n" \
        "\t-i -> convert a source text file to an image\n" \
        "\t-t -> convert a source image file to a text file\n"


def exit_error():
    print(USAGE)
    sys.exit(1)



if __name__=="__main__":
    args=sys.argv[1:]
    if len(args)==0:
        print(USAGE)
        sys.exit(0)
    if args[0]=="-h":
        print(USAGE)
        sys.exit(0) if len(args)==1 else exit_error()
    if len(args)==3:
        args.append("all")
    elif len(args)!=4:
        exit_error()
    if args[0] not in ("-i", "-t"): exit_error()
    if args[3] not in ("all", "r", "g", "b"): exit_error()
    if not os.path.exists(args[1]): exit_error()
    if args[0]=="-i":
        encode_to_image(args[1], args[2], args[3])
    else:
        decode_to_text(args[1], args[2])
    sys.exit(0)
