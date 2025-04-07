import argparse
from convert import nfa_to_dfa
from nfa_parser import load_nfa_from_file
from dfa_graph import print_dfa_readable, draw_dfa

parser = argparse.ArgumentParser(description="Convert NFA to DFA")
parser.add_argument("input_file", help="Input NFA file")
parser.add_argument("--graph", action="store_true", help="Generate and open DFA graph PDF")
args = parser.parse_args()

nfa = load_nfa_from_file(args.input_file)
dfa = nfa_to_dfa(nfa)

print("DFA States:", dfa.states)
print("DFA Transitions:", dfa.transitions)
print("DFA Start State:", dfa.start_state)
print("DFA Accept States:", dfa.accept_states)

print_dfa_readable(dfa)

if args.graph:
    draw_dfa(dfa, filename="dfa_output")
