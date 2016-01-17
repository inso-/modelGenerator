import json
import sys
#from src.utils.DjangoModel import *
sys.path.append('../.')
from utils.DjangoModel import *

class ParseJson:
    jsonFile = None
    inClass = False
    className = ""
    parsed = []
    tmpModel = DjangoModel()

    def __init__(self, fileName="data.json"):
        self.pyFile = open(fileName, 'r')
        self.genered = []
        self.parsed = []
        self.inClass = False
        self.ClassName = ""
        self.tmpModel = DjangoModel()
        self.varType = None
        self.varName = None

    def parse_rec(self, it, model):
        if type(it) is dict:
            if model is None:
                model = DjangoModel()
                model.setClassName("BaseClass")

            for key, value in it.items():
                if type(value) is list:
                    for i in value:
                        newModel = DjangoModel()
                        newModel.setClassName(key)
                        self.parse_rec(i, newModel)
                        if newModel.nameClass not in self.genered:
                            self.parsed.append(newModel)
                            self.genered.append(newModel.nameClass)
                if type(value) is dict:
                    newModel = DjangoModel()
                    newModel.setClassName(key)
                    self.parse_rec(value, newModel)
                else:
                    model.addFunc(key, str(type(value)))

        if model.nameClass not in self.genered:
            self.parsed.append(model)
            self.genered.append(model.nameClass)
            return

    def parse(self):
        self.parse_rec(json.load(self.pyFile), None)
        self.convert()

    def convert(self):
        converter = {
            "int": "IntegerField",
            "unicode": "TextField",
            "none": "TextField",
            "bool": "BooleanField",
            "list": "ListField",
            #"DecimalField": "int",
            #"PositiveSmallIntegerField": "int",
            #"BigIntegerField": "double",
            #"BooleanField": "bool",
            #"DateField": "DateTime",
            #"DateTimeField": "DateTime",
        }
        i = 0
        for a in self.parsed:
            for k, v in a.var.items():
                v = v.replace("<type '", "").replace("'>", "")
                a.var[k] = converter.get(v)
                if a.var[k] == None:
                    print "Type %s not found for %s" % (v, k)
                    a.var[k] = "TextField"
                self.parsed[i] = a
            i = i + 1

#def test():
#    a = ParseJson()
#    a.parse()
#    for b in a.parsed:
#            print b.nameClass#print a
#            print b.var

#test()