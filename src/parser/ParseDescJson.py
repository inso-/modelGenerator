import json, sys
from .ParseJson import *
sys.path.append('../.')
from utils.APIModel import *
import urllib, json
#from pprint import pprint


class ParseDescJson:
    descJsonFile = None
    parsedAPI = []
    parsedModel = []

    def __init__(self, fileName="/example_source/nflarrest.japi"):
        self.descJsonFile = fileName

    def parse_model(self, exampleParam):
        for elem in self.parsedAPI.route:
            if elem.method != "get":
                continue
            try:
                url = self.parsedAPI.baseURL + elem.url
                atmp = url.split("/")
                i = len(atmp) - 1
                if "{" in elem.url:
                    i = i - 1
                    a = url.split("{")[1].split("}")[0]
                    b = exampleParam[a]
                    url = url.split("{")[0] + b
                modelName = atmp[i]
                response = urllib.urlopen("http://" + url)
                strJson = response.read()
                data = json.loads(strJson)
                tmp = ParseJson()
                tmp.parse(data, modelName)
                self.parsedModel += tmp.parsedModel
            except Exception as e:
                print url
                print e

    def parse_route(self, api):
        for elem in api['ROUTE']:
            try:
                url = elem["URL"]
                tmp = RouteModel()
                tmp.url = url
                if "{" in tmp.url:
                    a = tmp.url.split("{")[1].replace("}", "")
                    if "," in a:
                        tmp2 = a.split(",")
                        for p in tmp2:
                            tmp.param[p] = None
                    else:
                        tmp.param[a] = None
                tmp.method = elem["METHOD"]
                self.parsedAPI.route.append(tmp)
            except Exception as e:
                print url
                print e

    def parse_baseurl(self, apiurl, apiParam):
        url = apiurl
        self.parsedAPI.basURLParam = url
        if '{' in apiurl:
            tmp = apiurl.split("{")
            i = 0
            url = apiurl.split("{")[0]
            while len(tmp) >= i + 2:
                paramName = apiurl.split("{")[i  + 1].replace("}", "")
                value = apiParam[paramName]
                strEnd = apiurl.split("{")[i  + 1].split("}")[1]
                url += str(value) + strEnd
                self.parsedAPI.param[paramName] = value
                i = i + 1
        self.parsedAPI.baseURL = url



    def parse(self):
        data_file = open(self.descJsonFile, 'r')
        api = json.load(data_file)
        self.parsedAPI = APIModel()
        self.parsedAPI.title = api["title"]
        self.parse_baseurl(api["baseURL"], api["URL_PARAM"])
        self.parse_route(api)
        self.parse_model(api["EXAMPLE_PARAM"])
        #from pprint import pprint
        #pprint (vars(self.parsedAPI))
        #for route in self.parsedAPI.route:
        #    pprint (vars(route))
        #self.parse_route(api)
        return self.parsedAPI