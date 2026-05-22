"""
input_args.py — Parse input sentences in command line

"""

import argparse

def get_input_text():
    # Instantiates the ArgumentParser object
    parser = argparse.ArgumentParser(description='Provide sentence to translate')
    parser.add_argument("text", help="insert sentence here")
    args = parser.parse_args()
    return args.text