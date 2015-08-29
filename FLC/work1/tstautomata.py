# caian 26/08/2015

"""
These are the tests of automata class.
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
        
def simple_tst(states, alphabet, transitions, start, accept):
    print("Automata states:")
    print_fsm(fsm)

    fsm.rmstate('q3')
    print("Automata states after remove q3:")
    print_fsm(fsm)

    fsm.addletter('d')
    print("Automata states after add letter 'd':")
    print_fsm(fsm)

    fsm.rmletter('c')
    print("Automata states after remove letter 'c':")
    print_fsm(fsm)

def walk_tst(fsm, letter):
    print("Walk test: letter %s" % letter)
    print("\tactual_state:",fsm.actual_state)
    fsm.walk(letter)
    print("\tactual_state:",fsm.actual_state)

def detect_tst(fsm, word):
    print("Detect test: word %s" % word)
    print("\tactual_state:",fsm.actual_state)
    print("\tdetected? ",fsm.detect(word))
    print("\tactual_state:",fsm.actual_state)

"""
Tests:
"""
fsm = Automata(states, alphabet, transitions, start, accept)
fsm1 = copy.deepcopy(fsm)
print("Original states:")
print_tst(states,alphabet,transitions,start,accept)
#simple_tst(states, alphabet, transitions, start, accept)

print("Automata to next tests: ")
#fsm1.addtransition({'q0' : ['b', 'q3']})
print_fsm(fsm1)
letter = 'b'
walk_tst(fsm1, letter)
word = 'aababcc'
fsm1.actual_state = fsm1.states[0]
detect_tst(fsm1, word)
print("Now we know that automata is not deterministic, we need detereminize it!")
fsm2 = fsm.determinize()
print("Non-deterministic automata:")
print_fsm(fsm)
print("Deterministic one equivalent:")
print_fsm(fsm2)
