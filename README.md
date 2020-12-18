# Mongo Workload Synth

Code and library to help generate varied query workload against a MongoDB cluster.


## Using

The library give you some blocks to build a `find()` command, supplying varying values to the comparison terms. The framework lets you run the query variety for a specified number of times.

To create an experiment, configure a `generator` with desired filters.

The `with_field` method accepts a field name (dot-notation or top level), a value generation specification, and a match operator.

The field value generator inherits `GenSpec` and produces varying values. Several built in ones are available to generate integer , string, objectid, and dates. More detail on those below.

The `method=` argument chooses the matching shape of the query. Default is `eq`, which generates a query such as `{my_field: {$eq: &lt;xyz&gt;} }`. Also supported is `gte_lt` which generates a range query of the form `{my_field: {$gte: &lt;value1&gt;, $lt: &lt;value2&gt;} }`.


```python
from  cli import generator, cli_args
from gen_spec import IntGenSpec, StringGenSpec, ObjectIdGenSpec, DateGenSpec

# Setup any fields you wish to target with queries
generator.with_field('customer._id', IntGenSpec(0, 1000000))
generator.with_field('shipTo.country', StringGenSpec().upper(), method='gte_lt')
generator.with_field('created', DateGenSpec(start = datetime.now(), day_range = 60), method='gte_lt')

generator.with_sort({'created': 1})

# Run
try:
    doc_count = generator.run(cli_args.iteration_count)    
    
    print(f'{doc_count} documents found')
except Exception as e:
    print(e)

```

### Value Generators
|Generator| Option| Description|
|---      |---    |---         |
|`IntGenSpec` |    |Generates integer field values |
|`IntGenSpec` | `min=`    | Lower range of number. Required |
|`IntGenSpec` | `max=`    | Upper range of number. Required |
|`StringGenSpec` |    |Generates random string field values |
|`StringGenSpec` | `alphabet=`    | String containing character set to use. Default `string.ascii_letters` from Python's _string_ l`ibrary |
|`StringGenSpec` |  `length=`  | String length. Defaults to 4 |
|`ObjectIdGenSpec` |    | Generates an ObjectId |
|`DateGenSpec` |    |Generates date field values |
|`DateGenSpec` | `start_date=`   | Lower range start date of the values. Default `datetime.now()` from Python's _datetime_ library |
|`DateGenSpec` | `day_range=`   | Number of days past `start_date` as upper range ov the values. Defaults to 365 |

In addition to the above parameters, each gen spec may support alternate methods to affect behavior. `StringGenSpec(...).upper()` for example sets the alphabet to ASCII uppercase letters via fluent method, and is equivalent to using the constructor parameter `alphabet= string.ascii_uppercase`.


### Load Generator

The load generator is configured via fluent methods:

| Method | Description |
|--- |--- |
| `with_url(mongo_url)`| Target cluster connection URL|
| `with_db(db_name)`| Target database name|
| `with_collection(db_name)`| Target collection name|
| `with_field(field_name=, gen_spec=, method=)`| Field match configuration. `field_name` is the target field (dot-notation ok). `gen-spec` is an instance of a value generator inheriting from `GenSpec`. `method` is one of `eq` or `gte_lt` and specifies the query operator|
| `with_sort(sort_spec)`| Optional sorting specification. `sort_spec` is a dict or SON compliant structure containing field(s) and sort direction(s)|


You can then run an experiment like so:

```shell
python example-1.py --url 'mongodb://.../' --db MyDbBName --collection MyCollectionName --iteration_count 1000
```

The code above will run 1000 iterations of `find()` each with a random value for the fields set up in the `example.py` file against the collection `MyCollectionName` in db `MyDbBName`.


## Generating Sample Data

If you don't have an existing collection with enough data, you can generate dummy data. 
The file [`invoice.template.json`](invoice.template.json) can be used with [`mgeneratejs`](https://github.com/rueckstiess/mgeneratejs) to create sample data.

```shell
mgeneratejs -n 1000000 .\invoice.template.json | mongoimport 'mongodb+srv://USR:PWD@mycluster.wpcge.mongodb.net/?retryWrites=true&w=1' --collection invoice --db commerce
```
The example code above will generate 1 million documents in the collection "invoice" in the database "commerce" at the target cluster specified above.
