import logging
from  cli import generator, cli_args

from gen_spec import IntGenSpec, StringGenSpec, ObjectIdGenSpec

logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',
                    level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')

# Setup any fields you wish to target with queries
generator.with_field('customer._id', IntGenSpec(0, 1000000), method='gte_lt')
generator.with_field('customer.name', StringGenSpec().upper(), method='gte_lt')

# Run
try:
    logging.info('Starting')

    doc_count = generator.run(cli_args.iteration_count)

    logging.info(f'{doc_count} documents found')
except Exception as e:
    logging.exception(e)

