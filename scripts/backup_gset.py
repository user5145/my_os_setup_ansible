#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://gist.github.com/elleryq/95415d24ceaac43c6acd
"""dump gsettings"""
from __future__ import print_function
from subprocess import check_output


def get_schemas():
    output = check_output(['gsettings', 'list-schemas'])
    schemas = output.split('\n')
    return schemas


def get_keys(schema):
    output = check_output(['gsettings', 'list-keys', schema])
    keys = output.split('\n')
    return keys


def get(schema, key):
    output = check_output(['gsettings', 'get', schema, key])
    return output.strip()


def main():
    for schema in get_schemas():
        if not schema:
            continue
        for key in get_keys(schema):
            if not key:
                continue
            print("{0} {1} {2}".format(schema, key, get(schema, key)))

if __name__ == "__main__":
    main()
