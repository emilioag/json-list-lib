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
        json = json.get(x) if isinstance(json, dict) else None
    return json


def __diff(l1, l2):
    """Returns the list differences:
       - o1 Returns the elements that appear more times in l1 than in
         l2.
       - o2 Returns the elements that appear more times in l2 than in
         l1."""
    (o1, o2) = l1, []
    for item in l2:
        o1.remove(item) if item in l1 else o2.append(item)
    return list(set(o1)), list(set(o2))


def diff(a, b, f=None):
    """Returns the list differences:
       - f is the function which is needed to apply for each element of the list
         to transform the list in a basic list
       - Returns a whith the elements that appears more times in a than in b
       - Returns b whith the elements that appears more times in b than in a"""
    return (__diff(map(f, a), map(f, b)) if f is not None else __diff(a, b))
