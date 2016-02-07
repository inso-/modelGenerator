//
//	position.swift Generate By modelGenerator
//	Create the Sun Feb  7 05:19:32 2016
//	https://github.com/inso-/modelGenerator
//

class position: NSObject {

	var Position: String!
	var arrest_count: String!

	init(data: NSDictionary)
	{
		super.init()
		self.setValuesForKeysWithDictionary(data as! [String : AnyObject])
	}

}