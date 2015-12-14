#!/usr/bin/env python
from PromptUtils import *

def getTypeCsharp(varType):
    if "ForeignKey" in varType :
        typeConverted = varType.split("(")[1].replace("'", "").replace(")", "")
        codeImport = "" # "@import \"" + typeConverted + ".h\"" + "\n"
        return typeConverted, codeImport
    
    typeTable = { "models.CharField" : "string",
                  "models.TextField" : "string",
                  "models.IntegerField" : "int",
                  "models.DecimalField": "int",
                  "models.PositiveSmallIntegerField" : "int",
                  "models.BigIntegerField" : "double",
                  "models.BooleanField" : "bool",
                  "models.DateField" : "DateTime",
                  "models.DateTimeField" : "DateTime",
    }
    typeConverted = typeTable.get(varType)
    if typeConverted is None:
        print varType + " not found"
        return "intr", None
    return typeConverted , None

def header():
    code = "//\n"
    code += "//   Generate By modelGenerator\n"
    code += "//   https://github.com/inso-/modelGenerator\n"
    code += "//\n"
    return code

def generateCsharp(parsed, prompt=False, verbose=False):
    for model in parsed:
        if prompt and not query_yes_no("generate " + model.nameClass + " ?"):
            continue
        csharpFile = open("output/" + model.nameClass + ".cs", "w")
        
        code = ""
        codeCor = ""
        
        codeImport = ""

        codeCor += "public class " + model.nameClass + "\n{\n"
        for varName, varType in  model.var.iteritems():
            typeVar, newImport = getTypeCsharp(varType)
                
            if newImport != None:
                codeImport += newImport 
            codeCor += "\tpublic  " + typeVar + " " + varName + " { get; set; }\n"
        codeCor += "}"

        code += header() + "\n"
        code += codeImport + "\n"
        code += codeCor

            
        csharpFile.write(code)

        if verbose:
            print "Generate output/" + model.nameClass + ".cs"
