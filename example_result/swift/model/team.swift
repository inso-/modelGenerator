//
//	team.swift Generate By modelGenerator
//	Create the Sun Feb  7 05:19:31 2016
//	https://github.com/inso-/modelGenerator
//

class team: NSObject {

	var arrest_count: String!
	var Team: String!

	init(data: NSDictionary)
	{
		super.init()
		self.setValuesForKeysWithDictionary(data as! [String : AnyObject])
	}

}