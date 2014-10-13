# -*- coding: utf-8 -*-
"""file manipulations"""

import sys
import os.path as osp


def optional_output_path(func):
    """applying this decorator turns function arguments

      (input_stream, output_stream)

    into

      (input_path, output_path=None)
    """
    def wrapper(input_path, output_path=None):
        input_stream = open(input_path)
        if output_path is None:
            output_stream = sys.stdout
        else:
            output_stream = open(output_path, 'w')
        func(input_stream, output_stream)
        input_stream.close()
        if output_path is not None:
            output_stream.close()
    wrapper.__name__ = func.__name__
    return wrapper


@optional_output_path
def invert_file_1(input_stream, output_stream):
    lines = []
    for line in input_stream:
        lines.append(line)
    for line in reversed(lines):
        output_stream.write(line)


@optional_output_path
def invert_file_2(input_stream, output_stream):
    lines = reversed([line for line in input_stream])
    output_stream.write(''.join(lines))


@optional_output_path
def invert_file_3(input_stream, output_stream):
    output_stream.write(''.join(reversed(list(input_stream))))


if __name__ == '__main__':
    for func in (invert_file_1, invert_file_2, invert_file_3):
        print '*'*40, func.__name__
        func(osp.join(osp.dirname(__file__), 'input', 'testconf.ini'))
