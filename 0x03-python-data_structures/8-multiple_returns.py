#!/usr/bin/python3
from 8-main import *


def multiple_returns(sentence):
    if sentence != '\0':
        new_tuple = (len(sentence), sentence[0])
        return (new_tuple)
    else:
        return (None)
