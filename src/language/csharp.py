#!/usr/bin/env python
from src.pydjgenerator import *


class csharp(CodeGenerator):

    def __init__(self):
        CodeGenerator.__init__(self)
        self.extensien_file_out = ".cs"
        self.defaultType = "int"
        self.include_foreign = False
        self.classTemplate = "public class %s : model\n{\n"
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
            "ListField": "list<model>",
        }
        ##        self.typeTable = {
##            "AutoField": "" ,
##            "BigIntegerField": "" ,
##            "BinaryField": "" ,
##            "BooleanField": "" ,
##            "CharField": "" ,
##            "CommaSeparatedIntegerField": "" ,
##            "DateField": "" ,
##            "DateTimeField": "" ,
##            "DecimalField": "" ,
##            "DurationField": "" ,
##            "EmailField": "" ,
##            "FileField": "" ,
##            "FileField and FieldFile": "" ,
##            "FilePathField": "" ,
##            "FloatField": "" ,
##            "ImageField": "" ,
##            "IntegerField": "" ,
##            "GenericIPAddressField": "" ,
##            "NullBooleanField": "" ,
##            "PositiveIntegerField": "" ,
##            "PositiveSmallIntegerField": "" ,
##            "SlugField": "" ,
##            "SmallIntegerField": "" ,
##            "TextField": "" ,
##            "TimeField": "" ,
##            "URLField": "" ,
##            "UUIDField": "" ,
##            }