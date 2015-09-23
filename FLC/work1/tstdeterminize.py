# caian 22/09/2015

"""
These are the tests of automata class.
"""

from automata import Automata
import copy

# Q - States
states = ['p','q','r']
# E - Alphabet
alphabet = ['a','b','c','e']
# d - Transitions
transitions = {
    'p' : {
        'a' : [],
        'b' : ['q'],
        'c' : ['r'],
        'e' : ['p', 'r']},
    'q' : {
        'a' : ['p'],
        'b' : ['r'],
        'c' : ['p', 'q'],
        'e' : []},
    'r' : {
        'a' : [],
        'b' : [],
        'c' : [],
        'e' : []}
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
print_tst(states,alphabet,transitions,start,accept)
print_fsm(fsm)

print("Is deterministic?",fsm.isdeterministic())
print("Now we know that automata is not deterministic, we need detereminize it!")

print_fsm(fsm.determinize())
