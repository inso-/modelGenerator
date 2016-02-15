#!/usr/bin/env python
from src.pydjgenerator import *


class swift(CodeGenerator):

    def __init__(self):
        CodeGenerator.__init__(self)
        self.API = False
        self.extensien_file_out = ".swift"
        self.defaultType = "Int"
        self.construct = True
        self.codeGenericInclude = "import UIKit\n\n"
        self.classTemplate = "class %s: NSObject {\n\n"
        self.classCloser = "}"
        self.commentSyntax = "//"
        self.classVariableTemplate = "\tvar %s: %s!\n"
        self.inverseNameType = True
        self.includeTemplate = "import %s\n"
        self.jsonConstructTemplate = "\tinit(data: NSDictionary)\n\t{\n\t\tsuper.init()\n\t\tself.setValuesForKeysWithDictionary(data as! [String : AnyObject])\n"
        self.jsonConstructCor = False
        self.jsonConstructCorTemplate = ""
        self.jsonConstructCorClose = ""
        self.jsonConstructCorCloseForeign = ""
        self.jsonConstructClose = "\t}\n\n"
        self.arrayConstructCor = True
        self.arrayConstructCorTemplate = "\tclass func ObjectArrayFromArray(src : Array<NSDictionary>) -> Array<%s>\n\t{\n\t\tvar res : Array<%s> = Array<%s>()\n\t\tfor elem : NSDictionary in src\n\t\t{\n\t\t\tres.append(%s(data: elem))\n\t\t}\n\t\treturn res\n\t}"
        self.singletonTemplateArg = 3
        self.singletonTemplate = "\tstruct Static {\n\t\tstatic var onceToken : dispatch_once_t = 0\n\t\tstatic var instance : %s? = nil\n\t}\n\n\tlet functionSessionManager:AFHTTPSessionManager\n\n\tclass var sharedInstance : %s{\n\t\tdispatch_once(&Static.onceToken) {\n\t\t\tStatic.instance = %s()\n\t\t}\n\t\treturn Static.instance!\n\t}\n\n"
        self.singletonImplemTemplate = ""
        self.arrayTemplate = "[%s]"
        self.replace = [":", "."]
        self.typeTable = {
            "CharField": "String",
            "TextField": "String",
            "IntegerField": "Int",
            "DecimalField": "Int",
            "PositiveSmallIntegerField": "Int",
            "BigIntegerField": "Double",
            "BooleanField": "Bool",
            "DateField": "Date",
            "DateTimeField": "Date",
            "ListField": "Array = [Int]()",
        }