import frappe

@frappe.whitelist()
def test_api_method(h):
    print("----------------h" + str(h))

@frappe.whitelist()
def item_list():
    try:
        item_list=frappe.get_list("Item",filters={},fields=["*"])
        return {"data": item_list}
    except Exception as e:
        return e

def does_item_belong_to_pos(item_code, pos_name):
    item_list=frappe.get_list("PosWrapper", filters={"parent": item_code},fields=["parent"])
    return len(item_list) > 0


@frappe.whitelist()
def item_list_for(pos_profile):
    try:
        # pos_profile = "Pos 1"
        pos_filtered=frappe.get_list("PosWrapper", filters={"pos_profile": pos_profile},fields=["parent"])
        pos_dic = {}
        for pos in pos_filtered:
            pos_dic[pos.parent] = True
        
        item_list=frappe.get_list("Item", filters={},fields=["item_name, item_code"])
        item_filtered = []
        for item in item_list:
            if item["item_code"] in pos_dic:
                item['pos_profile'] = pos_profile
                item_filtered.append(item)
            
        return {"data": item_filtered}
    except Exception as e:
        return e

@frappe.whitelist()
def item_list_filtered():
    try:
        item_list=frappe.get_list("Item", filters={},fields=["item_name, item_code"])
        items = []
        for item in item_list:
            code = item["item_code"]
            print(code)
        return {"data": item_list}
    except Exception as e:
        return e