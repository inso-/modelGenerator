#!/usr/bin/env python
from src.pydjgenerator import *
from .swift import swift

class swiftAFNetworkingAPIBolts(swift):

    def __init__(self):
        self.API = True
        self.APIsingleton = True
        self.baseURLImplemTemplate = "\toverride init() {\n\t\tlet configuration = NSURLSessionConfiguration.ephemeralSessionConfiguration()\n\t\tconfiguration.HTTPAdditionalHeaders = [\n\t\t\t\"Content-Type\" : \"application/json\"\n\t\t]\n\t\tself.functionSessionManager = AFHTTPSessionManager(baseURL:NSURL(string:\"%s\"), sessionConfiguration:configuration)\n\t\tself.functionSessionManager.requestSerializer = AFJSONRequestSerializer()\n\t\tself.functionSessionManager.responseSerializer = AFJSONResponseSerializer()\n\t}"
            #"\tNSURL *baseURL = [NSURL URLWithString:@\"%s\"];\n\t\t\tNSURLSessionConfiguration *config = [NSURLSessionConfiguration defaultSessionConfiguration];\n\t\tNSURLCache *cache = [[NSURLCache alloc] initWithMemoryCapacity:10 * 1024 * 1024\n\t\t\tdiskCapacity:50 * 1024 * 1024\n\t\t\tdiskPath:nil];\n\t\t\t[config setURLCache:cache];\n\t\t\t_theApiClient = [[ApiClient alloc] initWithBaseURL:baseURL\n\t\t\t\tsessionConfiguration:config];\n\t\t\t_theApiClient.responseSerializer = [AFJSONResponseSerializer serializer];\n\t\t});\n\treturn _theApiClient;\n}\n\n"
        self.APIclassTemplate = "class %s : NSObject {\n"
        self.APIVariable = "\n\n"
        self.APImethodTemplateOpen = "\tfunc %s("
        self.APImethodParamTemplate = "%s : String) -> BFTask\n\t{\n"
        self.APImethodTemplateClose = ""
        self.APIImplemin_out = True
        self.APImethodImplemTemplate = "\t\tlet deferred = BFTaskCompletionSource()\n\t\tself.functionSessionManager.%s(\"%s, parameters:[:],\n\t\t\tsuccess:{task, responseObject in\n\t\t\t\tdeferred.setResult(responseObject)\n\t\t},\n\t\t\tfailure:{task, error in\n\t\t\t\tdeferred.setError(error)\n\t\t})"
        self.APImethodImplemTemplateClose = "\n\t\treturn deferred.task\n\t}\n\n"