'''
This program parses through the provided NFA file and creates an NFA object from the provided data.
'''
from nfa import NFA

def load_nfa_from_file(filename):

    # Open the provided NFA file and read its contents line by line
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    # Initialize variables to store NFA components
    states = set()
    language = set()
    transitions = {}
    start_state = ''
    accept_states = set()
    reading_transitions = False

    # Parse through the lines to extract NFA components
    for line in lines:
        if line.startswith('states:'):
            states = set(s.strip() for s in line.replace('states:', '').split(','))
        elif line.startswith('language:'):
            language = set(s.strip() for s in line.replace('language:', '').split(','))
        elif line.startswith('start_state:'):
            start_state = line.replace('start_state:', '').strip()
        elif line.startswith('accept_states:'):
            accept_states = set(s.strip() for s in line.replace('accept_states:', '').split(','))
        elif line.startswith('transitions:'):
            reading_transitions = True
        elif reading_transitions:
            from_state, symbol, to_state = line.split(',')
            key = (from_state.strip(), symbol.strip())
            if key not in transitions:
                transitions[key] = []
            transitions[key].append(to_state.strip())

    # Return the constructed NFA object
    return NFA(states, language, transitions, start_state, accept_states)
