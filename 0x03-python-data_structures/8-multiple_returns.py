#!/usr/bin/python3
def multiple_returns(sentence):
    s = len(sentence)
    if s == 0:
        return s, None
    new_tuple = (s, sentence[0])
    return new_tuple
