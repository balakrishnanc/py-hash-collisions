#!/usr/bin/env python3
# -*- mode: python; coding: utf-8; fill-column: 80; -*-
"""Simple example to show that the hashing function used in Python may offer
quite poor performance.
#
# https://github.com/python/cpython/blob/main/Objects/dictobject.c#L141
# https://colab.research.google.com/drive/1scFw_OtQICixwuW3it41N4FKGXr5nN5F?usp=sharing#scrollTo=dUt3EhMcOp3M
"""

import argparse
import io
import random
import time


def time_it(func):
    def wrapper(*args):
        beg = time.time()
        func(*args)
        end = time.time()
        return end - beg
    return wrapper


def indices(num_keys, sz):
    ind = 0
    for i in range(num_keys):
        yield ind + sz
        ind = (ind * 5 + 1) % sz

@time_it
def fill_dict(d, num_keys, table_sz):
    for i in indices(num_keys, table_sz):
        d[i] = 0

@time_it
def access_dict(d, i, n):
    for _ in range(n):
        d[i] = 0


def main(args):
    with io.open(args.out_file, 'w', encoding='utf-8') as out:
        bad_dict = {}
        fill_dict(bad_dict, args.num_keys, args.table_sz)

        # # Accessing 0 is now very slow: linear time in database size.
        # access_dict(bad_dict, 0)

        # # Accessing 3 is constant time.
        # access_dict(bad_dict, 3)

        rnd_indices = list(range(args.num_keys))
        random.shuffle(rnd_indices)
        rnd_indices = sorted(rnd_indices[:1000])
        for i in rnd_indices:
            t = access_dict(bad_dict, i, args.num_trials)
            out.write(f"{i} {t:.6f}\n")
            out.flush()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Demonstrate hash collisions in Python's dictionary")
    parser.add_argument('-k', '--keys', dest='num_keys',
                        metavar='num-keys',
                        type=int,
                        default=2**16,
                        help=('Number of keys to enter into the dictionary'))
    parser.add_argument('-s', '--size', dest='table_sz',
                        metavar='table-size',
                        type=int,
                        default=2**17,
                        help=('Size of hash table'))
    parser.add_argument('-n', '--trials', dest='num_trials',
                        metavar='num-trials',
                        type=int,
                        default=2**14,
                        help=('Number of trials for amplifying measurements'))
    parser.add_argument('-o', '--out', dest='out_file',
                        metavar='output',
                        default='data.txt',
                        type=str,
                        help=('Output file path'))
    main(parser.parse_args())
