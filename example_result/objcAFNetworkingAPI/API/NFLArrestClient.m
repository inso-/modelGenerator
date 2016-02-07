//
//	NFLArrestClient.m Generate By modelGenerator
//	Create the Sun Feb  7 05:19:31 2016
//	https://github.com/inso-/modelGenerator
//

@import "NFLArrestClient.h"

+ (NFLArrestClient)TheNFLArrestClient {
	static NFLArrestClient *_theApiClient = nil;
	static dispatch_once_t onceToken;
	dispatch_once(&onceToken, ^{
			NSURL *baseURL = [NSURL URLWithString:@"www.NflArrest.com/api/v1"];
			NSURLSessionConfiguration *config = [NSURLSessionConfiguration defaultSessionConfiguration];
		NSURLCache *cache = [[NSURLCache alloc] initWithMemoryCapacity:10 * 1024 * 1024
			diskCapacity:50 * 1024 * 1024
			diskPath:nil];
			[config setURLCache:cache];
			_theApiClient = [[ApiClient alloc] initWithBaseURL:baseURL
				sessionConfiguration:config];
			_theApiClient.responseSerializer = [AFJSONResponseSerializer serializer];
		});
	return _theApiClient;
}

- (NSURLSessionDataTask *)get_crime:
(void (^)(NSArray *results, NSError* error))completion
{
	NSURLSessionDataTask *task = [self GET:
		parameters:nil
		success:^(NSURLSessionDataTask *task, id responseObject) {
			NSHTTPURLResponse *httpResponse = (NSHTTPURLResponse *)task.response;
			if (httpResponse.statusCode == 200) {
			} else {
			    dispatch_async(dispatch_get_main_queue(), ^{
				   completion(nil, nil);
			    }
			}}
		failure:^(NSURLSessionDataTask *task, NSError *error) {
			dispatch_async(dispatch_get_main_queue(), ^{
			    completion(nil, error);
			});
	}];
	return task;
}

- (NSURLSessionDataTask *)get_crime_topTeams_CrimeID:(NSString *)CrimeID
(void (^)(NSArray *results, NSError* error))completion
{
	NSURLSessionDataTask *task = [self GET:[NSString stringwithformat:@"/crime/topTeams/%@",CrimeID]
		parameters:nil
		success:^(NSURLSessionDataTask *task, id responseObject) {
			NSHTTPURLResponse *httpResponse = (NSHTTPURLResponse *)task.response;
			if (httpResponse.statusCode == 200) {
			} else {
			    dispatch_async(dispatch_get_main_queue(), ^{
				   completion(nil, nil);
			    }
			}}
		failure:^(NSURLSessionDataTask *task, NSError *error) {
			dispatch_async(dispatch_get_main_queue(), ^{
			    completion(nil, error);
			});
	}];
	return task;
}

- (NSURLSessionDataTask *)get_crime_topPositions_CrimeID:(NSString *)CrimeID
(void (^)(NSArray *results, NSError* error))completion
{
	NSURLSessionDataTask *task = [self GET:[NSString stringwithformat:@"/crime/topPositions/%@",CrimeID]
		parameters:nil
		success:^(NSURLSessionDataTask *task, id responseObject) {
			NSHTTPURLResponse *httpResponse = (NSHTTPURLResponse *)task.response;
			if (httpResponse.statusCode == 200) {
			} else {
			    dispatch_async(dispatch_get_main_queue(), ^{
				   completion(nil, nil);
			    }
			}}
		failure:^(NSURLSessionDataTask *task, NSError *error) {
			dispatch_async(dispatch_get_main_queue(), ^{
			    completion(nil, error);
			});
	}];
	return task;
}

- (NSURLSessionDataTask *)get_crime_timeline_CrimeID:(NSString *)CrimeID
(void (^)(NSArray *results, NSError* error))completion
{
	NSURLSessionDataTask *task = [self GET:[NSString stringwithformat:@"/crime/timeline/%@",CrimeID]
		parameters:nil
		success:^(NSURLSessionDataTask *task, id responseObject) {
			NSHTTPURLResponse *httpResponse = (NSHTTPURLResponse *)task.response;
			if (httpResponse.statusCode == 200) {
			} else {
			    dispatch_async(dispatch_get_main_queue(), ^{
				   completion(nil, nil);
			    }
			}}
		failure:^(NSURLSessionDataTask *task, NSError *error) {
			dispatch_async(dispatch_get_main_queue(), ^{
			    completion(nil, error);
			});
	}];
	return task;
}

- (NSURLSessionDataTask *)get_crime_arrests_CrimeID:(NSString *)CrimeID
(void (^)(NSArray *results, NSError* error))completion
{
	NSURLSessionDataTask *task = [self GET:[NSString stringwithformat:@"/crime/arrests/%@",CrimeID]
		parameters:nil
		success:^(NSURLSessionDataTask *task, id responseObject) {
			NSHTTPURLResponse *httpResponse = (NSHTTPURLResponse *)task.response;
			if (httpResponse.statusCode == 200) {
			} else {
			    dispatch_async(dispatch_get_main_queue(), ^{
				   completion(nil, nil);
			    }
			}}
		failure:^(NSURLSessionDataTask *task, NSError *error) {
			dispatch_async(dispatch_get_main_queue(), ^{
			    completion(nil, error);
			});
	}];
	return task;
}

- (NSURLSessionDataTask *)get_team:
(void (^)(NSArray *results, NSError* error))completion
{
	NSURLSessionDataTask *task = [self GET:
		parameters:nil
		success:^(NSURLSessionDataTask *task, id responseObject) {
			NSHTTPURLResponse *httpResponse = (NSHTTPURLResponse *)task.response;
			if (httpResponse.statusCode == 200) {
			} else {
			    dispatch_async(dispatch_get_main_queue(), ^{
				   completion(nil, nil);
			    }
			}}
		failure:^(NSURLSessionDataTask *task, NSError *error) {
			dispatch_async(dispatch_get_main_queue(), ^{
			    completion(nil, error);
			});
	}];
	return task;
}

- (NSURLSessionDataTask *)get_team_topPlayers_TeamID:(NSString *)TeamID
(void (^)(NSArray *results, NSError* error))completion
{
	NSURLSessionDataTask *task = [self GET:[NSString stringwithformat:@"/team/topPlayers/%@",TeamID]
		parameters:nil
		success:^(NSURLSessionDataTask *task, id responseObject) {
			NSHTTPURLResponse *httpResponse = (NSHTTPURLResponse *)task.response;
			if (httpResponse.statusCode == 200) {
			} else {
			    dispatch_async(dispatch_get_main_queue(), ^{
				   completion(nil, nil);
			    }
			}}
		failure:^(NSURLSessionDataTask *task, NSError *error) {
			dispatch_async(dispatch_get_main_queue(), ^{
			    completion(nil, error);
			});
	}];
	return task;
}

- (NSURLSessionDataTask *)get_team_topCrimes_TeamID:(NSString *)TeamID
(void (^)(NSArray *results, NSError* error))completion
{
	NSURLSessionDataTask *task = [self GET:[NSString stringwithformat:@"/team/topCrimes/%@",TeamID]
		parameters:nil
		success:^(NSURLSessionDataTask *task, id responseObject) {
			NSHTTPURLResponse *httpResponse = (NSHTTPURLResponse *)task.response;
			if (httpResponse.statusCode == 200) {
			} else {
			    dispatch_async(dispatch_get_main_queue(), ^{
				   completion(nil, nil);
			    }
			}}
		failure:^(NSURLSessionDataTask *task, NSError *error) {
			dispatch_async(dispatch_get_main_queue(), ^{
			    completion(nil, error);
			});
	}];
	return task;
}

- (NSURLSessionDataTask *)get_team_search_:
(void (^)(NSArray *results, NSError* error))completion
{
	NSURLSessionDataTask *task = [self GET:
		parameters:nil
		success:^(NSURLSessionDataTask *task, id responseObject) {
			NSHTTPURLResponse *httpResponse = (NSHTTPURLResponse *)task.response;
			if (httpResponse.statusCode == 200) {
			} else {
			    dispatch_async(dispatch_get_main_queue(), ^{
				   completion(nil, nil);
			    }
			}}
		failure:^(NSURLSessionDataTask *task, NSError *error) {
			dispatch_async(dispatch_get_main_queue(), ^{
			    completion(nil, error);
			});
	}];
	return task;
}

- (NSURLSessionDataTask *)get_team_timeline_TeamID:(NSString *)TeamID
(void (^)(NSArray *results, NSError* error))completion
{
	NSURLSessionDataTask *task = [self GET:[NSString stringwithformat:@"/team/timeline/%@",TeamID]
		parameters:nil
		success:^(NSURLSessionDataTask *task, id responseObject) {
			NSHTTPURLResponse *httpResponse = (NSHTTPURLResponse *)task.response;
			if (httpResponse.statusCode == 200) {
			} else {
			    dispatch_async(dispatch_get_main_queue(), ^{
				   completion(nil, nil);
			    }
			}}
		failure:^(NSURLSessionDataTask *task, NSError *error) {
			dispatch_async(dispatch_get_main_queue(), ^{
			    completion(nil, error);
			});
	}];
	return task;
}

- (NSURLSessionDataTask *)get_team_arrests_TeamID:(NSString *)TeamID
(void (^)(NSArray *results, NSError* error))completion
{
	NSURLSessionDataTask *task = [self GET:[NSString stringwithformat:@"/team/arrests/%@",TeamID]
		parameters:nil
		success:^(NSURLSessionDataTask *task, id responseObject) {
			NSHTTPURLResponse *httpResponse = (NSHTTPURLResponse *)task.response;
			if (httpResponse.statusCode == 200) {
			} else {
			    dispatch_async(dispatch_get_main_queue(), ^{
				   completion(nil, nil);
			    }
			}}
		failure:^(NSURLSessionDataTask *task, NSError *error) {
			dispatch_async(dispatch_get_main_queue(), ^{
			    completion(nil, error);
			});
	}];
	return task;
}

- (NSURLSessionDataTask *)get_player:
(void (^)(NSArray *results, NSError* error))completion
{
	NSURLSessionDataTask *task = [self GET:
		parameters:nil
		success:^(NSURLSessionDataTask *task, id responseObject) {
			NSHTTPURLResponse *httpResponse = (NSHTTPURLResponse *)task.response;
			if (httpResponse.statusCode == 200) {
			} else {
			    dispatch_async(dispatch_get_main_queue(), ^{
				   completion(nil, nil);
			    }
			}}
		failure:^(NSURLSessionDataTask *task, NSError *error) {
			dispatch_async(dispatch_get_main_queue(), ^{
			    completion(nil, error);
			});
	}];
	return task;
}

- (NSURLSessionDataTask *)get_player_topCrimes_PlayerName:(NSString *)PlayerName
(void (^)(NSArray *results, NSError* error))completion
{
	NSURLSessionDataTask *task = [self GET:[NSString stringwithformat:@"/player/topCrimes/%@",PlayerName]
		parameters:nil
		success:^(NSURLSessionDataTask *task, id responseObject) {
			NSHTTPURLResponse *httpResponse = (NSHTTPURLResponse *)task.response;
			if (httpResponse.statusCode == 200) {
			} else {
			    dispatch_async(dispatch_get_main_queue(), ^{
				   completion(nil, nil);
			    }
			}}
		failure:^(NSURLSessionDataTask *task, NSError *error) {
			dispatch_async(dispatch_get_main_queue(), ^{
			    completion(nil, error);
			});
	}];
	return task;
}

- (NSURLSessionDataTask *)get_player_search_:
(void (^)(NSArray *results, NSError* error))completion
{
	NSURLSessionDataTask *task = [self GET:
		parameters:nil
		success:^(NSURLSessionDataTask *task, id responseObject) {
			NSHTTPURLResponse *httpResponse = (NSHTTPURLResponse *)task.response;
			if (httpResponse.statusCode == 200) {
			} else {
			    dispatch_async(dispatch_get_main_queue(), ^{
				   completion(nil, nil);
			    }
			}}
		failure:^(NSURLSessionDataTask *task, NSError *error) {
			dispatch_async(dispatch_get_main_queue(), ^{
			    completion(nil, error);
			});
	}];
	return task;
}

- (NSURLSessionDataTask *)get_player_arrests_PlayerName:(NSString *)PlayerName
(void (^)(NSArray *results, NSError* error))completion
{
	NSURLSessionDataTask *task = [self GET:[NSString stringwithformat:@"/player/arrests/%@",PlayerName]
		parameters:nil
		success:^(NSURLSessionDataTask *task, id responseObject) {
			NSHTTPURLResponse *httpResponse = (NSHTTPURLResponse *)task.response;
			if (httpResponse.statusCode == 200) {
			} else {
			    dispatch_async(dispatch_get_main_queue(), ^{
				   completion(nil, nil);
			    }
			}}
		failure:^(NSURLSessionDataTask *task, NSError *error) {
			dispatch_async(dispatch_get_main_queue(), ^{
			    completion(nil, error);
			});
	}];
	return task;
}

- (NSURLSessionDataTask *)get_position:
(void (^)(NSArray *results, NSError* error))completion
{
	NSURLSessionDataTask *task = [self GET:
		parameters:nil
		success:^(NSURLSessionDataTask *task, id responseObject) {
			NSHTTPURLResponse *httpResponse = (NSHTTPURLResponse *)task.response;
			if (httpResponse.statusCode == 200) {
			} else {
			    dispatch_async(dispatch_get_main_queue(), ^{
				   completion(nil, nil);
			    }
			}}
		failure:^(NSURLSessionDataTask *task, NSError *error) {
			dispatch_async(dispatch_get_main_queue(), ^{
			    completion(nil, error);
			});
	}];
	return task;
}

- (NSURLSessionDataTask *)get_position_topTeams_PositionID:(NSString *)PositionID
(void (^)(NSArray *results, NSError* error))completion
{
	NSURLSessionDataTask *task = [self GET:[NSString stringwithformat:@"/position/topTeams/%@",PositionID]
		parameters:nil
		success:^(NSURLSessionDataTask *task, id responseObject) {
			NSHTTPURLResponse *httpResponse = (NSHTTPURLResponse *)task.response;
			if (httpResponse.statusCode == 200) {
			} else {
			    dispatch_async(dispatch_get_main_queue(), ^{
				   completion(nil, nil);
			    }
			}}
		failure:^(NSURLSessionDataTask *task, NSError *error) {
			dispatch_async(dispatch_get_main_queue(), ^{
			    completion(nil, error);
			});
	}];
	return task;
}

- (NSURLSessionDataTask *)get_position_topCrimes_PositionID:(NSString *)PositionID
(void (^)(NSArray *results, NSError* error))completion
{
	NSURLSessionDataTask *task = [self GET:[NSString stringwithformat:@"/position/topCrimes/%@",PositionID]
		parameters:nil
		success:^(NSURLSessionDataTask *task, id responseObject) {
			NSHTTPURLResponse *httpResponse = (NSHTTPURLResponse *)task.response;
			if (httpResponse.statusCode == 200) {
			} else {
			    dispatch_async(dispatch_get_main_queue(), ^{
				   completion(nil, nil);
			    }
			}}
		failure:^(NSURLSessionDataTask *task, NSError *error) {
			dispatch_async(dispatch_get_main_queue(), ^{
			    completion(nil, error);
			});
	}];
	return task;
}

- (NSURLSessionDataTask *)get_position_timeline_PositionID:(NSString *)PositionID
(void (^)(NSArray *results, NSError* error))completion
{
	NSURLSessionDataTask *task = [self GET:[NSString stringwithformat:@"/position/timeline/%@",PositionID]
		parameters:nil
		success:^(NSURLSessionDataTask *task, id responseObject) {
			NSHTTPURLResponse *httpResponse = (NSHTTPURLResponse *)task.response;
			if (httpResponse.statusCode == 200) {
			} else {
			    dispatch_async(dispatch_get_main_queue(), ^{
				   completion(nil, nil);
			    }
			}}
		failure:^(NSURLSessionDataTask *task, NSError *error) {
			dispatch_async(dispatch_get_main_queue(), ^{
			    completion(nil, error);
			});
	}];
	return task;
}

- (NSURLSessionDataTask *)get_position_arrests_PositionID:(NSString *)PositionID
(void (^)(NSArray *results, NSError* error))completion
{
	NSURLSessionDataTask *task = [self GET:[NSString stringwithformat:@"/position/arrests/%@",PositionID]
		parameters:nil
		success:^(NSURLSessionDataTask *task, id responseObject) {
			NSHTTPURLResponse *httpResponse = (NSHTTPURLResponse *)task.response;
			if (httpResponse.statusCode == 200) {
			} else {
			    dispatch_async(dispatch_get_main_queue(), ^{
				   completion(nil, nil);
			    }
			}}
		failure:^(NSURLSessionDataTask *task, NSError *error) {
			dispatch_async(dispatch_get_main_queue(), ^{
			    completion(nil, error);
			});
	}];
	return task;
}

