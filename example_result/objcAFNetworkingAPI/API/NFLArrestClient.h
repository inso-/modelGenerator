//
//	NFLArrestClient.h Generate By modelGenerator
//	Create the Sun Feb  7 05:19:31 2016
//	https://github.com/inso-/modelGenerator
//

@interface NFLArrestClient : AFHTTPSessionManager 

+ (NFLArrestClient)TheNFLArrestClient;

@property BOOL connected;
@property (strong, nonatomic) NSString *token;
@property (strong, nonatomic) NSString *user;

- (NSURLSessionDataTask *)get_crime_topTeams_CrimeID:(NSString *)CrimeID
(void (^)(NSArray *results, NSError* error))completion;

- (NSURLSessionDataTask *)get_crime_topPositions_CrimeID:(NSString *)CrimeID
(void (^)(NSArray *results, NSError* error))completion;

- (NSURLSessionDataTask *)get_crime_timeline_CrimeID:(NSString *)CrimeID
(void (^)(NSArray *results, NSError* error))completion;

- (NSURLSessionDataTask *)get_crime_arrests_CrimeID:(NSString *)CrimeID
(void (^)(NSArray *results, NSError* error))completion;

- (NSURLSessionDataTask *)get_team_topPlayers_TeamID:(NSString *)TeamID
(void (^)(NSArray *results, NSError* error))completion;

- (NSURLSessionDataTask *)get_team_topCrimes_TeamID:(NSString *)TeamID
(void (^)(NSArray *results, NSError* error))completion;

- (NSURLSessionDataTask *)get_team_timeline_TeamID:(NSString *)TeamID
(void (^)(NSArray *results, NSError* error))completion;

- (NSURLSessionDataTask *)get_team_arrests_TeamID:(NSString *)TeamID
(void (^)(NSArray *results, NSError* error))completion;

- (NSURLSessionDataTask *)get_player_topCrimes_PlayerName:(NSString *)PlayerName
(void (^)(NSArray *results, NSError* error))completion;

- (NSURLSessionDataTask *)get_player_arrests_PlayerName:(NSString *)PlayerName
(void (^)(NSArray *results, NSError* error))completion;

- (NSURLSessionDataTask *)get_position_topTeams_PositionID:(NSString *)PositionID
(void (^)(NSArray *results, NSError* error))completion;

- (NSURLSessionDataTask *)get_position_topCrimes_PositionID:(NSString *)PositionID
(void (^)(NSArray *results, NSError* error))completion;

- (NSURLSessionDataTask *)get_position_timeline_PositionID:(NSString *)PositionID
(void (^)(NSArray *results, NSError* error))completion;

- (NSURLSessionDataTask *)get_position_arrests_PositionID:(NSString *)PositionID
(void (^)(NSArray *results, NSError* error))completion;


@end