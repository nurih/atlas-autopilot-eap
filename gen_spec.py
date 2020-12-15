from bson.objectid import ObjectId
from random import randrange

class GenSpec:
    def generate(self):
        pass

    def eq(self):
        return {'$eq': self.generate()}


class ObjectIdGenSpec(GenSpec):
    def generate(self):
        return ObjectId()


class IntGenSpec(GenSpec):
    def __init__(self, min, max):
        self.min = min
        self.max = max

        if(min >= max):
            raise ValueError(f'{min} must be less than {max}')

    def generate(self):
        return randrange(self.min, self.max, 1)
