#!/usr/bin/env python
import sys, inspect
from settings import  *
from parser.ParsePyModel import ParsePyModel
from parser.ParseJson import ParseJson
from language import *
from language.language import language as planguage


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

    for lang in planguage:
        #print globals()
        print lang
        klass = inspect.getmembers(globals()[lang], inspect.isclass)[1][1]
        #print klass[1][1]
        toGenerate = globals()[lang.upper()]
        prompt = globals()[lang.upper() + "_PROMPT"]
        if (toGenerate == 1 or prompt == 1):
            #print type(klass[1][1])
            klass().generate(n.parsed, prompt, verbose)

main()
