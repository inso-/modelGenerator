#!/usr/bin/env python
from pydjgenerator import *


class csharp(CodeGenerator):

    def __init__(self):
        super.__init__(self)
        self.extensien_file_out = ".cs"
        self.defaultType = "int"
        self.include_foreign = False
        self.classTemplate = "public class %s\n{\n"
        self.classCloser = "}"
        self.commentSyntax = "//"
        self.classVariableTemplate = "\tpublic %s %s { get; set; }\n"
        self.includeTemplate = ""
        self.typeTable = {
            "CharField": "string",
            "TextField": "string",
            "IntegerField": "int",
            "DecimalField": "int",
            "PositiveSmallIntegerField": "int",
            "BigIntegerField": "double",
            "BooleanField": "bool",
            "DateField": "DateTime",
            "DateTimeField": "DateTime",
        }