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
A three-step algorithm is used to convert a provided NFA into a DFA. In the first step, the algorithm lists all possible subsets of the NFA and finds all of the possible transitions on each input symbol. When handling any $\epsilon$-transitions in the provided NFA, the algorithm uses the $\epsilon$-closure of the state as its transition. During this step, if the algorithm encounters a subset that includes a final state, it marks the subset as a final state for the DFA.

The second step of the algorithm handles the removal of unreachable states. It achieves this through the ***[insert file name]*** program, which ***[explain how file works]***. This ensures that only reachable states are used for the DFA.

The third and final step of the algorithm is to finally create the DFA using the gathered state information and transition table. ***[Talk more in-depth about the file(s) that handle this]***.

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

If the program runs successfully, it should output something similar to the following text, which is the resulting DFA:

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