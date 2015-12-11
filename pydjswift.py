#!/usr/bin/env python

from ParsePyModel import *

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
    code += "//   Generate By \n"
    code += "//   Thomas Moussajee software\n"
    code += "//\n"
    return code

def generateObjc(parsed):
    for model in parsed:
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

def main():
    n = ParsePyModel("out.py")
    generateObjc(n.parse())

main()
