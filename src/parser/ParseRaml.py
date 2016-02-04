import pyraml.parser

class ParseRaml:
    ramlFile = None
    parsed = []

    def __init__(self, fileName="schema.raml"):
        self.ramlFile = fileName

    def parse(self):
        api = pyraml.parser.load(self.ramlFile)
        self.parsed = api
        return self.parsed
