#!/usr/bin/env python3

import sys


def printg(iterable, columns=None, padding=None, ostream=sys.stdout):
    '''printg(iterable, columns=None, padding=None, ostream=sys.stdout)
    Prints an iterable in a grid format.
    Optional arguments:
    columns: the number of columns per line
    padding: the amount of padding for each item printed.
    ostream: a stream to write to; stdout by default
    If padding is not specified, items' __str__ or __repr__ members are used to
    get appropriate padding.
    If columns is not speficied, the maximum number of columns will be used
    while keeping each line under 80 characters.
    '''

    # get appropriate padding, if none is given
    if padding == None:
        iterable = list(iterable)
        padding = 0

        for item in iterable:
            # base padding off of each items str() length (or repr())
            try:
                width = len(str(item))
            except:
                width = 0

            if width > padding:
                padding = width

        # add a space on each side of each item
        padding += 2

    # get appropriate number of columns, if not specified
    if columns == None:
        # keep each line under 80 characters by default
        columns = 80 // padding

    # write to ostream
    index = 1
    for index, item in enumerate(iterable):
        ostream.write('{0:>{1}}'.format(item, padding))
        # move to new line when needed
        if (index + 1) % columns == 0:
            ostream.write('\n')
    # ensure the last line ends with a newline
    if (index + 1) % columns != 0:
        ostream.write('\n')
