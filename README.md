# atlas-autopilot-eap

This repo has some code to help evaluate MongoDB's Atlas Autopilot feature.

[`example-1.py`](example-1.py) shows how to set up a query generator that will supply random match values to `find()`.

You can then run :

```shell
python example-1.py --url 'mongodb://.../' --db MyDbBName --collection MyCollectionName --iteration_count 1000
```

The code above will run 1000 iterations of `find()` each with a random value for the fields set up in the `example.py` file against the collection `MyCollectionName` in db `MyDbBName`.


The file [`invoice.template.json`](invoice.template.json) can be used with [`mgeneratejs`](https://github.com/rueckstiess/mgeneratejs) to create sample data.

```shell
mgeneratejs -n 1000000 .\invoice.template.json | mongoimport 'mongodb+srv://USR:PWD@cluster0.wpcge.mongodb.net/?retryWrites=true&w=1' --collection invoice --db commerce
```
