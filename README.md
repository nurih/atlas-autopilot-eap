# atlas-autopilot-eap

This repo has some code to help evaluate MongoDB's Atlas Autopilot feature.

The [`example.py`](example.py) file shows how to set up a query generator that will supply random match values to `find()`.

You can then run :

```shell
python example.py --url 'mongodb://.../' --db MyDbBName --collection MyCollectionName --iteration_count 1000
```

The code above will run 1000 iterations of `find()` each with a random value for the fields set up in the `example.py` file against the collection `MyCollectionName` in db `MyDbBNaame`.

