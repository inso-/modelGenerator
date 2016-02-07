#!/usr/bin/env python
import sys, inspect
from settings import *
from parser.ParsePyModel import ParsePyModel
from parser.ParseJson import ParseJson
from parser.ParseRaml import ParseRaml
from parser.ParseDescJson import ParseDescJson
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

    print "Source : %s" % fileName

    if ".py" in fileName:
        n = ParsePyModel(fileName)
    elif ".json" in fileName:
        n = ParseJson(fileName)
    elif ".japi" in fileName:
        n = ParseDescJson(fileName)
    elif ".raml" in fileName:
        n = ParseRaml(fileName)
    else:
        print("Usage:\n\t\t./" + __file__ + " [PyModel or json InputFile] \n\t\t -v Verbose Mode")
        return

    n.parse()
    run_generate(n, verbose)

def run_generate(data, verbose):
    for lang in planguage:
        klass = inspect.getmembers(globals()[lang], inspect.isclass)[1][1]
        toGenerate = globals()[lang.upper()]
        prompt = globals()[lang.upper() + "_PROMPT"]
        if (toGenerate == 1 or prompt == 1):
            gen = klass()
            run_generate_api(gen, data, verbose, prompt)
            run_generate_model(gen, data, verbose, prompt)

def run_generate_api(gen, data, verbose, prompt):
    if gen.API is False or data.parsedAPI is None:
        return
    gen.generateAPI(data.parsedAPI, prompt, verbose)


def run_generate_model(gen, data, verbose, prompt):
    if (data.parsedModel != None):
        gen.generate(data.parsedModel, prompt, verbose)


main()
