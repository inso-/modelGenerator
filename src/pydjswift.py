#!/usr/bin/env python
from PromptUtils import *

def getTypeSwift(varType):
    if "ForeignKey" in varType :
        typeConverted = varType.split("(")[1].replace("'", "").replace(")", "")
        codeImport = "import " + typeConverted + "\n"
        return typeConverted, codeImport
    
    typeTable = { "models.CharField" : "String",
                  "models.TextField" : "String",
                  "models.IntegerField" : "Int",
                  "models.DecimalField": "Int",
                  "models.PositiveSmallIntegerField" : "Int",
                  "models.BigIntegerField" : "Double",
                  "models.BooleanField" : "Bool",
                  "models.DateField" : "Date",
                  "models.DateTimeField" : "Date",
    }
    typeConverted = typeTable.get(varType)
    if typeConverted is None:
        print varType + " not found"
        return "String", None
    return typeConverted , None

def header():
    code = "//\n"
    code += "//   Generate By modelGenerator\n"
    code += "//   https://github.com/inso-/modelGenerator\n"
    code += "//\n"
    return code

def generateSwift(parsed, prompt=False, verbose=False):
    for model in parsed:
        if prompt and not query_yes_no("generate " + model.nameClass + " ?"):
            continue
        swiftFile = open("output/" + model.nameClass + ".swift", "w")
        
        code = ""
        codeCor = ""
        codeImport = ""

        codeCor += "Class " + model.nameClass + " {\n\n"
        
        for varName, varType in  model.var.iteritems():
            typeVar, newImport = getTypeSwift(varType)

            if newImport != None:
                codeImport += newImport 

            codeCor += "\tlet " + varName + ": " + typeVar + "\n"
        codeCor += "\t}" 
            
        code += header() + "\n"
        code += codeImport + "\n"
        code += codeCor

        swiftFile.write(code)

        if verbose:
            print "Generate output/" + model.nameClass + ".swift"
