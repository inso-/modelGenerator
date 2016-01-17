#!/usr/bin/env python
from src.pydjgenerator import CodeGenerator


class objc(CodeGenerator):

    def __init__(self):
        CodeGenerator.__init__(self)
        self.implem_out = True
        self.extensien_file_out = ".h"
        self.extensien_implem_out = ".m"
        self.defaultType = "NSInteger"
        self.include_foreign = True
        self.classTemplate = "@interface %s : NSObject\n\n"
        self.classCloser = "@end"
        self.commentSyntax = "//"
        self.classVariableTemplate = "@property(nonatomic, strong) %s *%s;\n"
        self.includeTemplate = "@import \"%s" + self.extensien_file_out + "\"\n"
        self.implemTemplate = "@implementation %s"
        self.typeTable = {
            "CharField": "NSString",
            "TextField": "NSString",
            "IntegerField": "NSInteger",
            "DecimalField": "NSInteger",
            "PositiveSmallIntegerField": "NSInteger",
            "BigIntegerField": "NSInteger",
            "BooleanField": "NSInteger",
            "DateField": "NSDate",
            "DateTimeField": "NSDate",
            "ListField": "NSMutableArray",
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