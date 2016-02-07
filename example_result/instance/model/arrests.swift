//
//	arrests.swift Generate By modelGenerator
//	Create the Sun Feb  7 05:12:51 2016
//	https://github.com/inso-/modelGenerator
//

class arrests: NSObject {

	var Category: String!
	var Name: String!
	var Encounter: String!
	var resolution_category_id: String!
	var general_category_id: String!
	var legal_level_id: String!
	var Team: String!
	var Date: String!
	var Position: String!
	var Outcome: String!
	var arrest_stats_id: String!
	var Description: String!

	init(data: NSDictionary)
	{
		super.init()
		self.setValuesForKeysWithDictionary(data as! [String : AnyObject])
	}

}