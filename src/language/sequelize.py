#!/usr/bin/env python
from src.pydjgenerator import CodeGenerator

class Sequelize(CodeGenerator):

    def __init__(self):
        CodeGenerator.__init__(self)
        self.extensien_file_out = ".js"
        self.defaultType = "int"
        self.include_foreign = False
        self.classTemplate = "module.exports = function(sequelize, DataTypes) {\nreturn sequelize.define('%s', {\n"
        self.classCloser = "};"
        self.commentSyntax = "//"
        self.classVariableTemplate = "\t%s: {\n\t\ttype: %s\n\t};\t\n"
        self.includeTemplate = ""
        self.inverseNameType = True
        self.typeTable = {
            "EmailField": "DataTypes.CHAR",
            "FileField": "DataTypes.CHAR",
            "FilePathField": "DataTypes.CHAR",
            "CharField": "DataTypes.CHAR" ,
            "FieldFile": "DataTypes.CHAR" ,
            "URLField": "DataTypes.CHAR" ,
            "GenericIPAddressField": "DataTypes.CHAR" ,
            "SlugField": "DataTypes.CHAR" ,
            "ImageField": "DataTypes.CHAR" ,
            "IntegerField": "DataTypes.INTEGER" ,
            "AutoField": "DataTypes.INTEGER, autoIncrement: true" ,
            "PositiveIntegerField": "DataTypes.INTEGER.UNSIGNED" ,
            "PositiveSmallIntegerField": "DataTypes.INTEGER.UNSIGNED" ,
            "SmallIntegerField": "DataTypes.INTEGER" ,
            "DurationField": "DataTypes.BIGINT" ,
            "BigIntegerField": "DataTypes.BIGINT" ,
            "BinaryField": "DataTypes.BLOB" ,
            "BooleanField": "DataTypes.BOOLEAN" ,
            "NullBooleanField": "DataTypes.BOOLEAN, allowNull: true" ,
            "DateField": "DataTypes.DATEONLY" ,
            "DateTimeField": "DataTypes.DATE" ,
            "DecimalField": "DataTypes.DECIMAL" ,
            "FloatField": "DataTypes.FLOAT" ,
            "TextField": "DataTypes.TEXT" ,
            "TimeField": "DataTypes.TIME" ,
            "UUIDField": "DataTypes.UUID" ,
            "CommaSeparatedIntegerField": "DataTypes." ,
            }