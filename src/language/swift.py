#!/usr/bin/env python
from src.pydjgenerator import *


class swift(CodeGenerator):

    def __init__(self):
        CodeGenerator.__init__(self)
        self.extensien_file_out = ".swift"
        self.defaultType = "Int"
        self.include_foreign = True
        self.classTemplate = "Class %s {\n\n"
        self.classCloser = "}"
        self.commentSyntax = "//"
        self.classVariableTemplate = "\tlet %s: %s\n"
        self.includeTemplate = "import %s\n"
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