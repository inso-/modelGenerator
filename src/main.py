#!/usr/bin/env python
from settings import *
from ParsePyModel import *
from pydjobjc import *
from pydjswift import *
from pydjjava import *
from pydjcsharp import *
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
    if (OBJC or OBJC_PROMPT):
        generateObjc(n.parsed, OBJC_PROMPT, verbose)
    if (SWIFT or SWIFT_PROMPT):
        generateSwift(n.parsed, SWIFT_PROMPT, verbose)
    if (JAVA or JAVA_PROMPT):
        generateJava(n.parsed, JAVA_PROMPT, verbose)
    if (CSHARP or CSHARP_PROMPT):
        generateCsharp(n.parsed, CSHARP_PROMPT, verbose)

main()
