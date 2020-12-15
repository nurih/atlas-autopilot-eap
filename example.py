from  cli import generator, cli_args

from gen_spec import IntGenSpec

# Setup any fields you wish to target with queries
generator.with_field('score', IntGenSpec(0, 10))

# Run
doc_count = generator.run(cli_args.iteration_count)

print(f'{doc_count} found')
