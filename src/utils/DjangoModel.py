class DjangoModel:
    nameClass = "lol"
    var = {}

    def __init__(self):
        self.nameClass = ""
        self.var = {}

    def setClassName(self, className):
        self.nameClass = className
        
    def addFunc(self, Name, Type):
        self.var[Name] = Type
