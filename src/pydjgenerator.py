import time
import sys
sys.path.append('.')
from src.utils.PromptUtils import *
import itertools
import os

class CodeGenerator():
    API = False
    APIImplemin_out = False
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
    foreignSpecific = False
    include_lib = False
    jsonConstructCor = False
    code = ""
    codeHeader = ""
    codeConstruct = ""
    codeSerialize = ""
    codeGenericInclude = ""
    codeInclude = ""
    codeCor = ""
    codeGetterSetter = ""
    outputDirectory = "output/"
    APIclassTemplate = ""
    APIsingleton = False
    APIvariable = ""
    singletonTemplate = ""
    classTemplate = ""
    classCloser = ""
    commentSyntax = ""
    classVariableTemplate = ""
    classVariableForeignTemplate = ""
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
    APImethodTemplateOpen = ""
    APImethodTemplateClose = ""
    APImethodParamTemplate = ""
    APImethodImplemTemplateOpen = ""
    APImethodImplemTemplateClose = ""
    APImethodImplemParamTemplate = ""
    paramSeparator = ""

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
                if "ForeignKey" in varType and self.foreignSpecific:
                    if self.inverseNameType:
                        self.codeCor += self.classVariableForeignTemplate % (varName, typeVar, varName)
                    else:
                        self.codeCor += self.classVariableForeignTemplate % (typeVar, varName, varName)
                else:
                    if self.inverseNameType == 1:
                        self.codeCor += self.classVariableTemplate % (varName, typeVar)
                    else:
                        self.codeCor += self.classVariableTemplate % (typeVar, varName)
                if self.getter_setter:
                    self.generateGetterSetter(typeVar, varName)
                if self.construct and self.jsonConstructCor is not False:
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
        lang = self.__class__.__name__
        path = self.outputDirectory + lang + "/model/"
        mkdir_p(path)
        for model in parsed:
            if prompt and not query_yes_no("generate " + model.nameClass + " ?"):
                continue
            self.generateFile(model)
            if verbose:
                print "Generate " + path + model.nameClass + self.extensien_file_out
            if self.implem_out:
                self.generateImplemFile(model)
                if verbose:
                    print "Generate " + path + model.nameClass + self.extensien_implem_out

    def initConstruct(self, model):
        self.codeConstruct = ""
        #self.codeConstruct += self.defaultConstructTemplate % model.nameClass
        if (self.jsonConstructCor != False):
            self.codeConstruct += self.jsonConstructTemplate % model.nameClass
        else:
            self.codeConstruct += self.jsonConstructTemplate

    def initSerialize(self, model):
        self.codeSerialize = ""
        self.codeSerialize += self.serializeTemplate



    def generateImplemFile(self, model):
        lang = self.__class__.__name__
        path = self.outputDirectory + lang + "/model/"
        self.file_implem_out = open(path + model.nameClass + self.extensien_implem_out, "w")
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
        lang = self.__class__.__name__
        path = self.outputDirectory + lang + "/model/"
        self.file_out = open(path + model.nameClass + self.extensien_file_out, "w")
        self.code = ""
        self.codeInclude = self.codeGenericInclude
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

    def generateAPICor(self, api):
        title = api.title.replace(" ", "") + "Client"
        if self.APIsingleton:
            if self.singletonTemplateArg == 2:
                self.codeCor += self.singletonTemplate % (title, title)
            elif self.singletonTemplateArg == 3:
                self.codeCor += self.singletonTemplate % (title, title, title)
            if self.APIImplemin_out:
                self.codeCor += self.baseURLImplemTemplate % api.baseURL
        self.codeCor += self.APIVariable
        #url = api.baseUrl
        for route in api.route:
            if "{" in route.url:
                a = route.url.split("{")[1].replace("}", "")
                paramUrl = 0
                if "," in a:
                    param = a.split(",")
                    paramUrl = len(param)
                else:
                    paramUrl = 1;
                    param = []
                    param.append(a)

                self.codeCor += self.APImethodTemplateOpen % ((route.method + route.url).replace("/", "_").replace("{", "_").replace("__", "_").replace("}", ""))
                i = 0
                while (i < paramUrl):
                        if (i > 1):
                            self.codeCor += self.paramSeparator
                        self.codeCor += self.APImethodParamTemplate % param[i]
                        i = i + 1

                if self.APIImplemin_out:
                    self.codeCor += self.APImethodImplemTemplateOpen
                    self.codeCor += self.APImethodImplemTemplate % (route.method.upper(), route.url.replace("{", "\" + ").replace("}", ""))
                    self.codeCor += self.APImethodImplemTemplateClose


                self.codeCor += self.APImethodTemplateClose

        pass



    def generateAPIImplemCOR(self, api):
        title = api.title.replace(" ", "") + "Client"
        if self.APIsingleton:
            self.codeCor += self.singletonImplemTemplate % (title, title, title)
            self.codeCor += self.baseURLImplemTemplate % api.baseURL
        for route in api.route:
            codeRouteparam = ""
            codeRoute = ""
            paramUrl = 0
            if "{" in route.url:
                a = route.url.split("{")[1]
                url = route.url.split("{")[1].replace("}", "")
                b = route.url.split("{")[0]
                if "," in a:
                    codeRouteFormat = self.APIParamURLTemplate % b
                    param = a.split(",")

                    for p in param:
                        codeRouteFormat += self.formatFlag
                        codeParam = p + self.callParamSeparator
                    codeRouteFormat += self.paramCloser
                    codeRoute += self.APIManyParamURLTemplate % (codeRouteFormat ,codeParam[:-1])

                else:
                    paramUrl = 1;
                    param = []
                    param.append(url)
                    codeRoute =  self.APIOneParamURLTemplate % (b , param[0])

            self.codeCor += self.APImethodDefineImplemTemplateOpen % ((route.method + route.url).replace("/", "_").replace("{", "_").replace("__", "_").replace("}", ""))
            i = 0
            while (i < paramUrl):
                    if (i > 1):
                        self.codeCor += self.paramSeparator
                    self.codeCor += self.APImethodParamTemplate % param[i]
                    i = i + 1
            self.codeCor += self.APImethodDefineImplemTemplateClose
            self.codeCor += self.APImethodImplemTemplateOpen
            self.codeCor += self.APImethodImplemTemplate % (route.method.upper(), codeRoute)
            self.codeCor += self.APImethodImplemTemplateClose

    #def generateAPICor(self, api):
    #    title = api.title.replace(" ", "") + "Client"
    #    if self.APIsingleton:
    #        self.codeCor += self.singletonTemplate % (title, title)
    #    self.codeCor += self.APIVariable
    #    #url = api.baseUrl
    #    for route in api.resources.__iter__():
    #        print route
    #        print api.resources[route]
    #        if "{" in route:
    #            a = route.split("{")[1].replace("}", "")
    #            if "," in a:
    #                param = a.split(",")
    #                paramUrl = len(param)
    #            else:
    #                paramUrl = 1;
    #                param = []
    #                param.append(a)
    #
    #        for method in api.resources[route].methods:
    #            print method
    #            print api.resources[route].methods[method]
    #            self.codeCor += self.APImethodTemplateOpen % ((method + route).replace("/", "_").replace("{", "_").replace("__", "_").replace("}", ""))
    #            i = 0
    #            while (i < paramUrl):
    #                    if (i > 1):
    #                        self.codeCor += self.paramSeparator
    #                    self.codeCor += self.APImethodParamTemplate % param[i]
    #                    i = i + 1
    #            self.codeCor += self.APImethodTemplateClose
    #    pass

    #def generateAPIImplemCOR(self, api):
    #    title = api.title.replace(" ", "") + "Client"
    #    if self.APIsingleton:
    #        self.codeCor += self.singletonImplemTemplate % (title, title, title)
    #        if '{' in api.baseUri:
    #            b = api.baseUri.split("{")[1].replace("}", "")
    #            print b
    #            url = api.baseUri.split("{")[0] + str(getattr(api, b))
    #        self.codeCor += self.baseURLImplemTemplate % url
    #    for route in api.resources.__iter__():
    #        print route
    #        print api.resources[route]
    #        codeRouteparam = ""
    #        codeRoute = ""
    #        if "{" in route:
    #            a = route.split("{")[1].replace("}", "")
    #            b = route.split("{")[0]
    #            if "," in a:
    #                codeRouteFormat = '[NSString stringwithformat: @"' + b + '",' + '@"'
    #                param = a.split(",")
    #                paramUrl = len(param)
    #
    #                for p in param:
    #                    codeRouteFormat += "%@/"
    #                    codeRouteparam += ""
    #                    codeParam = p + ","
    #                codeRouteFormat += '"]'
    #                codeRoute += '[NSString stringwithformat:@"' + codeRouteFormat + '",' + codeParam[:-1] + "]"
    #
    #            else:
    #                paramUrl = 1;
    #                param = []
    #                param.append(a)
    #                codeRoute = '[NSString stringwithformat:@"' + b + '%s",' + param[0] + '"]'
    #
    #
    #        for method in api.resources[route].methods:
    #            print method
    #            print api.resources[route].methods[method]
    #            self.codeCor += self.APImethodDefineImplemTemplateOpen % ((method + route).replace("/", "_").replace("{", "_").replace("__", "_").replace("}", ""))
    #            i = 0
    #            while (i < paramUrl):
    #                    if (i > 1):
    #                        self.codeCor += self.paramSeparator
    #                    self.codeCor += self.APImethodParamTemplate % param[i]
    #                    i = i + 1
    #            self.codeCor += self.APImethodDefineImplemTemplateClose
    #            self.codeCor += self.APImethodImplemTemplateOpen
    #            self.codeCor += self.APImethodImplemTemplate % (method.upper(), codeRoute)
    #            self.codeCor += self.APImethodImplemTemplateClose
    #    pass
    #
    #    #self.codeCor +=  self.implemTemplate % title
    #    #self.codeCor += "\n" + self.classCloser
    #    pass
    #


    def generateAPIFile(self, api):
        lang = self.__class__.__name__
        path = self.outputDirectory + lang + "/API/"
        mkdir_p(path)
        title = api.title.replace(" ", "") + "Client"
        self.file_out = open(path + title + self.extensien_file_out, "w")
        self.code = ""
        self.codeInclude = ""
        self.codeCor += self.APIclassTemplate % title
        self.generateHeader(title + self.extensien_file_out)
        self.generateAPICor(api)
        self.code += self.codeHeader + "\n"
        if self.include_lib:
            self.code += self.codeInclude + "\n"
        self.code += self.codeCor + "\n"
        self.code += self.classCloser
        self.file_out.write(self.code)
        pass

    def generateAPIImplemFile(self, api):
        lang = self.__class__.__name__
        path = self.outputDirectory + lang + "/API/"
        mkdir_p(path)
        title = api.title.replace(" ", "") + "Client"
        self.file_implem_out = open(path + title + self.extensien_implem_out, "w")
        self.generateHeader(title + self.extensien_implem_out)
        self.code = ""
        self.codeCor = ""
        self.codeInclude = ""
        self.codeInclude += self.includeTemplate % title
        self.generateAPIImplemCOR(api)
        self.code += self.codeHeader + "\n"
        self.code += self.codeInclude + "\n"
        self.code += self.codeCor
        self.file_implem_out.write(self.code)
        pass

    def generateAPI(self, parsed, prompt=False, verbose=False):
        title = parsed.title.replace(" ", "") + "Client"
        lang = self.__class__.__name__
        path = self.outputDirectory + lang + "/API/"
        mkdir_p(path)
        if prompt and not query_yes_no("generate " + title + " ?"):
            return
        self.generateAPIFile(parsed)
        if verbose:
            print "Generate " + path + title + self.extensien_file_out
        if self.implem_out:
            self.generateAPIImplemFile(parsed)
            if verbose:
                print "Generate " + path + title + self.extensien_implem_out

#        print n.parsed.title
#        print n.parsed.documentation
#        print n.parsed.baseUri
#        print n.parsed.resources
#        print type(n.parsed.resources)



    pass

import errno
import os


def mkdir_p(path):
    if os.path.exists(path):
        return
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise