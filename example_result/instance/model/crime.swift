//
//	crime.swift Generate By modelGenerator
//	Create the Sun Feb  7 05:12:51 2016
//	https://github.com/inso-/modelGenerator
//

class crime: NSObject {

	var Category: String!
	var arrest_count: String!

	init(data: NSDictionary)
	{
		super.init()
		self.setValuesForKeysWithDictionary(data as! [String : AnyObject])
	}

}