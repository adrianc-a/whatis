#!/usr/bin/env python3

from sys import argv
from urllib.error import HTTPError
import urllib.request
import urllib.error
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
    cache = os.getenv('HOME') + '/.whatis/wiki/' + what
    if os.path.exists(cache):
        f = open(cache, 'r', encoding='utf-8')
        definition = f.read()
        f.close()
        return definition
    try:
        resp = urllib.request.urlopen('http://en.wikipedia.org/wiki/' + what)
    except HTTPError:
        return 'The page: ' + 'http://en.wikipedia.org/wiki/' + what + \
               ' does not exist.'
    html = resp.read().decode('utf-8')

    index = html.find('<p>')
    if not index == -1:
        definition = remove_tags(html[index:html.find('</p>')])
        definition += '\nRead more at: http://en.wikipedia.org/wiki/' + what
        f = open(cache, 'w', encoding='utf-8')
        f.write(definition)
        f.close()
        return definition
    return urban(what)


def urban(word, user=0):
    cache = os.getenv('HOME') + '/.whatis/urban/' + word + '_' + str(user)
    if os.path.exists(cache):
        f = open(cache, 'r', encoding='utf-8')
        definition = f.read()
        f.close()
        return definition
    resp = urllib.request.urlopen(
        'http://api.urbandictionary.com/v0/define?term='
        + word)
    j = resp.read().decode('utf-8')
    definitions = json.loads(j)
    if definitions['result_type'] == 'no_results':
        return "There were no results found for " + word
    if user > len(definitions['list']):
        user = len(definitions['list']) - 1
    return_string = 'Definition:\n'
    return_string += definitions['list'][user]['definition']
    return_string += '\nExample:\n' + definitions['list'][user]['example']
    f = open(cache, 'w', encoding='utf-8')
    f.write(return_string)
    f.close()
    return return_string


def gen_args(arr, add_char='_'):
    args = ''
    for arg in arr:
        if arg == arr[0]:
            args += arg
        else:
            args += add_char + arg
    return args


def main():
    if not os.path.exists(os.getenv('HOME') + '/.whatis/wiki'):
        os.makedirs(os.getenv('HOME') + '/.whatis/wiki')
    if not os.path.exists(os.getenv('HOME') + '/.whatis/urban'):
        os.makedirs(os.getenv('HOME') + '/.whatis/urban')
    if argv[1] == '-u':
        if argv[2] == '-n':
            print(urban(gen_args(argv[4:], '+')))
        else:
            print(urban(gen_args(argv[2:], '+')))
    else:
        print(wiki(gen_args(argv[1:])))


if __name__ == '__main__':
    main()
