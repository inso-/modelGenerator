#!/usr/bin/env python
from src.pydjgenerator import CodeGenerator


class objc(CodeGenerator):

    def __init__(self):
        CodeGenerator.__init__(self)
        self.APIclassTemplate = "@interface %s : AFHTTPSessionManager \n\n"
        self.singletonTemplate = "+ (%s)The%s;\n\n"
        self.singletonImplemTemplate = "+ (%s)The%s {\n\tstatic %s *_theApiClient = nil;\n\tstatic dispatch_once_t onceToken;\n\tdispatch_once(&onceToken, ^{\n\t\t"
        self.APIVariable = "@property BOOL connected;\n@property (strong, nonatomic) NSString *token;\n@property (strong, nonatomic) NSString *user;\n\n"
        self.baseURLImplemTemplate = "\tNSURL *baseURL = [NSURL URLWithString:%s];\n\t\t\tNSURLSessionConfiguration *config = [NSURLSessionConfiguration defaultSessionConfiguration];NSURLCache *cache = [[NSURLCache alloc] initWithMemoryCapacity:10 * 1024 * 1024\n\t\t\tdiskCapacity:50 * 1024 * 1024\n\t\t\tdiskPath:nil];\n\t\t\t[config setURLCache:cache];\n\t\t\t_theApiClient = [[ApiClient alloc] initWithBaseURL:baseURL\n\t\t\t\tsessionConfiguration:config];\n\t\t\t_theApiClient.responseSerializer = [AFJSONResponseSerializer serializer];\n\t\t});\n\treturn _theApiClient;\n}\n\n"
        self.APIsingleton = True
        self.APImethodTemplateOpen = "- (NSURLSessionDataTask *)%s:"
        self.APImethodDefineImplemTemplateOpen = self.APImethodTemplateOpen
        self.APImethodParamTemplate = "(NSString *)%s"
        self.paramSeparator = " : "
        self.APImethodDefineImplemTemplateClose = "\n(void (^)(NSArray *results, NSError* error))completion\n"
        self.APImethodImplemTemplateOpen = "{\n"
        self.APImethodImplemTemplate = "\tNSURLSessionDataTask *task = [self %s:%s\n\t\tparameters:nil\n\t\tsuccess:^(NSURLSessionDataTask *task, id responseObject) {\n\t\t\tNSHTTPURLResponse *httpResponse = (NSHTTPURLResponse *)task.response;\n\t\t\tif (httpResponse.statusCode == 200) {\n\t\t\t} else {\n\t\t\t    dispatch_async(dispatch_get_main_queue(), ^{\n\t\t\t\t   completion(nil, nil);\n\t\t\t    }\n\t\t\t}}\n\t\tfailure:^(NSURLSessionDataTask *task, NSError *error) {\n\t\t\tdispatch_async(dispatch_get_main_queue(), ^{\n\t\t\t    completion(nil, error);\n\t\t\t});\n\t}];"
        self.APImethodImplemTemplateClose = "\n\treturn task;\n}\n\n"
        self.APImethodTemplateClose = "\n(void (^)(NSArray *results, NSError* error))completion;\n\n"
        self.implem_out = True
        self.extensien_file_out = ".h"
        self.extensien_implem_out = ".m"
        self.defaultType = "NSInteger"
        self.include_foreign = True
        self.classTemplate = "@interface %s : NSObject\n\n"
        self.classCloser = "@end"
        self.commentSyntax = "//"
        self.classVariableTemplate = "@property(nonatomic, strong) %s *%s;\n"
        self.includeTemplate = "@import \"%s" + self.extensien_file_out + "\"\n"
        self.implemTemplate = "@implementation %s"
        self.typeTable = {
            "CharField": "NSString",
            "TextField": "NSString",
            "IntegerField": "NSInteger",
            "DecimalField": "NSInteger",
            "PositiveSmallIntegerField": "NSInteger",
            "BigIntegerField": "NSInteger",
            "BooleanField": "NSInteger",
            "DateField": "NSDate",
            "DateTimeField": "NSDate",
            "ListField": "NSMutableArray",
        }
        ##        self.typeTable = {
##            "AutoField": "" ,
##            "BigIntegerField": "" ,
##            "BinaryField": "" ,
##            "BooleanField": "" ,
##            "CharField": "" ,
##            "CommaSeparatedIntegerField": "" ,
##            "DateField": "" ,
##            "DateTimeField": "" ,
##            "DecimalField": "" ,
##            "DurationField": "" ,
##            "EmailField": "" ,
##            "FileField": "" ,
##            "FileField and FieldFile": "" ,
##            "FilePathField": "" ,
##            "FloatField": "" ,
##            "ImageField": "" ,
##            "IntegerField": "" ,
##            "GenericIPAddressField": "" ,
##            "NullBooleanField": "" ,
##            "PositiveIntegerField": "" ,
##            "PositiveSmallIntegerField": "" ,
##            "SlugField": "" ,
##            "SmallIntegerField": "" ,
##            "TextField": "" ,
##            "TimeField": "" ,
##            "URLField": "" ,
##            "UUIDField": "" ,
##            }