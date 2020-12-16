from bson.objectid import ObjectId
from random import randrange, choice
import string


class GenSpec:
    def generate(self):
        pass

    def eq(self):
        return {'$eq': self.generate()}

    def gte_lt(self):
        bounds = sorted([self.generate(), self.generate()])
        return {'$gte': bounds[0], '$lt': bounds[1]}


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


class StringGenSpec(GenSpec):
    def __init__(self, alphabet=None, length=4):
        self.alphabet = alphabet or string.ascii_letters
        self.length = length

    def printable(self):
        self.alphabet = string.ascii_letters
        
        return self

    def upper(self):
        self.alphabet = string.ascii_uppercase
        
        return self
    
    def generate(self):
        return ''.join(choice(self.alphabet) for i in range(self.length))
