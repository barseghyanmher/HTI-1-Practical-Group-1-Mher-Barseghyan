import os
import random

ZEN_FILE = 'words.txt'


def get_a_word():
    file_path = os.path.abspath(__file__)  # current python file path
    directory = os.path.dirname(file_path)
    zen_file_path = os.path.join(directory, ZEN_FILE)

    with open(zen_file_path) as f:
        return random.choice(f.readlines()).rstrip()
