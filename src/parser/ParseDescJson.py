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
                response = urllib.urlopen(url)
                strJson = response.read()
                print "source: " + url
                data = json.loads(strJson)
                tmp = ParseJson()
                print "1"
                tmp.parse(data, modelName)
                print "2"
                self.parsedModel += tmp.parsedModel
            except Exception as e:
                print url
                print e

    def parse_route(self, api):
        for elem in api['ROUTE']:
            #try:
                url = elem["URL"]
                tmp = RouteModel()
                tmp.url = url
                if "{" in tmp.url:
                    tmp3 = url.split("{")
                    Rurl = tmp3[0]
                    i = 0
                    while len(tmp3) > i + 1:
                        tmp4 = url.split("{")[i  + 1].split("}")
                        paramName = tmp4[0]
                        print paramName
                        print Rurl
                        if (paramName in api["URL_PARAM"].keys()):
                            value = api["URL_PARAM"][paramName]
                        else:
                            value = "{" + paramName + "}"

                        if (len(tmp4) > 1):
                            strEnd = tmp4[1]
                            Rurl += str(value) + strEnd
                        else:
                            Rurl += str(value)
                        print Rurl
                        i = i + 1
                    tmp.url = Rurl
                    print tmp.url
                    a = tmp.url.split("{")[1].replace("}", "")
                    if "," in a:
                        tmp2 = a.split(",")
                        for p in tmp2:
                            tmp.param[p] = None
                    else:
                        tmp.param[a] = None
                tmp.method = elem["METHOD"]
                self.parsedAPI.route.append(tmp)
            #except Exception as e:
            #    print url
            #    print e

    def parse_baseurl(self, apiurl, apiParam):
        url = apiurl
        self.parsedAPI.basURLParam = url
        if '{' in apiurl:
            url = apiurl.split("{")[0]
            while len(tmp) >= i + 2:
                paramName = apiurl.split("{")[i  + 1].split("}")[0]
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
#        try:
        self.parse_route(api)
#        except Exception as e:
#            print(e)
        self.parse_model(api["EXAMPLE_PARAM"])
        #from pprint import pprint
        #pprint (vars(self.parsedAPI))
        #for route in self.parsedAPI.route:
        #    pprint (vars(route))
        return self.parsedAPI