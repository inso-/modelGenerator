#from src.utils.DjangoModel import *
import sys
sys.path.append('../.')
from utils.DjangoModel import *

# Add the ptdraft folder path to the sys.path list

#from src.utils import *

#from ...utils import *

class ParsePyModel:
    pyFile = None
    inClass = False
    inMeta = False
    className = ""
    parsed = []
    tmpModel = DjangoModel()

    def __init__(self, fileName="out.py"):
        self.pyFile = open(fileName, 'r')
        self.parsed = []
        self.inClass = False
        self.inMeta = False
        self.ClassName = ""
        self.tmpModel = DjangoModel()
        self.varType = None
        self.varName = None

    def parse(self):
        for line in self.pyFile.readlines():
            if line[0:5] == "class":
                if self.inClass:
                    self.parsed.append(self.tmpModel)
                    self.inMeta = False;
                    self.tmpModel = DjangoModel()
                else:
                    self.inClass = True
                    self.inMeta = False;
                self.className = line[6:].split("(")[0]
                self.tmpModel.setClassName(self.className)

            if "Meta" in line:
                self.inMeta = True;

            if self.inClass and not self.inMeta and "=" in line:
                self.varName = line.split("=")[0].replace(" ", "")
                if "ForeignKey" in line:
                    self.varType = line.split("=")[1].split(",")[0].replace(" ", "").replace("\n", "")
                else:
                    self.varType = line.split("=")[1].split("(")[0].replace(" ", "").replace("\n", "")
                self.tmpModel.addFunc(self.varName, self.varType)

        return self.parsed
