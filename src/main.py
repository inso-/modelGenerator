#!/usr/bin/env python
import sys, inspect, urllib, json
from settings import *
from parser.ParsePyModel import ParsePyModel
from parser.ParseJson import ParseJson
from parser.ParseRaml import ParseRaml
from parser.ParseDescJson import ParseDescJson
from language import *
from language.language import language as planguage


def main():
    verbose = False
    if (len(sys.argv) > 1):
        if len(sys.argv) > 2 and "-v" in sys.argv[1]:
            verbose = True
            fileName = sys.argv[2]
        elif len(sys.argv) > 2 and "-v" in sys.argv[2]:
            verbose = True
            fileName = sys.argv[1]
        else:
            fileName = sys.argv[1]
    else:
        print("Usage:\n\t\t./" + __file__ + " [PyModel or json InputFile] \n\t\t -v Verbose Mode")
        return

    if ".py" in fileName:
        n = ParsePyModel(fileName)
        n.parse()
        run_generate_model(n, verbose)

    elif ".json" in fileName:
        n = ParseJson(fileName)
        n.parse()
        run_generate_model(n, verbose)

    elif ".japi" in fileName:
        n = ParseDescJson(fileName)
        n.parse()
        for elem in n.parsed['GET']:
            try:
                url = "http://www." + elem["URL"]
                atmp = url.split("/")
                i = len(atmp) - 1
                if "{" in elem["URL"]:
                    i = i - 1
                    a = url.split("{")[1].split("}")[0]
                    b = n.parsed['EXAMPLE_PARAM'][a]
                    url = url.split("{")[0] + b

                modelName = atmp[i]
                response = urllib.urlopen(url)
                strJson = response.read()
                data = json.loads(strJson)
                tmp = ParseJson()
                tmp.parse(data, modelName)
                run_generate_model(tmp, verbose)
            except Exception as e:
                print url
                print e
    elif ".raml" in fileName:
        n = ParseRaml(fileName)
        n.parse()
        run_generate_api(n, verbose)
        return

    else:
        print("Usage:\n\t\t./" + __file__ + " [PyModel or json InputFile] \n\t\t -v Verbose Mode")
        return


def run_generate_api(data, verbose):
    print data.parsed.title
    print data.parsed.documentation
    print data.parsed.baseUri
    print data.parsed.resources
    print type(data.parsed.resources)
    for a in data.parsed.resources.__iter__():
        # print a
        # print n.parsed.resources[a]
        print data.parsed.resources[a].methods
    prompt = False
    objc.objc().generateAPI(data.parsed, prompt, verbose)


def run_generate_model(data, verbose):
    for lang in planguage:
        # print globals()
        #print lang
        klass = inspect.getmembers(globals()[lang], inspect.isclass)[1][1]
        # print klass[1][1]
        toGenerate = globals()[lang.upper()]
        prompt = globals()[lang.upper() + "_PROMPT"]
        if (toGenerate == 1 or prompt == 1):
            # print type(klass[1][1])
            klass().generate(data.parsed, prompt, verbose)


main()
