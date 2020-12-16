from  cli import generator, cli_args

from gen_spec import IntGenSpec, StringGenSpec, ObjectIdGenSpec

# Setup any fields you wish to target with queries
generator.with_field('items.qty', IntGenSpec(2, 24), method='eq')
generator.with_field('items.sku', StringGenSpec(alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', length=1).upper(), method='gte_lt')

# Run
try:
    doc_count = generator.run(cli_args.iteration_count)    
    
    print(f'{doc_count} documents found')
except Exception as e:
    print(e)

