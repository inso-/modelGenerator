#!/usr/bin/env python
from src.pydjgenerator import CodeGenerator


class objc(CodeGenerator):

    def __init__(self):
        CodeGenerator.__init__(self)
        self.singletonTemplateArg = 2
        self.singletonTemplate = "+ (%s)The%s;\n\n"
        self.singletonImplemTemplate = "+ (%s)The%s {\n\tstatic %s *_theApiClient = nil;\n\tstatic dispatch_once_t onceToken;\n\tdispatch_once(&onceToken, ^{\n\t\t"
        self.codeGenericInclude = "#import <Foundation/Foundation.h>\n\n"
        self.paramSeparator = " : "
        self.implem_out = True
        self.extensien_file_out = ".h"
        self.extensien_implem_out = ".m"
        self.defaultType = "NSInteger"
        self.include_foreign = True
        self.classTemplate = "@interface %s : NSObject\n\n"
        self.classCloser = "@end"
        self.commentSyntax = "//"
        self.paramCloser = "]"
        self.formatFlag = "%@/"
        self.callParamSeparator = ","
        self.classVariableTemplate = "@property(nonatomic, strong) %s *%s;\n"
        self.includeTemplate = "@import \"%s" + self.extensien_file_out + "\"\n"
        self.implemTemplate = "@implementation %s"
        self.arrayTemplate = "NSMutableArray /* %s */"
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