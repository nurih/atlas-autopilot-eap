import argparse
import load_generator
from load_generator import *

parser = argparse.ArgumentParser(
    description='Run queries against a mongo cluster')
parser.add_argument('--url', '--connection', required=True, type=str,
                    help='Mongo connection string')
parser.add_argument('--db', required=True, type=str, help='Database name')
parser.add_argument('--collection', required=True,
                    type=str, help='Collection name')

parser.add_argument('--iteration_count',  type=int,
                    help='Collection name', default=100)

cli_args = parser.parse_args()

generator = LoadGenerator().with_url(cli_args.url).with_db(
    cli_args.db).with_collection(cli_args.collection)

