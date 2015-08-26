# caian 26/08/2015

class Automata(object):
"""
Automata definition: M is a 5-tuple (Q,E,d,q0,F) where
    Q   - finite set of states
    E   - finite set of simbols called the alphabet
    d   - a transition function (d : Q x E -> Q)
    q0  - a start state (q0 is in Q)
    F   - a set of accept states (F have some states from Q)
In my implementation, i'll assume that the form of data comes are in the following form:
    M(object) = {
        states = ['q0','q1']            # or eventually ['q0', 'q1']
        alphabet = ['a','b','0','1']    # the empty transition is 'e'
        transitions = {}                # described below
        start = 'q0'                    # start state
        accept = ['q1']                 # always a list
    }

transition is defined by the following form:
    transitions = {
        'q0' : {
            'a' : 'q1',
            'b' : 'q0',
            'e' : None,     # None is a dead state
            '1' : 'q1',
            '2' : None},
        'q1' : {
            'a' : 'q1',
            'b' : 'q0',
            'e' : None,
            '1' : 'q1',
            '2' : None}
    }

So, thats the form I'll be doing this.    
"""
    def __init__(self, states=None, alphabet=None, transitions=None, start=None, accept=None):
        """
        Automata() -> empty automata
        The Automata must be described like the up description
        """
        if states is None:
            self.states = []
            self.alphabet = []
            self.transitions = {}
            self.start = None
            self.accept = []
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        if not start in states:
            self.start = None
        else:
            self.start = start
        if not accept in states:
            self.accept = []
        else:
            self.accept = accept

        self.actual_state = self.start

    def addstate(self, state):
        """
        Adds a state to the automata states.
        """
        self.states.append(state)

    def addstart(self, state):
        """
        Adds a start state.
        """
        if state in self.states:
            self.start = state
        else:
            self.addstate(state)
            self.addstart(state)

    def rmstate(self, state):
        """
        Remove a specific state,
        """
        if state in self.states:
            self.states.remove(state)
        if state == self.start:
            self.start = None

    def addletter(self, letter):
        """
        Adds a letter to the alphabet.
        """
        if not letter in self.alphabet:
            self.alphabet.append(letter)

    def rmletter(self, letter):
        """
        Remove a letter from the alphabet.
        """
        if letter in self.alphabet:
            self.alphabet.remove(letter)

    def addtransition(self, transition):
        """
        Adds a transition. The transition must be in the form:
        transition = { 'qX' : ['z', 'qY'] }
        """
        for key in transition:
            if not key in self.states:
                self.states.addstate(key)
            if transitions[key] == None:
                self.transitions[key] = {
                    transition[key][0] : transition[key][1]
                }
            else:
                self.transitions[key][0] = transition[key][1]

    def rmtransition(self, transition):
        """
        Remove a transition. The transition mus be in the form:
        transition = { 'qX' : 'z'}
        You cannot remove a state transition without removing the state.
        Here you can only set the transition to None.
        """
        for key in transition:
            if transitions[key] == None:
                self.transitions[key] = {
                    transition[key] : None
                }
            else:
                self.transitions[key][transition[key]] = None

    def walk(self, letter):
        """
        You can walk one step by one. The return will be the actual state.
        """
        if not letter in self.alphabet:
            return None
        self.actual = transitions[self.actual][letter]
        return self.actual

    def detect(self, word):
        """
        Detect if it is a valid word.
        """
        for letter in word:
            end_state = walk(letter)
            if end_state == None:
                break
        if end_state in accept:
            return True
        return False
