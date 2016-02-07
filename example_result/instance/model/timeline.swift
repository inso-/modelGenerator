//
//	timeline.swift Generate By modelGenerator
//	Create the Sun Feb  7 05:12:51 2016
//	https://github.com/inso-/modelGenerator
//

class timeline: NSObject {

	var arrest_count: String!
	var Month: String!
	var Year: String!

	init(data: NSDictionary)
	{
		super.init()
		self.setValuesForKeysWithDictionary(data as! [String : AnyObject])
	}

}