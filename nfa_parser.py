# nfa_parser.py

from nfa import NFA

def load_nfa_from_file(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    states = set()
    language = set()
    transitions = {}
    start_state = ''
    accept_states = set()
    reading_transitions = False

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

    '''
    print("DEBUG - Parsed NFA:")
    print("States:", states)
    print("Alphabet:", language)
    print("Start state:", start_state)
    print("Accept states:", accept_states)
    print("Transitions:", transitions)
    '''


    return NFA(states, language, transitions, start_state, accept_states)
