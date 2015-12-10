#!/usr/bin/env python

import parser

class DjangoModel:
    nameClass = "lol"
    var = {}

    def __init__(self):
        self.nameClass = ""
        self.var = {}

    def setClassName(self, className):
        self.nameClass = className
        
    def addFunc(self, Name, Type):
        self.var[Name] = Type

pyFile = open("out.py", 'r')
inClass = False
inMeta = False
ClassName = ""
parsed = []
tmpModel = DjangoModel()

for line in pyFile.readlines():
    if line[0:5] == "class":
        if inClass == True:
            parsed.append(tmpModel)
            inMeta = False;
            tmpModel = DjangoModel()
        else:
            inClass = True
            inMeta = False;
        className = line[6:].split("(")[0]
        tmpModel.setClassName(className)
        
    if "Meta" in line:
        inMeta = True;

    if inClass == True and inMeta == False and "=" in line:
        varName = line.split("=")[0].replace(" ", "")
        if "ForeignKey" in line:
            varType = line.split("=")[1].split(",")[0].replace(" ", "").replace("\n", "")
        else:
            varType = line.split("=")[1].split("(")[0].replace(" ", "").replace("\n", "")
        tmpModel.addFunc(varName, varType)

def getTypeObjc(varType):
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

def generateObjc():
    for model in parsed:
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
                varName = "_description";
                
            if newImport != None:
                codeImport += newImport 
            codeCor += "@property(nonatomic, strong) " + typeVar + " *" + varName + ";\n"
        codeCor += "\n@end"

        code += header() + "\n"
        code += codeImport + "\n"
        code += codeCor

        objcHeader.write(code)

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

generateObjc()
