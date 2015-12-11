#!/usr/bin/env python

from ParsePyModel import *

def getTypeSwift(varType):
    if "ForeignKey" in varType :
        typeConverted = varType.split("(")[1].replace("'", "").replace(")", "")
        codeImport = "@import " + typeConverted + ".h" + "\n"
        return typeConverted, codeImport
    
    typeTable = { "models.CharField" : "NSString",
                  "models.TextField" : "NSString",
                  "models.IntegerField" : "NSInteger",
                  "models.DecimalField": "NSInteger",
                  "models.PositiveSmallIntegerField" : "NSInteger",
                  "models.BigIntegerField" : "NSInteger",
                  "models.BooleanField" : "NSInteger",
                  "models.DateField" : "NSDate",
                  "models.DateTimeField" : "NSDate",
    }
    typeConverted = typeTable.get(varType)
    if typeConverted is None:
        print varType + " not found"
        return "NSInteger", None
    return typeConverted , None

def header():
    code = "//\n"
    code += "//   Generate By \n"
    code += "//   Thomas Moussajee software\n"
    code += "//\n"
    return code

