#!/usr/bin/env python
from pydjgenerator import CodeGenerator


class java(CodeGenerator):

    def __init__(self):
        super.__init__(self)
        self.implem_out = False
        self.extensien_file_out = ".java"
        self.defaultType = "int"
        self.include_foreign = True
        self.getter_setter = True
        self.construct = True
        self.serialize = True
        self.classTemplate = "public class %s{\n\n"
        self.classCloser = "}"
        self.commentSyntax = "//"
        self.classVariableTemplate = "\tprivate %s %s;\n"
        self.includeTemplate = "@import \"%s" + self.extensien_file_out + "\"\n"
        self.implemTemplate = "@implementation %s"
        self.codeGenericInclude = "import org.json.JSONException;\nimport org.json.JSONObject;\n"
        self.defaultConstructTemplate = "\tpublic %s() {}\n\n"
        self.jsonConstructTemplate = "\tpublic %s(JSONObject data) {\n"
        self.serializeTemplate =  "\tpublic JSONObject toJSON() {\n\t\tJSONObject data = new JSONObject();\n\t\ttry {\n"
        self.serializeCorTemplate = "\t\t\tdata.put(\"%s\", %s);\n "
        self.serializeClose = "\t\t}\n"
        self.foreignKeySerializeTemplate = "\t\t\t\tdata.put(\"%s\", %s.toJSON());\n "
        self.serializeConditionTemplate = "\t\t\tif (%s != null)\n"
        self.jsonConstructCorTemplate = "\t\t%s = %s(\"%s\")"
        self.jsonConstructCorClose = ";\n"
        self.jsonConstructCorCloseForeign = ");\n"
        self.jsonConstructClose = "\t\t}\n\t\tcatch (JSONException je) {\n\n\t\t}\n\t\treturn data;\n\t}\n"
        self.getterTemplate = "\tpublic %s get%s() {\n\t\treturn %s;\n\t}\n\n"
        self.setterTemplate = "\tpublic void set%s(%s Param%s) {\n\t\t%s = Param%s;\n\t}\n\n"
        self.typeTable = {
            "CharField": "String",
            "TextField": "String",
            "IntegerField": "int",
            "DecimalField": "int",
            "PositiveSmallIntegerField": "int",
            "BigIntegerField": "long",
            "BooleanField": "boolean",
            "DateField": "String",
            "DateTimeField": "String",
        }
        self.jsontypetable =  {
            "CharField": "optString",
            "TextField": "optString",
            "IntegerField": "optInt",
            "DecimalField": "optInt",
            "PositiveSmallIntegerField": "optInt",
            "BigIntegerField": "optLong",
            "BooleanField": "optBoolean",
            "DateField": "optString",
            "DateTimeField": "optString",
        }