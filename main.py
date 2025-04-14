'''
This is the main program that converts an NFA to a DFA and prints the DFA in a readable format.
'''

# Call the necessary modules and libraries
import argparse
from convert import nfa_to_dfa
from nfa_parser import load_nfa_from_file
from dfa_graph import print_dfa_readable

# Set up command line argument parsing
parser = argparse.ArgumentParser(description="Convert NFA to DFA")
parser.add_argument("input_file", help="Input NFA file")
parser.add_argument("--graph", action="store_true", help="Generate and open DFA graph PDF")
args = parser.parse_args()

# Load the NFA from the provided file and convert it to DFA
nfa = load_nfa_from_file(args.input_file)
dfa = nfa_to_dfa(nfa)

# Print the DFA in a readable format
print_dfa_readable(dfa)