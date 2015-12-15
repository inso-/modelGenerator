#!/usr/bin/env python
from ParsePyModel import *
from ParseJson import *
from language import *
from settings import *
import sys


def main():
    verbose = False
    if (len(sys.argv) > 1):
        if len(sys.argv) > 2 and "-v" in sys.argv[1]:
            verbose = True
            fileName = sys.argv[2]
        elif len(sys.argv) > 2 and "-v" in sys.argv[2]:
            verbose = True
            fileName = sys.argv[1]
        else:
            fileName = sys.argv[1]
    else:
        print("Usage:\n\t\t./" + __file__ + " [PyModel or json InputFile] \n\t\t -v Verbose Mode")
        return

    if ".py" in fileName:
        n = ParsePyModel(fileName)
        n.parse()
    elif ".json" in fileName:
        n = ParseJson(fileName)
        n.parse()
    else:
        print("Usage:\n\t\t./" + __file__ + " [PyModel or json InputFile] \n\t\t -v Verbose Mode")
        return

    for lang in language:
        klass = globals()[lang]

        toGenerate = globals()[lang.upper()]
        prompt = globals()[lang.upper() + "_PROMPT"]
        if (toGenerate == 1 or prompt == 1):
            klass().generate(n.parsed, prompt, verbose)

main()
