import json
from pprint import pprint

class ParseDescJson:
    descJsonFile = None
    parsed = []

    def __init__(self, fileName="nflarrest.japi"):
        self.descJsonFile = fileName

    def parse(self):
        data_file = open(self.descJsonFile, 'r')
        data = json.load(data_file)
        self.parsed = data
        return data