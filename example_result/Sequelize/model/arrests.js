//
//	arrests.js Generate By modelGenerator
//	Create the Sun Feb  7 05:19:32 2016
//	https://github.com/inso-/modelGenerator
//

module.exports = function(sequelize, DataTypes) {
return sequelize.define('arrests', {
	Category: {
		type: DataTypes.TEXT
	};	
	Name: {
		type: DataTypes.TEXT
	};	
	Encounter: {
		type: DataTypes.TEXT
	};	
	resolution_category_id: {
		type: DataTypes.TEXT
	};	
	general_category_id: {
		type: DataTypes.TEXT
	};	
	legal_level_id: {
		type: DataTypes.TEXT
	};	
	Team: {
		type: DataTypes.TEXT
	};	
	Date: {
		type: DataTypes.TEXT
	};	
	Position: {
		type: DataTypes.TEXT
	};	
	Outcome: {
		type: DataTypes.TEXT
	};	
	arrest_stats_id: {
		type: DataTypes.TEXT
	};	
	Description: {
		type: DataTypes.TEXT
	};	

};