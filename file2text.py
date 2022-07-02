#!/usr/bin/env python
#
# file2text
#
# Encode and decode files as text using base85
# Use --help for a basic rundown of usage
#
# Copyright (C) 2022 Ben Marsh <seafork@tutamail.com>

import argparse
from base64 import b85decode, b85encode
import os.path as op


def parse_args():
    parser = argparse.ArgumentParser(
        description="Encode and decode files as text using base85. Deafult is endcode, pass -d to decode.")
    parser.add_argument(
        "infile", help="the file you want to encode or decode", type=str)
    parser.add_argument("outfile", help="the file that stores the encoded or decoded contents",
                        type=str, nargs='?', default="out.f2t")
    parser.add_argument("-f", "--force", action="store_true",
                        help="allows the program to overwrite an existing output file.")
    parser.add_argument("-d", "--decode", action="store_true",
                        help="decodeds the input file and then writes to output.")

    args = parser.parse_args()

    if vars(args) == {}:
        parser.print_help()
        exit()

    if not(op.exists(args.infile)):
        print("The input file doesn't exist!")
        exit()

    if op.exists(args.outfile):
        if not(args.force):
            print(
                "Output file already exists! If you want to override this file pass -f to the program")
            exit()

    return args


def encode_data(data, args):
    print("Encoding file...")
    encoded_data = b85encode(data).decode(encoding="utf-8")
    print("Encoding finished!")

    print("Writing out file...")
    with open(args.outfile, "w") as f:
        f.write(encoded_data)
    print("File written!")


def decode_data(data, args):
    print("Decoding file...")
    decoded_data = b85decode(data)
    print("Decoding finished!")

    print("Writing out file...")
    with open(args.outfile, "wb") as f:
        f.write(decoded_data)
    print("File written!")


def main():
    args = parse_args()

    with open(args.infile, "rb") as f:
        data = f.read()
    if args.decode:
        decode_data(data, args)
    else:
        encode_data(data, args)


if __name__ == "__main__":
    main()
