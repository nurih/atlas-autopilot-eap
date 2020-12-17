import unittest
from gen_spec import IntGenSpec,  ObjectIdGenSpec, StringGenSpec,DateGenSpec
from bson import objectid
import string
from datetime import *

ALPHABET = 'abc123'


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

    def test_string_alphabet_default(self):
        actual = StringGenSpec(ALPHABET)
        self.assertEqual(actual.alphabet, ALPHABET)

    def test_string_printbale_alphabet(self):
        actual = StringGenSpec().printable()
        self.assertEqual(actual.alphabet, string.ascii_letters)

    def test_string_printbale_upper_alphabet(self):
        actual = StringGenSpec().upper()
        self.assertEqual(actual.alphabet, string.ascii_uppercase)

    def test_string_generate_length(self):
        actual = StringGenSpec(length=12).generate()
        self.assertEqual(len(actual), 12)

    def test_string_eq(self):
        actual = StringGenSpec().eq()
        self.assertIsInstance(actual['$eq'], str)

    def test_string_gte_lt(self):
        actual = StringGenSpec().gte_lt()
        self.assertIsInstance(actual['$gte'], str)
        self.assertIsInstance(actual['$lt'], str)

    def test_date_start(self):
        actual = DateGenSpec()
        self.assertIsInstance(actual.start, datetime)

    def test_date_end(self):
        actual = DateGenSpec()
        self.assertIsInstance(actual.end, datetime)

    def test_date_generage(self):
        subject = DateGenSpec()
        actual = subject.generate()
        self.assertTrue(actual < subject.end and actual >= subject.start )



if __name__ == '__main__':
    unittest.main()
