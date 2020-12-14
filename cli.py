import load_generator
from load_generator import *

gen = LoadGenerator().with_url(
    'mongodb://localhost:27017/').with_db('test').with_collection('scores')

gen.with_field('score', IntGenSpec(0, 10))

doc_count = gen.run(100)

print(f'{doc_count} found')
