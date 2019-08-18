#!/usr/bin/env python3

import argparse


def main():
    parser = argparse.ArgumentParser(prog='vup', description='Version updater')
    sub = parser.add_subparsers()

    gen = sub.add_parser('generate', help='generate version file')
    gen.add_argument('-x', choices=('c++', 'c'), help='output language (default: c++)', default='c++')
    gen.add_argument('--output', '-o', help='output file base name (default: vup)', default='vup')
    gen.add_argument('--header', '-e', help='header file extension (default: c++: hpp, c: h)', default=None)

    init = sub.add_parser('init', help='initialize configuration file')
    # init.add_argument('--interactive', '-i', action='store_true', help='run init as interactive mode')
    for p in ('major', 'minor', 'build', 'revision'):
        init.add_argument(
            '--{}-type'.format(p),
            choices=('auto', 'manual', 'year', 'month', 'day', 'days', 'none'),
            help='{} version style (auto: auto increment, '
                 'manual: increment by command execute, '
                 'days: number of days from specific date, '
                 'none: not use this field'.format(p),
            required=True)
        init.add_argument(
            '--{}'.format(p),
            help='initial value for {}'.format(p))
        init.add_argument(
            '--{}-from'.format(p),
            help='days: from date(YYYY-MM-DD)'
        )
