#!/usr/bin/env python3

def gather(path):
    bch=path/'.bch'
    if bch.exists():
        yield bch #path
        for child in path.glob('*'):
            yield from gather(child)


