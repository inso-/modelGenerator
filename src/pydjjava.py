#!/usr/bin/env python
from PromptUtils import *

def getTypeJava(varType):
    if "ForeignKey" in varType :
        typeConverted = varType.split("(")[1].replace("'", "").replace(")", "")
#        codeImport = "@import \"" + typeConverted + ".h\"" + "\n"
        return typeConverted, None#codeImport
    
    typeTable = { "models.CharField" : "String",
                  "models.TextField" : "int",
                  "models.IntegerField" : "int",
                  "models.DecimalField": "int",
                  "models.PositiveSmallIntegerField" : "int",
                  "models.BigIntegerField" : "long",
                  "models.BooleanField" : "bool",
                  "models.DateField" : "String",
                  "models.DateTimeField" : "String",
    }
    typeConverted = typeTable.get(varType)
    if typeConverted is None:
        print varType + " not found"
        return "NSInteger", None
    return typeConverted , None

def header():
    code = "//\n"
    code += "//   Generate By modelGenerator\n"
    code += "//   https://github.com/inso-/modelGenerator\n"
    code += "//\n"
    return code

def generateJava(parsed, prompt=False, verbose=False):
    for model in parsed:
        if prompt and not query_yes_no("generate " + model.nameClass + " ?"):
            continue
        javaObject = open("output/" + model.nameClass + ".java", "w")
        
        code = ""
        codeCor = ""
        codeImport = ""
        codeGetterSetter = ""

        codeCor += "public class " + model.nameClass + "{\n\n"
        for varName, varType in  model.var.iteritems():
            typeVar, newImport = getTypeJava(varType)
                
#            if newImport != None:
#                codeImport += newImport
            codeCor += "\tprivate " + typeVar + " " + varName + ";\n"
            codeGetterSetter += "\tpublic " + typeVar + " get" + varName.capitalize() + "() {\n\t\treturn " + varName + ";\n\t}\n\n"
            codeGetterSetter += "\tpublic void set" + varName.capitalize() + "(" + typeVar + " Param" + varName + ") {\n\t\t" + varName + " = Param" + varName + ";\n\t}\n\n"
        codeCor += "\n"

        codeCor += "Public " + model.nameClass + "(){}\n\n"

        codeCor += codeGetterSetter + "}\n"
        
        code += header() + "\n"
        code += codeImport + "\n"
        code += codeCor

            
        javaObject.write(code)

        if verbose:
            print "Generate output/" + model.nameClass + ".java"
