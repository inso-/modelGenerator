//
//	player.swift Generate By modelGenerator
//	Create the Sun Feb  7 05:12:51 2016
//	https://github.com/inso-/modelGenerator
//

class player: NSObject {

	var Position: String!
	var arrest_count: String!
	var Name: String!

	init(data: NSDictionary)
	{
		super.init()
		self.setValuesForKeysWithDictionary(data as! [String : AnyObject])
	}

}