import unittest
from gen_spec import IntGenSpec, ObjectIdGenSpec
from bson import objectid
from load_generator import LoadGenerator

SORT_SPEC = {'state': 1, 'city': -1}


class Test_LoadGenerator(unittest.TestCase):
    def test_with_url(self):
        self.assertEqual(LoadGenerator().with_url(
            'mongodb+srv://localhost/').mongo_url, 'mongodb+srv://localhost/')

    def test_with_db(self):
        self.assertEqual(LoadGenerator().with_db('db1').db_name, 'db1')

    def test_with_collection(self):
        self.assertEqual(LoadGenerator().with_collection(
            'the_collection').collection_name, 'the_collection')

    def test_with_field(self):
        self.assertTrue('foo' in LoadGenerator().with_field(
            'foo', None).query_fields.keys())

    def test__generate_query_eq(self):
        actual = LoadGenerator().with_field('foo', ObjectIdGenSpec())._generate_query()
        self.assertIsNotNone(actual['foo']['$eq'])

    def test__generate_query_gte_lt(self):
        actual = LoadGenerator().with_field('foo', ObjectIdGenSpec(),
                                            method='gte_lt')._generate_query()
        self.assertIsNotNone(actual['foo']['$gte'])
        self.assertIsNotNone(actual['foo']['$lt'])

    def test_with_sort(self):
        actual = LoadGenerator().with_sort(SORT_SPEC)
        self.assertEqual(actual.sort_spec, SORT_SPEC)



    def test_create_command(self):
        target = LoadGenerator()
        actual = target.create_command(
            123, 'my_name', {'match_me': 11}, {'sort_me': -1}, 33)

        self.assertEqual(actual['find'], 'my_name')
        self.assertEqual(actual['filter']['match_me'], 11)
        self.assertEqual(actual['sort']['sort_me'], -1)
        self.assertEqual(actual['limit'], 33)
        self.assertEqual(actual['comment'], 'load_generator 123')


if __name__ == '__main__':
    unittest.main()
