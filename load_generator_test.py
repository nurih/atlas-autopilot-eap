import load_generator
import unittest
from load_generator import IntGenSpec, LoadGenerator, ObjectIdGenSpec
from bson import objectid


class Test_LoadGenerator(unittest.TestCase):
    def test_with_url(self):
        self.assertEqual(LoadGenerator().with_url('mongodb+srv://localhost/').mongo_url, 'mongodb+srv://localhost/')

    def test_with_db(self):
        self.assertEqual(LoadGenerator().with_db('db1').db_name, 'db1')

    def test_with_collection(self):
        self.assertEqual(LoadGenerator().with_collection(
            'the_collection').collection_name, 'the_collection')

    def test_with_field(self):
        self.assertTrue('foo' in LoadGenerator().with_field(
            'foo', None).query_fields.keys())

    def test__generate_query(self):
        actual = LoadGenerator().with_field('foo', ObjectIdGenSpec())._generate_query()
        self.assertIsNotNone(actual['foo']['$eq'])


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
