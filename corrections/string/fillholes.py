"""fill holes in a text"""

import os.path
from string import punctuation

TEXT_WITH_HOLES = os.path.join(os.path.dirname(__file__), 'input', 'text_with_holes.txt')
HOLE_VALUES = os.path.join(os.path.dirname(__file__), 'input', 'hole_values.txt')

PUNC = list(punctuation)
PUNC.remove('<')
PUNC.remove('>')

def make_values_dict(substitution_file):
    """return a dictionary of substitutions defined in the given file"""
    values = {}
    stream = open(substitution_file)
    for line in stream:
        line = line.strip()
        if line:
            hole_id, val = line.split('=')
            values[hole_id] = val
    stream.close()
    return values

def strip_punctuation(word):
    """remove punctation from the word"""
    letter_list = list(enumerate(word))
    for start_index, letter in letter_list:
        if letter not in PUNC:
            break
    letter_list.reverse()
    for end_index, letter in letter_list:
        if word[end_index] not in PUNC:
            break
    return word[start_index:end_index+1]

def fill_file(input_file, substitution_file, output_file):
    values = make_values_dict(substitution_file)
    input_file = open(input_file)
    result = []
    for line in input_file:
        words = [strip_punctuation(word) for word in line.split()]
        result_line = []
        for word in words:
            if word[0] == '<' and word[-1] == '>':
                # this is an identifier, replace it by the associated value
                result_line.append(values[word[1:-1]])
            else:
                result_line.append(word)
        result.append(' '.join(result_line))
    input_file.close()

    output_file = open(output_file, 'w')
    output_file.write('\n'.join(result))
    output_file.close()


if __name__ == '__main__':
    fill_file(TEXT_WITH_HOLES, HOLE_VALUES, 'filled_file.txt')
