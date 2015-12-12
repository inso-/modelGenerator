#!/usr/bin/env python
from PromptUtils import *

def getTypeObjc(varType):
    if "ForeignKey" in varType :
        typeConverted = varType.split("(")[1].replace("'", "").replace(")", "")
        codeImport = "@import \"" + typeConverted + ".h\"" + "\n"
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

def generateObjc(parsed, prompt=False, verbose=False):
    for model in parsed:
        if prompt and not query_yes_no("generate " + model.nameClass + " ?"):
            continue
        objcHeader = open("output/" + model.nameClass + ".h", "w")
        
        code = ""
        codeCor = ""
        codeImport = ""

        codeCor += "@interface " + model.nameClass + " : " + "NSObject\n\n"
        for varName, varType in  model.var.iteritems():
            typeVar, newImport = getTypeObjc(varType)
            if varName == "id":
                varName = "_id"
            elif varName == "description":
                varName = "_description"
                
            if newImport != None:
                codeImport += newImport 
            codeCor += "@property(nonatomic, strong) " + typeVar + " *" + varName + ";\n"
        codeCor += "\n@end"

        code += header() + "\n"
        code += codeImport + "\n"
        code += codeCor

            
        objcHeader.write(code)

        if verbose:
            print "Generate output/" + model.nameClass + ".h"

        objcClass = open("output/" + model.nameClass + ".m", "w")
        code = ""
        codeCor = ""
        codeImport = ""

        codeImport += "@import \"" + model.nameClass + ".h\"" + "\n"
        codeCor += "@implementation " + model.nameClass 
        codeCor += "\n@end"

        code += header() + "\n"
        code += codeImport + "\n"
        code += codeCor

        objcClass.write(code)
        
        if verbose:
            print "Generate output/" + model.nameClass + ".m"
