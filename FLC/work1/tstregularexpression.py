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
print_fsm(fsm)

print("Is deterministic?",fsm.isdeterministic())
print("Now we know that automata is not deterministic, we need detereminize it!")

fsmD = fsm.determinize()

print("Here is the determinized automata:")
print_fsm(fsmD)

print("If we want a Regular Expression of the automata, here it is:")
regular_expression = fsmD.toRegEx()
print("RegEx:", regular_expression)

# test to RegGra
print("Regular Grammar test:")
regular_grammar = fsmD.toRegGra()
print("toRegGra:", regular_grammar)
print("And to a FSM again!")
new_automata = fsmD.fromRegGraToAutomata(regular_grammar, states[0])
print("Automata:")
print_fsm(new_automata)
