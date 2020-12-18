import logging
from pymongo import MongoClient


class LoadGenerator:

    def __init__(self):
        self.query_fields = {}
        self.sort_spec = None

    def with_url(self, mongo_url):
        self.mongo_url = mongo_url
        return self

    def with_db(self, db_name):
        self.db_name = db_name
        return self

    def with_collection(self, collection_name):
        self.collection_name = collection_name
        return self

    def with_field(self, field_name, gen_spec, method='eq'):
        self.query_fields[field_name] = {
            'generator': gen_spec, 'method': method}
        return self

    def with_sort(self, sort_spec):
        self.sort_spec = sort_spec
        return self

    def run(self, count, limit=10):
        db = MongoClient(self.mongo_url) \
            .get_database(self.db_name)

        # .get_collection(self.collection_name)

        doc_count = 0
        for ordinal in range(0, count):
            query = self._generate_query()
            cmd = self.create_command(ordinal, self.collection_name, query, self.sort_spec, limit)
            for d in db.command(cmd):
                doc_count = doc_count + 1                
            logging.info((ordinal, doc_count, cmd['filter'], cmd.get('sort', '_unsorted_')))
        return doc_count

    def create_command(self, number, collection_name, query, sort, limit):
        result = {
            "find": collection_name,
            "filter": query,
            "limit": limit,
            "comment": f'load_generator {number}'
        }

        if sort is not None:
            result['sort'] = sort
        return result

    def _generate_query(self):
        query = {}
        for k, gen in self.query_fields.items():
            query[k] = getattr(gen['generator'], gen['method'])()

        return query
