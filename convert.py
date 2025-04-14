'''
 This program converts the provided NFA into the resulting DFA.
'''

# Import the NFA and DFA classes
from nfa import NFA
from dfa import DFA

def nfa_to_dfa(nfa):

    # Initialize the DFA components
    dfa_states = []
    dfa_transitions = {}
    dfa_start_state = tuple(sorted(nfa.epsilon_closure({nfa.start_state})))
    dfa_accept_states = []
    unmarked_states = [dfa_start_state]
    dfa_states.append(dfa_start_state)

    # Iterate until all states are processed
    while unmarked_states:

        # Get the current state to process
        current_state = unmarked_states.pop(0)

        # Check if the current state is an accepting state and add to the DFA accepting states list
        if any(s in nfa.accept_states for s in current_state):
            dfa_accept_states.append(current_state)

        # Process each input symbol in the NFA's language
        for symbol in nfa.language:

            # Get the next state set after moving from the current state
            next_state_set = nfa.epsilon_closure(nfa.move(current_state, symbol))
            next_state = tuple(sorted(next_state_set))

            # Add the transition to the DFA
            if next_state:
                dfa_transitions[(current_state, symbol)] = next_state

                # Check if the next state is already in the DFA state
                if next_state not in dfa_states:
                    dfa_states.append(next_state)
                    unmarked_states.append(next_state)

            # If there is no valid transition, create a dead state
            else:
                dead_state = ('trap',)
                dfa_transitions[(current_state, symbol)] = dead_state
                if dead_state not in dfa_states:
                    dfa_states.append(dead_state)
                    for sym in nfa.language:
                        dfa_transitions[(dead_state, sym)] = dead_state

    # Create the DFA object and return it
    return DFA(dfa_states, nfa.language, dfa_transitions, dfa_start_state, dfa_accept_states)
