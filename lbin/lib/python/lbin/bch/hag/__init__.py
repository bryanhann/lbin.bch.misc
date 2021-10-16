#!/usr/bin/env python3

def gather(path):
    bch=path/'.bch'
    if (path/'.bch').exists():
        yield path
        for child in path.glob('*'):
            yield from gather(child)


