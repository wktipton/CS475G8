from nfa import NFA
from dfa import DFA

def nfa_to_dfa(nfa):
    dfa_states = []
    dfa_transitions = {}
    dfa_start_state = tuple(sorted(nfa.epsilon_closure({nfa.start_state})))
    # print("Start ε-closure:", dfa_start_state)
    dfa_accept_states = []
    unmarked_states = [dfa_start_state]
    dfa_states.append(dfa_start_state)

    while unmarked_states:
        current_state = unmarked_states.pop(0)

        if any(s in nfa.accept_states for s in current_state):
            dfa_accept_states.append(current_state)

        for symbol in nfa.alphabet:
            next_state_set = nfa.epsilon_closure(nfa.move(current_state, symbol))
            next_state = tuple(sorted(next_state_set))

            if next_state:
                dfa_transitions[(current_state, symbol)] = next_state
                if next_state not in dfa_states:
                    dfa_states.append(next_state)
                    unmarked_states.append(next_state)
            else:
                # Add transition to dead state
                dead_state = ('trap',)
                dfa_transitions[(current_state, symbol)] = dead_state
                if dead_state not in dfa_states:
                    dfa_states.append(dead_state)
                    for sym in nfa.alphabet:
                        dfa_transitions[(dead_state, sym)] = dead_state


    return DFA(dfa_states, nfa.alphabet, dfa_transitions, dfa_start_state, dfa_accept_states)
