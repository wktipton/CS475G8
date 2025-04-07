class NFA:
    def __init__(self, states, language, transitions, start_state, accept_states):
        self.states = states
        self.language = language
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states

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

    def move(self, states, symbol):
        reachable_states = set()
        for state in states:
            for next_state in self.transitions.get((state, symbol), []):
                reachable_states.add(next_state)
        return reachable_states
