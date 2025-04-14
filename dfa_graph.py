'''
This program prints the resulting DFA in a readable format
'''

# Maps the DFA tuple states to simple names like S0, S1, ...
def rename_states(dfa):
    mapping = {state: f"S{i}" for i, state in enumerate(dfa.states)}
    return mapping

def print_dfa_readable(dfa):
    # Rename DFA tuple states to simple names
    state_names = rename_states(dfa)

    # Print the state information
    print("States:")
    for state in dfa.states:
        print(f"  {state_names[state]} = {state}")

    # Print the start state
    print("\nStart State:")
    print(f"  {state_names[dfa.start_state]}")

    # Print the accepting states
    print("\nAccept States:")
    for state in dfa.accept_states:
        print(f"  {state_names[state]}")

    # Print the transitions
    print("\nTransitions:")
    for (src, symbol), dst in dfa.transitions.items():
        print(f"  {state_names[src]} -- {symbol} --> {state_names[dst]}")
    print()