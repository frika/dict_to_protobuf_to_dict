import copy
import unittest

from dict_to_protobuf_to_dict import dict_to_protobuf, protobuf_to_dict

from test.sample_pb2 import MainMessage


class TestProtoUtilModule(unittest.TestCase):

    def setUp(self):
        dct = {}
        dct["a_str"] = "Neeraj Koul"
        dct["int_to_lst_ints_map"] = {1: {"lst_ints": [0, 1]}, 2: {"lst_ints": [2, 3]}, 3: {"lst_ints": [4, 5]}}
        dct["an_enum"] = "second"
        dct["an_int"] = 2
        dct["lst_ints"] = [0, 1, 2]
        dct["str_to_message_map"] = {"where_from" : 
                                             {"a_str": "Kashmir", 
                                              "a_long": 1L, 
                                              "lst_longs": [1L, 2L, 3L]
                                              }
                                        }
        self.data_dct = dct
        self.main_msg_fields = self.data_dct.keys()

    def tearDown(self):
        self.data_dct, self.main_msg_fields = None, None

    def _are_fields_in_proto_msg(self, message, fields=[]):
        name_map = {}
        for field, _ in message.ListFields():
            name_map[field.name] = None
        for field in fields:
            if field not in name_map:
                return False
        return True

    def test_all_populated(self):
        msg = MainMessage()
        dict_to_protobuf(self.data_dct, msg)

        self.assertTrue(self._are_fields_in_proto_msg(msg, self.data_dct.keys()))

        dct = protobuf_to_dict(msg)

        self.assertEqual(dct, self.data_dct)

    def test_basic_scalar_manipulation(self):
        self.data_dct.pop("a_str")
        self.data_dct.pop("an_int")

        msg = MainMessage()
        dict_to_protobuf(self.data_dct, msg)

        self.assertFalse(self._are_fields_in_proto_msg(msg, ["a_str", "an_int"]))

        dct = protobuf_to_dict(msg)
        self.assertEqual(dct["a_str"], "")
        self.assertEqual(dct["an_int"], 0)

    def test_list_manipulation(self):
        self.data_dct["lst_ints"] = []
        msg = MainMessage()
        dict_to_protobuf(self.data_dct, msg)

        self.assertFalse(self._are_fields_in_proto_msg(msg, ["lst_ints"]))
        self.assertTrue(self._are_fields_in_proto_msg(msg, ["a_str"]))

        dct = protobuf_to_dict(msg)
        self.assertEqual(dct["lst_ints"], [])

    def test_enum_manipulation(self):
        self.data_dct["an_enum"] = "first"
        msg = MainMessage()
        dict_to_protobuf(self.data_dct, msg)

        # Am constant value 0 is not sent in enum even if we explicitly set it
        self.assertFalse(self._are_fields_in_proto_msg(msg, ["an_enum"]))

        dct = protobuf_to_dict(msg)
        self.assertEqual(dct["an_enum"], "first")


        # We check for the constant 1, which will be sent in the proto message
        self.data_dct["an_enum"] = "second"
        msg = MainMessage()
        dict_to_protobuf(self.data_dct, msg)

        # Am constant value 0 is not sent in enum even if we explicitly set it
        self.assertTrue(self._are_fields_in_proto_msg(msg, ["an_enum"]))

    def test_map_manipulation(self):
        self.data_dct["int_to_lst_ints_map"][1] = {}
        self.data_dct["int_to_lst_ints_map"].pop(2)

        self.data_dct["str_to_message_map"]["where_from"].pop("a_long")

        msg = MainMessage()
        dict_to_protobuf(self.data_dct, msg)

        self.assertTrue(1 in getattr(msg, "int_to_lst_ints_map").keys())
        self.assertTrue(2 not in getattr(msg, "int_to_lst_ints_map").keys())

        dct = protobuf_to_dict(msg)
        self.assertEqual(dct["int_to_lst_ints_map"][1], {"lst_ints": []})
        self.assertEqual(dct["int_to_lst_ints_map"][3], self.data_dct["int_to_lst_ints_map"][3])

        check_dct = {"a_str": "Kashmir", "lst_longs": [1L, 2L, 3L], "a_long": 0L}
        self.assertEqual(dct["str_to_message_map"]["where_from"], check_dct)

    def test_serialising_data_which_is_not_part_of_schema(self):
        data_dct_copy = copy.deepcopy(self.data_dct)

        self.data_dct["new_int"] = 11
        msg = MainMessage()
        dict_to_protobuf(self.data_dct, msg)

        self.assertFalse(self._are_fields_in_proto_msg(msg, ["new_int"]))

        dct = protobuf_to_dict(msg)

        self.assertEqual(dct, data_dct_copy)

if __name__ == '__main__':
    unittest.main()
