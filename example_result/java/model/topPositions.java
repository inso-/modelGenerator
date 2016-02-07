//
//	topPositions.java Generate By modelGenerator
//	Create the Sun Feb  7 05:19:32 2016
//	https://github.com/inso-/modelGenerator
//

import org.json.JSONException;
import org.json.JSONObject;

public class topPositions{

	private String Position;
	private String arrest_count;

	public topPositions(JSONObject data) {
		Position = data.optString("Position");
		arrest_count = data.optString("arrest_count");
		}
		catch (JSONException je) {

		}
		return data;
	}

	public JSONObject toJSON() {
		JSONObject data = new JSONObject();
		try {
			data.put("Position", Position);
 			data.put("arrest_count", arrest_count);
 		}

	public String getCategory() {
		return Category;
	}

	public void setCategory(String ParamCategory) {
		Category = ParamCategory;
	}

	public String getArrest_count() {
		return arrest_count;
	}

	public void setArrest_count(String Paramarrest_count) {
		arrest_count = Paramarrest_count;
	}

	public String getArrest_count() {
		return arrest_count;
	}

	public void setArrest_count(String Paramarrest_count) {
		arrest_count = Paramarrest_count;
	}

	public String getTeam() {
		return Team;
	}

	public void setTeam(String ParamTeam) {
		Team = ParamTeam;
	}

	public String getPosition() {
		return Position;
	}

	public void setPosition(String ParamPosition) {
		Position = ParamPosition;
	}

	public String getArrest_count() {
		return arrest_count;
	}

	public void setArrest_count(String Paramarrest_count) {
		arrest_count = Paramarrest_count;
	}


}