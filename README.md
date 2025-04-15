# CS475-001 Group 8 Subset Construction Final Project
**Python Version:** 3.12.3

**Group Members:** </br>
Daniel Tsark - dhtsark@crimson.ua.edu </br>
Will Tipton - wktipton@crimson.ua.edu </br>
Noah Morgans - nmorgans@crimson.ua.edu </br>

## Project Description
The goal of this project is to implement a python program that takes an NFA as an input and outputs the equivalent DFA.

This process, called **Subset Construction**, is used to establish equivalency between NFAs and DFAs. This can also help us prove the regularity of languages and showcases the limits of finite automata.

Some real world applications of this process include:
- Formal Language Processing
- Hardware Modeling
- Compiler Design

## Implementation
A three-step algorithm is used to convert a provided NFA into a DFA. The program uses two classes-- one for NFAs (```nfa.py```), one for DFAs (```dfa.py```)-- along with a NFA-to-DFA converter program (```convert.py```) and a DFA print program (```dfa_graph.py```).

In the first step, the algorithm reads through the provided NFA and determines all possible subsets of the NFA. It also determines all of the possible transitions on each letter from the alphabet. When the program encounters an $\epsilon$-transition in the provided NFA, the program runs the $\epsilon$-closure function in ```nfa.py``` listed below:

``` python
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
```

Furthermore, if the algorithm encounters a subset that includes an accepting state from the provided NFA, it marks the subset as accepting for the DFA.

The second step of the algorithm handles the removal of unreachable states. It achieves this through the move function located in the ```nfa.py``` program, which can be seen below:

``` python
def move(self, states, symbol):
        reachable_states = set()
        for state in states:
            for next_state in self.transitions.get((state, symbol), []):
                reachable_states.add(next_state)
        return reachable_states
```

As we can see from the function above, the program uses a depth-first search to traverse through the NFA to ensure that the state is reachable. If we combine this function with the $\epsilon$-closure function, we can ensure that only reachable states are represented in the resulting DFA.

The third and final step of the algorithm creates the resulting DFA from the information gathered from the provided NFA and the program's calculations. A large majority of this NFA-to-DFA construction is completed in the ```convert.py``` file. The program reads through the NFA and builds the DFA based off of certain conditions, such as:

 - Whether or not the current state is an accepting state
 - What the current input letter is

In summary, the program reads in a provided NFA from the user, then handles and $\epsilon$-transitions and resulting unreachable states before finally converting the NFA into a DFA using a list of conditions.

For more information regarding our implementation subset construction, please review ```CS 475 - Subset Construction.pptx```.

## How To Use
This program contains a makefile for better user accessibility. Running the command ```make``` in the terminal will provide you with the necessary information to run the program.

All NFAs must be stored as .txt files with the following information:
- The names of the states
- The language accepted by the NFA
- The start state of the NFA
- The accepting states of the NFA
- The transition table of the NFA

An example input can be found below. Please note that multiple states should be separated by commas and a new transition is indicated by a newline. Any $\epsilon$-transitions should be indicated by a blank space.

```
states: q0,q1,q2,q3

language: 0,1

start_state: q0

accept_states: q3

transitions:
q0,0,q0
q0,1,q0
q0,,q1
q0,1,q2
q1,0,q3
q2,1,q3
```

Once you have created the input NFA, you can run the program using the command ```make <NFA_filename>.txt```. Ensure that this file is located within the ```tests``` folder. If you want to check if your NFA file is located in the ```tests``` folder, you can use the ```make list``` command to list all of the .txt files within ```tests```.

If the program runs successfully, it should list all of the states, the start state, the accepting state(s), and the transitions of the resulting DFA:

```
python3 main.py tests/<NFA_filename>.txt
States:
  S0 = ('q0', 'q1')
  S1 = ('q0', 'q1', 'q2')
  S2 = ('q0', 'q1', 'q3')
  S3 = ('q0', 'q1', 'q2', 'q3')

Start State:
  S0

Accept States:
  S2
  S3

Transitions:
  S0 -- 1 --> S1
  S0 -- 0 --> S2
  S1 -- 1 --> S3
  S1 -- 0 --> S2
  S2 -- 1 --> S1
  S2 -- 0 --> S2
  S3 -- 1 --> S3
  S3 -- 0 --> S2
```

## Results
Talk about the results here.

## Sources
Place any references here