import pyraml.parser
import sys
sys.path.append('../.')
from utils.APIModel import *
#from pprint import pprint

class ParseRaml:
    ramlFile = None
    parsedAPI = None
    parsedModel = None

    def __init__(self, fileName="/example_source/schema.raml"):
        self.ramlFile = fileName

    def parse_baseurl(self, api):
        url = api.baseUri
        self.parsedAPI.basURLParam = url
        if '{' in api.baseUri:
            tmp = api.baseUri.split("{")
            i = 0
            url = api.baseUri.split("{")[0]
            while len(tmp) >= i + 2:
                paramName = api.baseUri.split("{")[i  + 1].replace("}", "")
                value = getattr(api, paramName)
                strEnd = api.baseUri.split("{")[i  + 1].split("}")[1]
                url += str(value) + strEnd
                self.parsedAPI.param[paramName] = value
                i = i + 1
        self.parsedAPI.baseURL = url


    def parse_route(self, api):
        for route in api.resources.__iter__():
            #print route
            #print api.resources[route]
            codeRouteparam = ""
            codeRoute = ""
            if "{" in route:
                a = route.split("{")[1].replace("}", "")
                b = route.split("{")[0]
                if "," in a:
                    tmp = a.split(",")
                    for p in tmp:
                        param[p] = None
                else:
                    param = {}
                    param[a] = None

            for method in api.resources[route].methods:
               #print method
               #print api.resources[route].methods[method]
               tmp = RouteModel()
               tmp.setURL(route)
               tmp.setMethod(method)
               tmp.param = param
               self.parsedAPI.route.append(tmp)

    def parse(self):
        api = pyraml.parser.load(self.ramlFile)
        self.parsedAPI = APIModel()
        self.parsedAPI.title = api.title
        self.parse_baseurl(api)
        self.parse_route(api)
        #from pprint import pprint
        #pprint (vars(self.parsedAPI))
        #for route in self.parsedAPI.route:
        #    pprint (vars(route))
        #return self.parsedAPI


        #exit()
    #   print self.parsedAPI
#        exit()
        #self.parsedAPI = api

