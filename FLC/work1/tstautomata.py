# caian 26/08/2015

"""
These are the tests of automata class.
"""

from automata import Automata

# Q - States
states = ['q0','q1','q2','q3']
# E - Alphabet
alphabet = ['a','b','c']
# d - Transitions
transitions = {
    'q0' : {
        'a' : 'q0',
        'b' : 'q1',
        'c' : 'q3'},
    'q1' : {
        'a' : 'q1',
        'b' : 'q2',
        'c' : 'q3'},
    'q2' : {
        'a' : 'q2',
        'b' : 'q3',
        'c' : 'q3'},
    'q3' : {
        'a' : 'q3',
        'b' : 'q3',
        'c' : 'q3'}
    }
# q0 - Start State
start = states[0]
# F - Accept States
accept = states[3]

print("Original states:")
print("\tstates:",states)
print("\talphabet:",alphabet)
print("\ttransitions:",transitions)
print("\tstart:", start)
print("\taccept:", accept)
        
fsm = Automata(states, alphabet, transitions, start, accept)

print("Automata states:")
print("\tstates:",fsm.states)
print("\talphabet:",fsm.alphabet)
print("\ttransitions:",fsm.transitions)
print("\tstart:",fsm.start)
print("\taccept:",fsm.accept)

fsm.rmstate('q3')
print("Automata states after remove q3:")
print("\tstates:",fsm.states)
print("\talphabet:",fsm.alphabet)
print("\ttransitions:",fsm.transitions)
print("\tstart:",fsm.start)
print("\taccept:",fsm.accept)
