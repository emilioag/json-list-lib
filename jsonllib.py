def get_elem_with_key(key_name, path, l):
    """Returns the element of the list l which has as value in the path,
       key_name."""
    output = None
    for elem in l:
        if json_path(elem, path) == key_name:
            output = elem
            break
    return output


def json_path(json, path):
    """Returns the value of the nested key located in path."""
    for x in path.split("."):
        json = json.get(x)
    return json


def diff_basic(to_add, to_del):
    """Returns the list differences:
       - adds Returns the elements that appear more times in to_add than in
         to_del.
       - dels Returns the elements that appear more times in to_del than in
         to_add."""
    (adds, dels) = to_add, []
    for item_2_del in to_del:
        if item_2_del in to_add:
            adds.remove(item_2_del)
        else:
            dels.append(item_2_del)
    return list(set(adds)), list(set(dels))


def diff(a, b, path=None):
    """Returns the list differences:
       - adds Returns the elements that appear more times in to_add than in
         to_del.
       - dels Returns the elements that appear more times in to_del than in
         to_add.
       - In this context, appear means that th key value in path appears in
         any element"""
    (adds, dels) = a, []
    if path is not None:
        (adds, dels) = diff_basic(map(lambda x: json_path(x, path), a),
                                  map(lambda x: json_path(x, path), b))
        adds = [get_elem_with_key(i, path, a) for i in adds]
        dels = [get_elem_with_key(i, path, b) for i in dels]
    else:
        (adds, dels) = diff_basic(a, b)
    return adds, dels
