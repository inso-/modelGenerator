//
//	crime.java Generate By modelGenerator
//	Create the Sun Feb  7 05:12:51 2016
//	https://github.com/inso-/modelGenerator
//

import org.json.JSONException;
import org.json.JSONObject;

public class crime{

	private String Category;
	private String arrest_count;

	public crime(JSONObject data) {
		Category = data.optString("Category");
		arrest_count = data.optString("arrest_count");
		}
		catch (JSONException je) {

		}
		return data;
	}

	public JSONObject toJSON() {
		JSONObject data = new JSONObject();
		try {
			data.put("Category", Category);
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


}