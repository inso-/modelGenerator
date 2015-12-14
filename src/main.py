#!/usr/bin/env python
from ParsePyModel import *
from language import *
from settings import *
import sys


def main():
    verbose = False
    if (len(sys.argv) > 1):
        if "-v" in sys.argv[1]:
            verbose = True
            fileName = sys.argv[2]
        elif "-v" in sys.argv[2]:
            verbose = True
            fileName = sys.argv[1]
        else:
            fileName = sys.argv[1]
    else:
        print("Usage:\n\t\t./" + __file__ + " PyModelFile\n\t\t -v Verbose Mode")
        return

    n = ParsePyModel(fileName)
    n.parse()

    for lang in language:
        klass = globals()[lang]

        toGenerate = globals()[lang.upper()]
        prompt = globals()[lang.upper() + "_PROMPT"]
        if (toGenerate == 1 or prompt == 1):
            klass().generate(n.parsed, prompt, verbose)

main()
