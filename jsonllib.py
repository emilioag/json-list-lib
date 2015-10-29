def get_elem_with_key(key_name, path, l):
    output = None
    for elem in l:
        if json_path(elem, path) == key_name:
            output = elem
            break
    return output


def json_path(json, path):
    for x in path.split("."):
        json = json.get(x)
    return json


def diff_basic(to_add, to_del):
    (adds, dels) = to_add, []
    for item_2_del in to_del:
        if item_2_del in to_add:
            adds.remove(item_2_del)
        else:
            dels.append(item_2_del)
    return list(set(adds)), list(set(dels))


def diff(a, b, path=None):
    (adds, dels) = a, []
    if path is not None:
        (adds, dels) = diff_basic(map(lambda x: json_path(x, path), a),
                                  map(lambda x: json_path(x, path), b))
        adds = [get_elem_with_key(i, path, a) for i in adds]
        dels = [get_elem_with_key(i, path, b) for i in dels]
    else:
        (adds, dels) = diff_basic(a, b)
    return adds, dels
