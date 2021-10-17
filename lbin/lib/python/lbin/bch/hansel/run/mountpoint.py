import sys
import importlib

from lbin.bch.builtin import BCH as bch

BCH.fpath = __file__

USAGE=f""" USAGE:\n\t{BCH.fname}\nDESCRIPTION:\n\tfoo\n"""

def main():
    if len(sys.argv)>1:
        sys.stderr.write(USAGE)
    else:
        foo = importlib.import_module(BCH.bname)
        print(foo)

main()
