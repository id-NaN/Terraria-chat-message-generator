import json



with open("terraria_items.tsv", "r") as items:
	item_list_raw = items.read().split("\n")



final_list = []
for item_raw in item_list_raw:
	item = {}
	item_id, item_name, item_internal_name = item_raw.split("\t")
	item["item_id"] = int(item_id)
	item["item_name"] = item_name
	item["wiki_url"] = "https://terraria.gamepedia.com/" + item_name.replace(" ", "_")
	item["internal_name"] = item_internal_name
	final_list.append(item)



with open("terraria_items.json", "w") as result_file:
	json.dump(final_list, result_file, indent = 4)