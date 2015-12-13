#!/usr/bin/env python
from PromptUtils import *

def getTypeJava(varType):
    if "ForeignKey" in varType :
        typeConverted = varType.split("(")[1].replace("'", "").replace(")", "")
#        codeImport = "@import \"" + typeConverted + ".h\"" + "\n"
        return typeConverted, "new " + typeConverted + "(object.optJSONObject",
    
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

    jsontypeTable = { "models.CharField" : "object.optString",
                      "models.TextField" : "object.optString",
                      "models.IntegerField" : "object.optInt",
                      "models.DecimalField": "object.optInt",
                      "models.PositiveSmallIntegerField" : "object.optString",
                      "models.BigIntegerField" : "object.optLong",
                      "models.BooleanField" : "object.optBoolean",
                      "models.DateField" : "object.optString",
                      "models.DateTimeField" : "object.optString",
    }
    jsontypeConverted = jsontypeTable.get(varType)
    if typeConverted is None:
        print varType + " not found"
        return "tnt", "object.optInt"
    return typeConverted , "data." + jsonTypeConverted

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
        CodeConstruct = ""

        codeImport += "import org.json.JSONException;\n"
        codeimport += "import org.json.JSONObject;\n"
        
        codeConstruct += "Public " + model.nameClass + "(){}\n\n"

        codeConstruct += "Public " + model.nameClass + "(JSONObject data){\n"
        codeCor += "public class " + model.nameClass + "{\n\n"

        for varName, varType in  model.var.iteritems():
            typeVar, jsontypeVar = getTypeJava(varType)
                
#            if newImport != None:
#                codeImport += newImport
            codeCor += "\tprivate " + typeVar + " " + varName + ";\n"
            codeGetterSetter += "\tpublic " + typeVar + " get" + varName.capitalize() + "() {\n\t\treturn " + varName + ";\n\t}\n\n"
            codeGetterSetter += "\tpublic void set" + varName.capitalize() + "(" + typeVar + " Param" + varName + ") {\n\t\t" + varName + " = Param" + varName + ";\n\t}\n\n"
            codeConstruct += varName  + " = " jsontypeVar + "(\"" + varName + "\")"
            if "(" in jsonTypeVar :
                codeConstruct += ")"
            codeConstruct += ";\n"
        codeCor += "\n"

        
        
        codeConstruct +="}\n"
        

        
        code += header() + "\n"
        code += codeImport + "\n"
        code += codeCor + "\n"
        code += codeConstruct + "\n"
        code += codeGetterSetter + "}\n"

            
        javaObject.write(code)

        if verbose:
            print "Generate output/" + model.nameClass + ".java"
