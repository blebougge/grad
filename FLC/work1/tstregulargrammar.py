# caian 01/10/2015

"""
These are the tests of Regular Grammars.
"""

from automata import Automata
import copy

# Q - States
states = ['q0','q1','q2','q3']
# E - Alphabet
# alphabet = ['a','b','c']
alphabet = ['a','b']
# d - Transitions
transitions = {
    'q0' : {
        'a' : ['q0','q1'],
        'b' : ['q0']},
    'q1' : {
        'a' : ['q2'],
        'b' : ['q3']},
    'q2' : {
        'a' : ['q2'],
        'b' : ['q2']},
    'q3' : {
        'a' : ['q3'],
        'b' : ['q3']}
    }
# q0 - Start State
start = states[0]
# F - Accept States
accept = states[2]

def print_tst(states, alphabet, transitions, start, accept):
    print("\tstates:",states)
    print("\talphabet:",alphabet)
    print("\ttransitions:",transitions)
    print("\tstart:", start)
    print("\taccept:", accept)

def print_fsm(fsm):
    print_tst(fsm.states,fsm.alphabet,fsm.transitions,fsm.start,fsm.accept)
        
"""
Tests:
"""
fsm = Automata(states, alphabet, transitions, start, accept)
print("Original states:")
print_fsm(fsm)

print("Automata to next tests: ")

# test for RegGra
print("If we want a Regular Grammar equivalent of the automata, here it is:")
regular_grammar = fsm.toRegGra()
print("RegGra:", regular_grammar)
print("And to a FSM again!")
new_automata = fsm.fromRegGraToAutomata(regular_grammar, states[0])
print("Automata:")
print_fsm(new_automata)
