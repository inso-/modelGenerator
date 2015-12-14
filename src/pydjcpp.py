#!/usr/bin/env python
from pydjgenerator import CodeGenerator


class cpp(CodeGenerator):

    def __init__(self):
        CodeGenerator.__init__(self)
        self.implem_out = True
        self.extensien_file_out = ".hh"
        self.extensien_implem_out = ".cpp"
        self.defaultType = "int"
        self.include_foreign = True
        self.classTemplate = "class %s\n{\n"
        self.classCloser = "}"
        self.commentSyntax = "//"
        self.classVariableTemplate = "public : %s %s;\n"
        self.includeTemplate = "#include \"%s" + self.extensien_file_out + "\"\n"
        self.implemTemplate = "class %s{\n"
        self.typeTable = {
            "CharField": "String",
            "TextField": "String",
            "IntegerField": "int",
            "DecimalField": "int",
            "PositiveSmallIntegerField": "int",
            "BigIntegerField": "double",
            "BooleanField": "bool",
            "DateField": "date",
            "DateTimeField": "date",
        }