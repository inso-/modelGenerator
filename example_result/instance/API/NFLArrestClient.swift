//
//	NFLArrestClient.swift Generate By modelGenerator
//	Create the Sun Feb  7 05:12:51 2016
//	https://github.com/inso-/modelGenerator
//

class NFLArrestClient : NSObject {
	struct Static {
		static var onceToken : dispatch_once_t = 0
		static var instance : NFLArrestClient? = nil
	}

	let functionSessionManager:AFHTTPSessionManager

	class var sharedInstance : NFLArrestClient{
		dispatch_once(&Static.onceToken) {
			Static.instance = NFLArrestClient()
		}
		return Static.instance!
	}

	override init() {
		let configuration = NSURLSessionConfiguration.ephemeralSessionConfiguration()
		configuration.HTTPAdditionalHeaders = [
			"Content-Type" : "application/json"
		]
		self.functionSessionManager = AFHTTPSessionManager(baseURL:NSURL(string:"www.NflArrest.com/api/v1"), sessionConfiguration:configuration)
		self.functionSessionManager.requestSerializer = AFJSONRequestSerializer()
		self.functionSessionManager.responseSerializer = AFJSONResponseSerializer()
	}

	func get_crime_topTeams_CrimeID(CrimeID : String) -> BFTask
	{
		let deferred = BFTaskCompletionSource()
		self.functionSessionManager.GET("/crime/topTeams/" + CrimeID, parameters:[:],
			success:{task, responseObject in
				deferred.setResult(responseObject)
		},
			failure:{task, error in
				deferred.setError(error)
		})
		return deferred.task
	}

	func get_crime_topPositions_CrimeID(CrimeID : String) -> BFTask
	{
		let deferred = BFTaskCompletionSource()
		self.functionSessionManager.GET("/crime/topPositions/" + CrimeID, parameters:[:],
			success:{task, responseObject in
				deferred.setResult(responseObject)
		},
			failure:{task, error in
				deferred.setError(error)
		})
		return deferred.task
	}

	func get_crime_timeline_CrimeID(CrimeID : String) -> BFTask
	{
		let deferred = BFTaskCompletionSource()
		self.functionSessionManager.GET("/crime/timeline/" + CrimeID, parameters:[:],
			success:{task, responseObject in
				deferred.setResult(responseObject)
		},
			failure:{task, error in
				deferred.setError(error)
		})
		return deferred.task
	}

	func get_crime_arrests_CrimeID(CrimeID : String) -> BFTask
	{
		let deferred = BFTaskCompletionSource()
		self.functionSessionManager.GET("/crime/arrests/" + CrimeID, parameters:[:],
			success:{task, responseObject in
				deferred.setResult(responseObject)
		},
			failure:{task, error in
				deferred.setError(error)
		})
		return deferred.task
	}

	func get_team_topPlayers_TeamID(TeamID : String) -> BFTask
	{
		let deferred = BFTaskCompletionSource()
		self.functionSessionManager.GET("/team/topPlayers/" + TeamID, parameters:[:],
			success:{task, responseObject in
				deferred.setResult(responseObject)
		},
			failure:{task, error in
				deferred.setError(error)
		})
		return deferred.task
	}

	func get_team_topCrimes_TeamID(TeamID : String) -> BFTask
	{
		let deferred = BFTaskCompletionSource()
		self.functionSessionManager.GET("/team/topCrimes/" + TeamID, parameters:[:],
			success:{task, responseObject in
				deferred.setResult(responseObject)
		},
			failure:{task, error in
				deferred.setError(error)
		})
		return deferred.task
	}

	func get_team_timeline_TeamID(TeamID : String) -> BFTask
	{
		let deferred = BFTaskCompletionSource()
		self.functionSessionManager.GET("/team/timeline/" + TeamID, parameters:[:],
			success:{task, responseObject in
				deferred.setResult(responseObject)
		},
			failure:{task, error in
				deferred.setError(error)
		})
		return deferred.task
	}

	func get_team_arrests_TeamID(TeamID : String) -> BFTask
	{
		let deferred = BFTaskCompletionSource()
		self.functionSessionManager.GET("/team/arrests/" + TeamID, parameters:[:],
			success:{task, responseObject in
				deferred.setResult(responseObject)
		},
			failure:{task, error in
				deferred.setError(error)
		})
		return deferred.task
	}

	func get_player_topCrimes_PlayerName(PlayerName : String) -> BFTask
	{
		let deferred = BFTaskCompletionSource()
		self.functionSessionManager.GET("/player/topCrimes/" + PlayerName, parameters:[:],
			success:{task, responseObject in
				deferred.setResult(responseObject)
		},
			failure:{task, error in
				deferred.setError(error)
		})
		return deferred.task
	}

	func get_player_arrests_PlayerName(PlayerName : String) -> BFTask
	{
		let deferred = BFTaskCompletionSource()
		self.functionSessionManager.GET("/player/arrests/" + PlayerName, parameters:[:],
			success:{task, responseObject in
				deferred.setResult(responseObject)
		},
			failure:{task, error in
				deferred.setError(error)
		})
		return deferred.task
	}

	func get_position_topTeams_PositionID(PositionID : String) -> BFTask
	{
		let deferred = BFTaskCompletionSource()
		self.functionSessionManager.GET("/position/topTeams/" + PositionID, parameters:[:],
			success:{task, responseObject in
				deferred.setResult(responseObject)
		},
			failure:{task, error in
				deferred.setError(error)
		})
		return deferred.task
	}

	func get_position_topCrimes_PositionID(PositionID : String) -> BFTask
	{
		let deferred = BFTaskCompletionSource()
		self.functionSessionManager.GET("/position/topCrimes/" + PositionID, parameters:[:],
			success:{task, responseObject in
				deferred.setResult(responseObject)
		},
			failure:{task, error in
				deferred.setError(error)
		})
		return deferred.task
	}

	func get_position_timeline_PositionID(PositionID : String) -> BFTask
	{
		let deferred = BFTaskCompletionSource()
		self.functionSessionManager.GET("/position/timeline/" + PositionID, parameters:[:],
			success:{task, responseObject in
				deferred.setResult(responseObject)
		},
			failure:{task, error in
				deferred.setError(error)
		})
		return deferred.task
	}

	func get_position_arrests_PositionID(PositionID : String) -> BFTask
	{
		let deferred = BFTaskCompletionSource()
		self.functionSessionManager.GET("/position/arrests/" + PositionID, parameters:[:],
			success:{task, responseObject in
				deferred.setResult(responseObject)
		},
			failure:{task, error in
				deferred.setError(error)
		})
		return deferred.task
	}


}