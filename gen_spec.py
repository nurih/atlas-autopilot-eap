import random
from datetime import *
from bson.objectid import ObjectId
from random import randrange, choice
import string
from datetime import datetime, timedelta


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
        self.alphabet = string.printable
        
        return self

    def upper(self):
        self.alphabet = string.ascii_uppercase
        
        return self
    
    def generate(self):
        return ''.join(choice(self.alphabet) for i in range(self.length))

class DateGenSpec(GenSpec):
    def __init__(self, start = datetime.now(), day_range = 365):
        self.start = start
        self.day_range = day_range
        self.end = self.start + timedelta(days= self.day_range)

    def generate(self):
        return self.start + (self.end - self.start) * random.random()
        
