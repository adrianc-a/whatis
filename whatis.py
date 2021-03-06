#!/usr/bin/env python

from sys import argv
import urllib2
from urllib2 import URLError
import json
import os

__author__ = 'Adrian Chmielewski-Anders'


def get(url):
    return urllib2.urlopen(url).read().decode('utf-8')


def cache_def(where, what):
    f = open(where, 'w')
    f.write(what.encode('utf-8'))
    f.close()


def read_cache(location):
    f = open(location, 'r')
    definition = f.read().decode(encoding='utf-8')
    f.close()
    return definition


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


def did_you_mean(html):
    index = html.find('<ul>')
    if not index == -1:
        return 'Did you mean: \n' + remove_tags(
            html[index: html.find('</ul>')]) + '\n?'


def wiki(what):
    cache = os.getenv('HOME') + '/.whatis/wiki/' + what
    if os.path.exists(cache):
        return read_cache(cache)
    try:
        html = get('http://en.wikipedia.org/wiki/' + what)
    except URLError:
        return urban(what)
    index = html.find('<p>')

    if not index == -1:
        definition = remove_tags(html[index:html.find('</p>')])
        if definition[len(what):] == ' may refer to:':
            return did_you_mean(html)
        cache_def(cache, definition)
        return definition + '\nRead more at: http://en.wikipedia.org/' \
                                   'wiki/' + what
    return urban(what)


def urban(word, user=0):
    user = int(user)
    cache = os.getenv('HOME') + '/.whatis/urban/' + word + '_' + str(user)
    if os.path.exists(cache):
        return read_cache(cache)
    try:
        j = get(
            'http://api.urbandictionary.com/v0/define?term='
            + word)
    except URLError:
        return 'Error, invalid URL'
    definitions = json.loads(j)
    if definitions['result_type'] == 'no_results':
        return "There were no results found for " + word
    if user >= len(definitions['list']):
        user = len(definitions['list']) - 1
    return_string = 'Definition:\n'
    return_string += definitions['list'][user]['definition']
    return_string += '\nExample:\n' + definitions['list'][user]['example']
    cache_def(cache, return_string)
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
            print urban(gen_args(argv[4:], '+'), argv[3])
        else:
            print urban(gen_args(argv[2:], '+'))
    else:
        print wiki(gen_args(argv[1:]))


if __name__ == '__main__':
    main()
