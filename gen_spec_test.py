import unittest
from gen_spec import IntGenSpec,  ObjectIdGenSpec
from bson import objectid

class Test_GenSpec(unittest.TestCase):
    def test_objectid(self):
        actual = ObjectIdGenSpec().generate()
        self.assertIsInstance(actual, objectid.ObjectId)

    def test_objectid(self):
        actual = ObjectIdGenSpec().eq()
        self.assertIsInstance(actual['$eq'], objectid.ObjectId)

    def test_int(self):
        actual = IntGenSpec(1, 3).generate()
        self.assertIn(actual, [1, 2, 3])

    def test_eq_int(self):
        actual = IntGenSpec(1, 2).eq()
        self.assertIsInstance(actual['$eq'], int)


if __name__ == '__main__':
    unittest.main()
