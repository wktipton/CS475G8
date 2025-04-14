'''
This program defines a class for a Non-Deterministic Finite Automaton (NFA).
'''

class NFA:
    ##This function initializes the NFA
    def __init__(self, states, language, transitions, start_state, accept_states):
        self.states = states
        self.language = language
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states

    ##This function calculates the epsilon closure of a set of states
    def epsilon_closure(self, states):
        closure = set(states)
        stack = list(states)

        while stack:
            state = stack.pop()
            for next_state in self.transitions.get((state, ''), []):
                if next_state not in closure:
                    closure.add(next_state)
                    stack.append(next_state)
        return closure

    ##This function moves to the next states based on the input symbol, which is used to determine the reachable states
    def move(self, states, symbol):
        reachable_states = set()
        for state in states:
            for next_state in self.transitions.get((state, symbol), []):
                reachable_states.add(next_state)
        return reachable_states