#!/usr/bin/env python
from src.pydjgenerator import *
from .swiftAFNetworkingAPIBolts import swiftAFNetworkingAPIBolts

class swiftAFNetworkingAPIBoltsObjectMapping(swiftAFNetworkingAPIBolts):

    def __init__(self):
        swiftAFNetworkingAPIBolts.__init__(self)
        self.classTemplate = "class %s: Mappable {\n\n"
        self.jsonConstructTemplate = "\tfunc mapping(map: Map)  // %s mapper\n\t{\n"
        self.jsonConstructCor = True
        self.jsonConstructCorTemplate = "\t\t%s\t\t<-\tmap[%s\"%s\"]\n"
        self.jsonConstructCorClose = ""
        self.jsonConstructCorCloseForeign = ""
        self.arrayConstructCorTemplate = "\trequired init?(_ map: Map)\n\t{\n\t}\n\n\tclass func ObjectArrayFromArray(src : Array<NSDictionary>) -> Array<%s>\n\t{\n\t\tvar res : Array<%s> = Array<%s>()\n\t\tfor elem : NSDictionary in src\n\t\t{\n\t\t\tres.append(Mapper<%s>().map(elem)!)\n\t\t}\n\t\treturn res\n\t}"
