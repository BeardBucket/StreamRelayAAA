import os
from .words import ALL,NAMES,WORDS

def generate_name_f(num: int = 4) -> str:
    """ Generate a random set of words with a count of `count` words"""
    total = len(ALL)
    words = []
    for i in range(num):
        iv=int.from_bytes(os.urandom(16), byteorder="big")
        word=ALL[iv%total]
        words.append(word.capitalize())
    return "".join(words)
