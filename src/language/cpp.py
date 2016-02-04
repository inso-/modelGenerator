#!/usr/bin/env python
import sys
sys.path.append('../.')
from pydjgenerator import CodeGenerator


class cpp(CodeGenerator):

    def __init__(self):
        CodeGenerator.__init__(self)
        self.implem_out = True
        self.extensien_file_out = ".hh"
        self.extensien_implem_out = ".cpp"
        self.defaultType = "int"
        self.include_foreign = True
        self.classTemplate = "class %s : public class model\n{\n"
        self.classCloser = "}"
        self.commentSyntax = "//"
        self.classVariableTemplate = "public : %s %s;\n"
        self.includeTemplate = "#include \"%s" + self.extensien_file_out + "\"\n"
        self.implemTemplate = "class %s{\n"
        self.typeTable = {
            "EmailField": "CString",
            "FileField": "CString",
            "FilePathField": "CString",
            "CharField": "CString",
            "FieldFile": "CString",
            "URLField": "CString",
            "GenericIPAddressField": "CString",
            "SlugField": "CString",
            "ImageField": "CString",
            "IntegerField": "long",
            "AutoField": "long",
            "PositiveIntegerField": "unsigned long",
            "PositiveSmallIntegerField": "unsigned long",
            "SmallIntegerField": "long",
            "DurationField": "CString",
            "BigIntegerField": "CString",
            "BinaryField": "CByteArray",
            "BooleanField": "BOOL",
            "NullBooleanField": "BOOL",
            "DateField": "CString",
            "DateTimeField": "CTime",
            "DecimalField": "CString",
            "FloatField": "double",
            "TextField": "CString",
            "TimeField": "CTime",
            "UUIDField": "CString",
            "CommaSeparatedIntegerField": "",
            }