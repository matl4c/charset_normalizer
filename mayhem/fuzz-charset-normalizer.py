#! /usr/bin/python3

import atheris
import sys
import io

with atheris.instrument_imports():
    from charset_normalizer import from_bytes, detect

def TestOneInput(input_bytes):
    from_bytes(input_bytes)
    detect(input_bytes)


def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
