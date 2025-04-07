from nfa import NFA
from convert import nfa_to_dfa

# Define NFA transitions
nfa_transitions = {
    ('q0', 'a'): ['q1', 'q2'],
    ('q1', 'b'): ['q2'],
    ('q2', 'a'): ['q2'],
    ('q2', 'b'): ['q2']
}

nfa = NFA(
    states={'q0', 'q1', 'q2'},
    alphabet={'a', 'b'},
    transitions=nfa_transitions,
    start_state='q0',
    accept_states={'q2'}
)

dfa = nfa_to_dfa(nfa)

# Print DFA results
print("DFA States:", dfa.states)
print("DFA Transitions:", dfa.transitions)
print("DFA Start State:", dfa.start_state)
print("DFA Accept States:", dfa.accept_states)
