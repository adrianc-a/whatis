#!/usr/bin/env python3
from sys import argv
import urllib.request
import json
import os

__author__ = 'Adrian Chmielewski-Anders'


def remove_tags(html):
    no_tags = ''
    intag = False
    for i in html:
        if i == '<':
            intag = True
        elif intag and i == '>':
            intag = False
        elif not intag:
            no_tags += i
    return no_tags


def wiki(what):
    cache = os.getenv('HOME') + '/whatis/wiki/' + what
    if os.path.exists(cache):
        f = open(cache, 'r')
        definition = f.read()
        f.close()
        return definition

    resp = urllib.request.urlopen('http://en.wikipedia.org/wiki/' + what)
    html = str(resp.read())

    index = html.find('<p>')
    if not index == -1:
        definition = remove_tags(html[index:html.find('</p>')])
        f = open(cache, 'w')
        f.write(definition)
        f.close()
        return definition
    return None


def urban(word):
    resp = urllib.request.urlopen('http://api.urbandictionary.com/v0/define?term=' + word)
    j = str(resp.read())[2:]
    json.loads(j)

    return None


def main():
    if not os.path.exists(os.getenv('HOME') + '/whatis/wiki'):
        os.makedirs(os.getenv('HOME') + '/whatis/wiki')

    if argv[1] == '-u':
        print(urban(argv[2]))
    else:
        args = ''
        for arg in argv[1:]:
            if arg == argv[1]:
                args += arg
            else:
                args += '_' + arg
        print(wiki(args))


if __name__ == '__main__':
    main()