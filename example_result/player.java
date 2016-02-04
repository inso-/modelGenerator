//
//	player.java Generate By modelGenerator
//	Create the Fri Feb  5 00:50:58 2016
//	https://github.com/inso-/modelGenerator
//

import org.json.JSONException;
import org.json.JSONObject;

public class player{

	private String Position;
	private String arrest_count;
	private String Name;

	public player(JSONObject data) {
		Position = data.optString("Position");
		arrest_count = data.optString("arrest_count");
		Name = data.optString("Name");
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
 			data.put("Name", Name);
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

	public String getName() {
		return Name;
	}

	public void setName(String ParamName) {
		Name = ParamName;
	}


}