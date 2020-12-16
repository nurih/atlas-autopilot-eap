from  cli import generator, cli_args

from gen_spec import IntGenSpec, StringGenSpec, ObjectIdGenSpec

# Setup any fields you wish to target with queries
generator.with_field('customer._id', IntGenSpec(0, 1000000), method='gte_lt')
generator.with_field('customer.name', StringGenSpec().upper(), method='gte_lt')

# Run
try:
    doc_count = generator.run(cli_args.iteration_count)    
    
    print(f'{doc_count} documents found')
except Exception as e:
    print(e)

