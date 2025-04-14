'''
This program defines a class for a Deterministic Finite Automaton (DFA).
'''

class DFA:
    def __init__(self, states, language, transitions, start_state, accept_states):
        self.states = states
        self.language = language
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states
