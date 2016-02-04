//
//	player.swift Generate By modelGenerator
//	Create the Fri Feb  5 00:50:58 2016
//	https://github.com/inso-/modelGenerator
//

import UIKit


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