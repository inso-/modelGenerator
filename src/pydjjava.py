#!/usr/bin/env python
from PromptUtils import *

def getTypeJava(varType):
    if "ForeignKey" in varType :
        typeConverted = varType.split("(")[1].replace("'", "").replace(")", "")
        return typeConverted, "new " + typeConverted + "(data.optJSONObject",
    
    typeTable = { "models.CharField" : "String",
                  "models.TextField" : "int",
                  "models.IntegerField" : "int",
                  "models.DecimalField": "int",
                  "models.PositiveSmallIntegerField" : "int",
                  "models.BigIntegerField" : "long",
                  "models.BooleanField" : "boolean",
                  "models.DateField" : "String",
                  "models.DateTimeField" : "String",
    }

    typeConverted = typeTable.get(varType)

    jsontypeTable = { "models.CharField" : "data.optString",
                      "models.TextField" : "data.optString",
                      "models.IntegerField" : "data.optInt",
                      "models.DecimalField": "data.optInt",
                      "models.PositiveSmallIntegerField" : "data.optString",
                      "models.BigIntegerField" : "data.optLong",
                      "models.BooleanField" : "data.optBoolean",
                      "models.DateField" : "data.optString",
                      "models.DateTimeField" : "data.optString",
    }
    jsontypeConverted = jsontypeTable.get(varType)
    if typeConverted is None:
        print varType + " not found"
        return "tnt", "object.optInt"
    return typeConverted , "data." + jsontypeConverted

def header():
    code = "//\n"
    code += "//   Generate By modelGenerator\n"
    code += "//   https://github.com/inso-/modelGenerator\n"
    code += "//\n"
    return code

def generateJava(parsed, prompt=False, verbose=False):
    for model in parsed:
        if prompt and not query_yes_no("generate " + model.nameClass + " ?"):
            continue
        javaObject = open("output/" + model.nameClass + ".java", "w")
        
        code = ""
        codeCor = ""
        codeImport = ""
        codeGetterSetter = ""
        codeConstruct = ""
        codeSerialize = ""
        
        codeImport += "import org.json.JSONException;\n"
        codeImport += "import org.json.JSONObject;\n"

        codeCor += "public class " + model.nameClass + "{\n\n"
        
        codeConstruct += "\tPublic " + model.nameClass + "() {}\n\n"
        codeConstruct += "\tPublic " + model.nameClass + "(JSONObject data) {\n"

        codeSerialize += "\tPublic JSONObject toJSON() {\n\t\tJSONObject data = new JSONObject();\n\t\ttry {\n"
        
        for varName, varType in  model.var.iteritems():
            typeVar, jsontypeVar = getTypeJava(varType)

            if varName == "public" or varName == "private":
                varName = "_" + varName
            
            codeCor += "\tprivate " + typeVar + " " + varName + ";\n"
            codeGetterSetter += "\tpublic " + typeVar + " get" + varName.capitalize() + "() {\n\t\treturn " + varName + ";\n\t}\n\n"
            codeGetterSetter += "\tpublic void set" + varName.capitalize() + "(" + typeVar + " Param" + varName + ") {\n\t\t" + varName + " = Param" + varName + ";\n\t}\n\n"
            codeConstruct += "\t\t" + varName  + " = " + jsontypeVar + "(\"" + varName + "\")"
            if "(" in jsontypeVar :
                codeConstruct += ");\n"
                codeSerialize += "\t\t\tif (" + varName + " != null)\n"
                codeSerialize += "\t\t\t\tdata.put(\"" + varName + "\", " + varName + ".toJSON());\n "
            else:
                codeSerialize += "\t\t\tdata.put(\"" + varName + "\", " + varName + ");\n "
                codeConstruct += ";\n"
        
        codeCor += "\n"
        codeSerialize += "\t\t}\n\t\tcatch (JSONException je) {\n\n\t\t}\n\t\treturn data;\n\t}\n"
        codeConstruct += "\t}\n"
        codeGetterSetter += "\t}\n"
        
        code += header() + "\n"
        code += codeImport + "\n"
        code += codeCor + "\n"
        code += codeConstruct + "\n"
        code += codeSerialize + "\n"
        code += codeGetterSetter + "\n"
        
            
        javaObject.write(code)

        if verbose:
            print "Generate output/" + model.nameClass + ".java"
