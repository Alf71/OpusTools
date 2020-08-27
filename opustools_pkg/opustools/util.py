"""Utility functions"""

import bz2
import gzip


def file_open(filename, mode='r', encoding='utf8'):
    """Open file with implicit gzip/bz2 support

    Uses text mode by default regardless of the compression.

    """
    if filename.endswith('.bz2'):
        if mode in {'r', 'w', 'x', 'a'}:
            mode += 't'
        return bz2.open(filename, mode=mode, encoding=encoding)
    if filename.endswith('.gz'):
        if mode in {'r', 'w', 'x', 'a'}:
            mode += 't'
        return gzip.open(filename, mode=mode, encoding=encoding)
    return open(filename, mode=mode, encoding=encoding)

def format_sentences(sentences, ids, wmode, direction):
    result = ''
    if wmode == 'normal':
        if len(sentences) == 0:
            result = '\n'
        if direction == 'src':
            result += '================================'
        for i, sentence in enumerate(sentences):
            result += ('\n('+direction+')="'+ids[i]+'">'+sentence)
        if direction == 'trg':
            result += '\n================================\n'
    return result
