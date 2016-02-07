class APIModel:
    title = "lol"
    route = []
    baseURLParam = ""
    param = {}
    baseURL = ""

    def __init__(self):
        self.title = ""
        self.param = {}
        self.route = []
        self.baseURL = []

    def setTitle(self, title):
        self.title = title

    def addRoute(self, route):
        self.route.append(route)

class RouteModel:
    url = ""
    method = ""
    urlparam = ""
    param = {}

    def __init__(self):
        self.url = ""

    def setURL(self, url):
        self.url = url

    def setMethod(self, method):
        self.method = method

    def setUrlparam(self, urlparam):
        self.urlparam = urlparam

    def setParam(self, param):
        self.param = param