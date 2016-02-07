#!/usr/bin/env python
from src.language.objc import objc


class objcAFNetworkingAPI(objc):

  def __init__(self):
        objc.__init__(self)
        self.API = True
        self.APIclassTemplate = "@interface %s : AFHTTPSessionManager \n\n"
        self.APIVariable = "@property BOOL connected;\n@property (strong, nonatomic) NSString *token;\n@property (strong, nonatomic) NSString *user;\n\n"
        self.APImethodDefineImplemTemplateClose = "\n(void (^)(NSArray *results, NSError* error))completion\n"
        self.APImethodImplemTemplateOpen = "{\n"
        self.APImethodImplemTemplate = "\tNSURLSessionDataTask *task = [self %s:%s\n\t\tparameters:nil\n\t\tsuccess:^(NSURLSessionDataTask *task, id responseObject) {\n\t\t\tNSHTTPURLResponse *httpResponse = (NSHTTPURLResponse *)task.response;\n\t\t\tif (httpResponse.statusCode == 200) {\n\t\t\t} else {\n\t\t\t    dispatch_async(dispatch_get_main_queue(), ^{\n\t\t\t\t   completion(nil, nil);\n\t\t\t    }\n\t\t\t}}\n\t\tfailure:^(NSURLSessionDataTask *task, NSError *error) {\n\t\t\tdispatch_async(dispatch_get_main_queue(), ^{\n\t\t\t    completion(nil, error);\n\t\t\t});\n\t}];"
        self.APImethodImplemTemplateClose = "\n\treturn task;\n}\n\n"
        self.APImethodTemplateClose = "\n(void (^)(NSArray *results, NSError* error))completion;\n\n"
        self.baseURLImplemTemplate = "\tNSURL *baseURL = [NSURL URLWithString:@\"%s\"];\n\t\t\tNSURLSessionConfiguration *config = [NSURLSessionConfiguration defaultSessionConfiguration];\n\t\tNSURLCache *cache = [[NSURLCache alloc] initWithMemoryCapacity:10 * 1024 * 1024\n\t\t\tdiskCapacity:50 * 1024 * 1024\n\t\t\tdiskPath:nil];\n\t\t\t[config setURLCache:cache];\n\t\t\t_theApiClient = [[ApiClient alloc] initWithBaseURL:baseURL\n\t\t\t\tsessionConfiguration:config];\n\t\t\t_theApiClient.responseSerializer = [AFJSONResponseSerializer serializer];\n\t\t});\n\treturn _theApiClient;\n}\n\n"
        self.APIsingleton = True
        self.APImethodTemplateOpen = "- (NSURLSessionDataTask *)%s:"
        self.APImethodDefineImplemTemplateOpen = self.APImethodTemplateOpen
        self.APImethodParamTemplate = "(NSString *)%s"
        self.APIOneParamURLTemplate = '[NSString stringwithformat:@\"%s%%@",%s]'
        self.APIManyParamURLTemplate = '[NSString stringwithformat:\"@%s\",%s]"'
        self.APIParamURLTemplate = '[NSString stringwithformat: @"%s",@"'