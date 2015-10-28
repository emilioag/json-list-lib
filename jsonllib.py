def json_path(json, path):
    for x in path.split("."):
        json = json.get(x)
    return json


def get_elem_with_key(key_name, path, list):
    output = None
    for elem in list:
        if json_path(elem, path) == key_name:
            output = elem
            break
    return output


def diff_basic(to_add, to_del):
    (adds, dels) = to_add, []
    for item_2_del in to_del:
        if item_2_del in to_add:
            adds.remove(item_2_del)
        else:
            dels.append(item_2_del)
    return list(set(adds)), list(set(dels))


def diff_docs(items_2_add, items_2_del, path):
    adds = items_2_add
    dels = []
    for item_2_del in items_2_del:
        value_of_key_item_2_del = json_path(item_2_del, path)
        del_from_adds = False
        for item_2_add in items_2_add:
            value_of_key_item_to_add = json_path(item_2_add, path)
            if value_of_key_item_to_add == value_of_key_item_2_del:
                del_from_adds = True
                break

        if del_from_adds:
            elem = get_elem_with_key(item_2_del["key"], path, adds)
            if elem is not None:
                adds.remove(elem)
        else:
            insert = True
            for delItem in dels:
                if value_of_key_item_2_del == json_path(delItem, path):
                    insert = False
                    break
            if insert:
                dels.append(item_2_del)
    return adds, dels


def diff(a, b, path=None):
    (adds, dels) = a, []
    if path is not None:
        (adds, dels) = diff_docs(a, b, path)
    else:
        (adds, dels) = diff_basic(a, b)
    return adds, dels
