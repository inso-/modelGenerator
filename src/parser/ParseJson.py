import json
import sys
import random
import string
#from src.utils.DjangoModel import *
sys.path.append('../.')
from utils.DjangoModel import *

class ParseJson:
    jsonFile = None
    inClass = False
    className = ""
    filename = ""
    parsedAPI = None
    parsedModel = []
    tmpModel = DjangoModel()

    def __init__(self, fileName="/example_source/data.json"):
        self.filename = fileName
        self.genered = []
        self.parsedModel = []
        self.inClass = False
        self.ClassName = ""
        self.tmpModel = DjangoModel()
        self.varType = None
        self.varName = None

    def parse_rec(self, it, model):

        if (type(it) is list):
            if len(it) < 1:
                return
            self.parse_rec(it[0], model)

        if type(it) is dict:
            if model is None:
                model = DjangoModel()
                model.setClassName("BaseClass" + ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(1)))

            for key, value in it.items():
                varName = key
                if type(value) is list:
                    newModel = DjangoModel()
                    newModel.setClassName(varName)
                    self.parse_rec(value[0], newModel)
                    if (key not in model.var):
                        model.addFunc(varName, "list(%s)" % varName.capitalize())
                        #if newModel.nameClass not in self.genered:
                         #   self.parsedModel.append(newModel)
                         #   self.genered.append(newModel.nameClass)
                elif type(value) is dict:
                    newModel = DjangoModel()
                    newModel.setClassName(varName)
                    self.parse_rec(value, newModel)
                    if (key not in model.var):
                        model.addFunc(varName, varName)
#                    print model.nameClass
#                    print key + ", " + key
                else:
#                    print model.nameClass
#                    print key + ", " + str(type(value))
                    if (key not in model.var):
                        model.addFunc(varName, str(type(value)))
            if model.nameClass not in (o.nameClass for o in self.parsedModel):
                self.parsedModel.append(model)

      #  if type(it) is list:
      #      if model is None:
      #          model = DjangoModel()
      #          model.setClassName("BaseClass")
      #      i = 0
      #      for i in it:
      #          i = i + 1
      #          if type(value) is dict or type(value) is list:
      #              newModel = DjangoModel()
      #              newModel.setClassName(model.nameClass + str(i))
      #              self.parse_rec(i, newModel)
      #          if model.nameClass not in self.genered:
      #              self.parsedModel.append(model)
      #              self.genered.append(model.nameClass)

      #  if model != None and model.nameClass not in self.genered:
      #      self.parsedModel.append(model)
      #      self.genered.append(model.nameClass)
      #      return

    def parse(self, data="", name="BaseClass"):
        model = DjangoModel()
        model.setClassName(name)
        if data == "":
            self.jsonFile = open(self.filename, 'r')
            self.parse_rec(json.load(self.jsonFile), model)
        else:
            self.parse_rec(data, model)
        try:
            from pprint import pprint
            for e in self.parsedModel:
                print(e)
            self.convert()
        except Exception as e:
            print "ICI =" + str(e)

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
#        import pprint
        res = {}
        for a in self.parsedModel:
#            pprint.pprint(a.var)
            for k, v in a.var.items():
                v = v.replace("<type '", "").replace("'>", "")
                if v in converter.values() or "foreignkey" in v:
                    continue
                if "list" in v:
                    continue
                a.var[k] = converter.get(v)
#                print v
#                print converter.get(v)
                if a.var[k] == None:
                    print "Type %s not found for %s" % (v, k)
                    a.var[k] = "ForeignKey('" + v + "')"
            i = i + 1

#def test():
#    a = ParseJson()
#    a.parse()
#    for b in a.parsedModel:
#            print b.nameClass#print a
#            print b.var

#test()