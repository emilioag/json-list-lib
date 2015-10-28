import unittest
from jsonllib import *


class TestJSON_ListLib(unittest.TestCase):
    def test_diferences_betwen_2_lists_equals(self):
        add = ["elem1", "elem2", "elem3"]
        delete = ["elem1", "elem2", "elem3"]
        self.assertEquals(([], []), diff(add, delete))

    def test_diferences_with_more_adds_than_deletes(self):
        add = ["elem1", "elem3", "elem2", "elem3"]
        delete = ["elem1", "elem2", "elem3"]
        self.assertEquals((["elem3"], []), diff(add, delete))

    def test_diferences_with_more_adds_than_deletes_and_duplicate_adds(self):
        add = ["elem1", "elem3", "elem2", "elem3", "elem3", "elem3"]
        delete = ["elem1", "elem2", "elem3"]
        self.assertEquals((["elem3"], []), diff(add, delete))

    def test_diferences_with_more_deletes_than_adds(self):
        add = ["elem1", "elem3", "elem2"]
        delete = ["elem1", "elem2", "elem3", "elem4"]
        self.assertEquals(([], ["elem4"]), diff(add, delete))

    def test_diferences_betwen_two_lists(self):
        add = ["elem1", "elem3", "elem2", "elem2", "elem2", "elem3", "elem5"]
        delete = ["elem1", "elem2", "elem3", "elem4"]
        expected_add = ["elem3", "elem2", "elem5"]
        expected_add.sort()
        expected_del = ["elem4"]
        expected_del.sort()
        (obtained_add, obtainted_del) = diff(add, delete)
        obtained_add.sort()
        obtainted_del.sort()
        self.assertEquals((expected_add, expected_del),
                          (obtained_add, obtainted_del))


class TestJSON_ListLib_dictionaries(unittest.TestCase):
    def test_diferences_betwen_2_lists_equals(self):
        add = [{"key": "elem1", "value": 0},
               {"key": "elem2", "value": 1},
               {"key": "elem3", "value": 2}]
        delete = [{"key": "elem1", "value": 3},
                  {"key": "elem2", "value": 4},
                  {"key": "elem3", "value": 5}]
        self.assertEquals(([], []), diff(add, delete, "key"))

    def test_diferences_with_more_adds_than_deletes(self):
        add = [{"key": "elem1", "value": 0},
               {"key": "elem2", "value": 1},
               {"key": "elem3", "value": 2},
               {"key": "elem1", "value": 0}]
        delete = [{"key": "elem1", "value": 3},
                  {"key": "elem2", "value": 4},
                  {"key": "elem3", "value": 5}]
        (a, d) = diff(add, delete, "key")
        (expected_add, expected_del) = (["elem1"], [])
        expected_del.sort()
        obtained_add = [i["key"] for i in a]
        obtainted_del = [i["key"] for i in d]
        obtainted_del.sort()
        self.assertEquals((expected_add, expected_del),
                          (obtained_add, obtainted_del))

    def test_diferences_with_more_deletes_than_adds(self):
        add = [{"key": "elem1", "value": 0},
               {"key": "elem2", "value": 1},
               {"key": "elem3", "value": 2}]
        delete = [{"key": "elem1", "value": 3},
                  {"key": "elem2", "value": 4},
                  {"key": "elem3", "value": 5},
                  {"key": "elem1", "value": 0}]
        (a, d) = diff(add, delete, "key")
        (expected_add, expected_del) = ([], ["elem1"])
        expected_del.sort()
        obtained_add = [i["key"] for i in a]
        obtainted_del = [i["key"] for i in d]
        obtainted_del.sort()
        self.assertEquals((expected_add, expected_del),
                          (obtained_add, obtainted_del))

    def test_diferences_betwen_two_lists(self):
        add = [{"key": "elem1", "value": 0},
               {"key": "elem2", "value": 1},
               {"key": "elem3", "value": 2},
               {"key": "elem1", "value": 0},
               {"key": "elem1", "value": 0}]
        delete = [{"key": "elem1", "value": 3},
                  {"key": "elem2", "value": 4},
                  {"key": "elem3", "value": 5},
                  {"key": "elem1", "value": 0},
                  {"key": "elem4", "value": 0},
                  {"key": "elem5", "value": 0},
                  {"key": "elem6", "value": 0},
                  {"key": "elem7", "value": 0}]
        (a, d) = diff(add, delete, "key")
        expected_add = ["elem1"]
        expected_del = ["elem4", "elem5", "elem6", "elem7"]
        expected_del.sort()
        obtained_add = [i["key"] for i in a]
        obtainted_del = [i["key"] for i in d]
        obtainted_del.sort()
        self.assertEquals((expected_add, expected_del),
                          (obtained_add, obtainted_del))
