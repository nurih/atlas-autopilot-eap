import pymongo


class LoadGenerator:

    def __init__(self):
        self.query_fields = {}

    def with_url(self, mongo_url):
        self.mongo_url = mongo_url
        return self

    def with_db(self, db_name):
        self.db_name = db_name
        return self

    def with_collection(self, collection_name):
        self.collection_name = collection_name
        return self

    def with_field(self, field_name, gen_spec):
        self.query_fields[field_name] = gen_spec
        return self

    def run(self, count, limit=10):
        collection = pymongo.MongoClient(self.mongo_url) \
            .get_database(self.db_name) \
            .get_collection(self.collection_name)

        doc_count = 0
        for i in range(0, count):
            query = self._generate_query()
            for d in collection.find(query).limit(limit):
                doc_count = doc_count+1

        return doc_count

    def _generate_query(self):
        query = {}
        for k, v in self.query_fields.items():
            query[k] = v.eq()

        return query
