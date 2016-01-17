import time
import sys
sys.path.append('.')
from src.utils.PromptUtils import *


class CodeGenerator():
    file_implem_out = None
    file_out = None
    extensien_file_out = None
    extensien_implem_out = None
    typeTable = {}
    jsontypeTable = {}
    defaultType = ""
    defaultjsonType = ""
    implem_out = False
    include_foreign = False
    getter_setter = False
    construct = False
    serialize = False
    header_file = False
    inverseNameType = False
    code = ""
    codeHeader = ""
    codeConstruct = ""
    codeSerialize = ""
    codeGenericInclude = ""
    codeInclude = ""
    codeCor = ""
    codeGetterSetter = ""
    outputDirectory = "output/"
    classTemplate = ""
    classCloser = ""
    commentSyntax = ""
    classVariableTemplate = ""
    includeTemplate = ""
    implemTemplate = ""
    defaultConstructTemplate = ""
    jsonConstructTemplate = ""
    jsonConstructCorTemplate = ""
    jsonConstructCorClose = ""
    jsonConstructCorCloseForeign = ""
    jsonConstructCloseTemplate = ""
    serializeTemplate = ""
    serializeCorTemplate = ""
    foreignKeySerializeTemplate = ""
    serializeConditionTemplate = ""
    getterTemplate = ""
    setterTemplate = ""
    jsonConstructClose = ""
    serializeClose = ""

    def __init__(self):
        pass

    def getType(self, varType):
        if "ForeignKey" in varType:
            typeConverted = varType.split("(")[1].replace("'", "").replace(")", "")
            if self.include_foreign:
                self.codeInclude += self.includeTemplate % typeConverted
            return typeConverted
        varType = varType.replace("models.", "")
        typeConverted = self.typeTable.get(varType)
        if typeConverted is None:
            print varType + " not found"
            return self.defaultType
        return typeConverted

    def getJsonType(self, varType):
        if "ForeignKey" in varType:
            typeConverted = varType.split("(")[1].replace("'", "").replace(")", "")
            return  "new " + typeConverted + "(data.optJSONObject",
        varType = varType.replace("models.", "")
        jsonConverter = self.jsontypeTable.get(varType)
        if jsonConverter is None:
            print varType + " jsonAdapter not found"
            jsonConverter = "data." + self.defaultjsonType
        return "data." + jsonConverter

    def generateHeader(self, filename):
        self.codeHeader = ""
        self.codeHeader = "%s\n" % self.commentSyntax
        self.codeHeader += "%s\t%s Generate By modelGenerator\n" % (self.commentSyntax, filename)
        self.codeHeader += "%s\tCreate the %s\n" % (self.commentSyntax, time.strftime("%c"))
        self.codeHeader += "%s\thttps://github.com/inso-/modelGenerator\n" % self.commentSyntax
        self.codeHeader += "%s\n" % self.commentSyntax

    def generateCor(self, model):
        self.codeCor = self.classTemplate % model.nameClass
        for varName, varType in model.var.iteritems():
                typeVar = self.getType(varType)
                if self.inverseNameType == 1:
                    self.codeCor += self.classVariableTemplate % (varName, typeVar)
                else:
                    self.codeCor += self.classVariableTemplate % (typeVar, varName)
                if self.getter_setter:
                    self.generateGetterSetter(typeVar, varName)
                if self.construct:
                    self.generateConstruct(varType, varName)
                if self.serialize:
                    self.generateSerialize(varType, varName)
        if self.construct:
            self.codeConstruct += self.jsonConstructClose
        if self.serialize:
            self.codeSerialize += self.serializeClose

    def generateGetterSetter(self, typeVar, varName):
        self.codeGetterSetter += self.getterTemplate % (typeVar, varName.capitalize(), varName)
        self.codeGetterSetter += self.setterTemplate % (varName.capitalize(), typeVar, varName, varName, varName)

    def generateConstruct(self, varType, varName):
        jsontypeVar = self.getJsonType(varType)
 #       if "List" in varType:
 #           return
        self.codeConstruct += self.jsonConstructCorTemplate % (varName, jsontypeVar, varName)
        if "(" in jsontypeVar:
            self.codeConstruct += self.jsonContructCorCloseForeign
        else:
            self.codeConstruct += self.jsonConstructCorClose

    def generateSerialize(self, varType, varName):
#        if "List" in varType:
#            return
        if "foreign" in varType:
                self.codeSerialize += self.serializeConditionTemplate % (varName, varName)
                self.codeSerialize += self.foreignKeySerializeTemplate % varName
        else:
                self.codeSerialize += self.serializeCorTemplate % (varName, varName)


    def generate(self, parsed, prompt=False, verbose=False):
        for model in parsed:
            if prompt and not query_yes_no("generate " + model.nameClass + " ?"):
                continue
            self.generateFile(model)
            if verbose:
                print "Generate " + self.outputDirectory + model.nameClass + self.extensien_file_out
            if self.implem_out:
                self.generateImplemFile(model)
                if verbose:
                    print "Generate output/" + model.nameClass + ".m"

    def initConstruct(self, model):
        self.codeConstruct = ""
        self.codeConstruct += self.defaultConstructTemplate % model.nameClass
        self.codeConstruct += self.jsonConstructTemplate % model.nameClass

    def initSerialize(self, model):
        self.codeSerialize = ""
        self.codeSerialize += self.serializeTemplate

    def generateImplemFile(self, model):
        self.file_implem_out = open(self.outputDirectory + model.nameClass + self.extensien_implem_out, "w")
        self.generateHeader(model.nameClass + self.extensien_implem_out)
        self.code = ""
        self.codeCor = ""
        self.codeInclude = ""
        self.codeInclude += self.includeTemplate % model.nameClass
        self.codeCor +=  self.implemTemplate % model.nameClass
        self.codeCor += "\n" + self.classCloser
        self.code += self.codeHeader + "\n"
        self.code += self.codeInclude + "\n"
        self.code += self.codeCor
        self.file_implem_out.write(self.code)

    def generateFile(self, model):
        self.file_out = open(self.outputDirectory + model.nameClass + self.extensien_file_out, "w")
        self.code = ""
        self.codeInclude = ""
        self.codeCor += self.classTemplate % model.nameClass
        self.generateHeader(model.nameClass + self.extensien_file_out)
        if self.construct:
            self.initConstruct(model)
        if self.serialize:
            self.initSerialize(model)
        self.generateCor(model)
        self.code += self.codeHeader + "\n"
        if self.include_foreign:
            self.code += self.codeInclude + "\n"
        self.code += self.codeCor + "\n"
        if self.construct:
            self.code += self.codeConstruct + "\n"
        if self.serialize:
            self.code += self.codeSerialize + "\n"
        if self.getter_setter:
            self.code += self.codeGetterSetter + "\n"
        self.code += self.classCloser
        self.file_out.write(self.code)
