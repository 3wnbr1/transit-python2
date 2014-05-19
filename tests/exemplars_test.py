# Copyright (c) Cognitect, Inc.
# All rights reserved.
import unittest
from transit.reader import JsonUnmarshaler, MsgPackUnmarshaler
from transit.writer import MsgPackMarshaler, JsonMarshaler
from transit.transit_types import Keyword, Symbol
from StringIO import StringIO
from helpers import ints_centered_on, mapcat
from uuid import UUID

class ExemplarBaseTest(unittest.TestCase):
    pass

def exemplar(name, val):
    class ExemplarTest(ExemplarBaseTest):
        def test_json(self):
            with open("../transit/simple-examples/" + name + ".json", 'r') as stream:
                data = JsonUnmarshaler().load(stream)
                self.assertEqual(val, data)

        def test_msgpack(self):
            with open("../transit/simple-examples/" + name + ".mp", 'r') as stream:
                data = MsgPackUnmarshaler().load(stream)
                self.assertEqual(val, data)

        def test_reencode_msgpack(self):
            io = StringIO()
            marshaler = MsgPackMarshaler(io)
            marshaler.marshal_top(val)
            s = io.getvalue()
            io = StringIO(s)
            newval = MsgPackUnmarshaler().load(io)
            self.assertEqual(val, newval)

        def test_reencode_json(self):
            io = StringIO()
            marshaler = JsonMarshaler(io)
            marshaler.marshal_top(val)
            s = io.getvalue()
            print s
            io = StringIO(s)
            newval = JsonUnmarshaler().load(io)
            self.assertEqual(val, newval)

    globals()["test_" + name + "_json"] = ExemplarTest

ARRAY_SIMPLE = (1, 2, 3)
ARRAY_MIXED = (0, 1, 2.0, True, False, 'five', Keyword("six"), Symbol("seven"), '~eight', None)
ARRAY_NESTED = (ARRAY_SIMPLE, ARRAY_MIXED)
SMALL_STRINGS = ("", "a", "ab", "abc", "abcd", "abcde", "abcdef")
POWERS_OF_TWO = tuple(map(lambda x: pow(2, x), range(66)))
INTERESTING_INTS = tuple(mapcat(lambda x: ints_centered_on(x, 2), POWERS_OF_TWO))

UUIDS = (UUID('5a2cbea3-e8c6-428b-b525-21239370dd55'),
         UUID('d1dc64fa-da79-444b-9fa4-d4412f427289'),
         UUID('501a978e-3a3e-4060-b3be-1cf2bd4b1a38'),
         UUID('b3ba141a-a776-48e4-9fae-a28ea8571f58'))

exemplar("nil", None)
exemplar("true", True)
exemplar("false", False)
exemplar("zero", 0)
exemplar("one", 1)
exemplar("one_string", "hello")
exemplar("one_keyword", Keyword("hello"))
exemplar("one_symbol", Symbol("hello"))
exemplar("vector_simple", ARRAY_SIMPLE)
exemplar("vector_empty", ())
exemplar("vector_mixed", ARRAY_MIXED)
exemplar("vector_nested", ARRAY_NESTED)
exemplar("small_strings", SMALL_STRINGS)
exemplar("strings_tilde", tuple(map(lambda x: "~" + x, SMALL_STRINGS)))
exemplar("strings_hash", tuple(map(lambda x: "#" + x, SMALL_STRINGS)))
exemplar("strings_hat", tuple(map(lambda x: "^" + x, SMALL_STRINGS)))
exemplar("ints", tuple(range(128)))
exemplar("small_ints", ints_centered_on(0))
exemplar("ints_interesting", INTERESTING_INTS)
exemplar("ints_interesting_neg", tuple(map(lambda x: -x, INTERESTING_INTS)))
exemplar("doubles_small", tuple(map(float, ints_centered_on(0))))
exemplar("doubles_interesting", (-3.14159, 3.14159, 4E11, 2.998E8, 6.626E-34))
exemplar("one_uuid", UUIDS[0])

if __name__=='__main__':
    unittest.main()