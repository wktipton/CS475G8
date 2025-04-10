def rename_states(dfa):
    """Maps DFA tuple states to simple names like S0, S1, ..."""
    mapping = {state: f"S{i}" for i, state in enumerate(dfa.states)}
    return mapping

def print_dfa_readable(dfa):
    state_names = rename_states(dfa)

    # print("\nPretty DFA Output:")
    print("States:")
    for state in dfa.states:
        print(f"  {state_names[state]} = {state}")

    print("\nStart State:")
    print(f"  {state_names[dfa.start_state]}")

    print("\nAccept States:")
    for state in dfa.accept_states:
        print(f"  {state_names[state]}")

    print("\nTransitions:")
    for (src, symbol), dst in dfa.transitions.items():
        print(f"  {state_names[src]} -- {symbol} --> {state_names[dst]}")
    print()

def draw_dfa(dfa, filename='dfa_output'):
    from graphviz import Digraph
    dot = Digraph(comment='DFA')
    state_names = rename_states(dfa)

    for state in dfa.states:
        shape = 'doublecircle' if state in dfa.accept_states else 'circle'
        dot.node(state_names[state], shape=shape)

    # Start arrow
    dot.node('', '', shape='none')
    dot.edge('', state_names[dfa.start_state])

    for (src, symbol), dst in dfa.transitions.items():
        dot.edge(state_names[src], state_names[dst], label=symbol)

    dot.render(filename, view=True, format='pdf')
