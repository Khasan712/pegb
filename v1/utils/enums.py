from enum import Enum


class OrderStatus(Enum):
    new = 'new'
    proccess = 'proccess'
    done = 'done'
    rejected = 'rejected'

    @classmethod
    def choices(cls):
        return [
            (key.value, key.name)
            for key in cls
        ]


class CustomerCategory(Enum):
    bronze = 'bronze'
    silver = 'silver'
    gold = 'gold'


    @classmethod
    def choices(cls):
        return [
            (key.value, key.name)
            for key in cls
        ]