#!/usr/bin/python3
def text_indentation(text):
    if type(text) != str:
        raise TypeError('text must be a string')

    for i in range(len(text)):
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print('\n')
        if text[i] == '.' and text[i+1] == ' ':
            continue
        if text[i] == ':' and text[i+1] == ' ':
            continue
        if text[i] == '?' and text[i+1] == ' ':
            continue
        print(text[i], end='')
