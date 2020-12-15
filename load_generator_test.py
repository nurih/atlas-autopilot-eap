import unittest
from gen_spec import IntGenSpec, ObjectIdGenSpec
from bson import objectid
from load_generator import LoadGenerator


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


if __name__ == '__main__':
    unittest.main()
