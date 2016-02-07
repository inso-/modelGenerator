#!/usr/bin/env python
from src.pydjgenerator import *


class swift(CodeGenerator):

    def __init__(self):
        CodeGenerator.__init__(self)
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
        self.jsonConstructClose = "\t}\n"
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