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
        else:
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
                self.accept = [accept]

        self.actual_state = self.start

    def showstates(self):
        """
        Return a set of all valid states.
        """
        return list(self.states)

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

    def addaccept(self, accept):
        """
        Adds a accept state.
        """
        if not accept in self.states:
            self.states.append(accept)
        if not accept in self.accept:
            self.accept.append(accept)

    def rmstate(self, state):
        """
        Remove a specific state including transitions.
        """
        if state in self.states:
            self.states.remove(state)
        if state == self.start:
            self.start = None
        if state in self.accept:
            self.accept.remove(state)
        for s in self.states:
            self.rmtransition([s, state])
        del self.transitions[state]

    def addletter(self, letter):
        """
        Adds a letter to the alphabet.
        """
        if not letter in self.alphabet:
            self.alphabet.append(letter)
        for state in self.transitions.keys():
            if not letter in self.transitions[state].keys():
                self.transitions[state][letter] = None

    def rmletter(self, letter):
        """
        Remove a letter from the alphabet.
        """
        if letter in self.alphabet:
            self.alphabet.remove(letter)
        for state in self.transitions.keys():
            while letter in self.transitions[state].keys():
                del self.transitions[state][letter]

    def addtransition(self, transition):
        """
        Adds a transition. The transition must be in the form:
        transition = { 'qX' : ['z', 'qY'] }
        """
        for state in transition:
            if not state in self.states:
                self.states.addstate(state)
            if self.transitions[state] == None:
                self.transitions[state] = {
                    transition[state][0] : transition[state][1]
                }
            else:
                self.transitions[state][0] = transition[state][1]

    def rmtransition(self, transition):
        """
        Remove a transition. The transition must be in the form:
        transition = ['qX', 'qY']
        You cannot remove a state transition without removing the state.
        Here you can only set the transition to None.
        """
        letter = ''
        for key in self.transitions[transition[0]].keys():
            if self.transitions[transition[0]][key] == transition[1]:
                letter = key
                self.transitions[transition[0]][letter] = None

    def walk(self, letter):
        """
        You can walk one step by one on transitions.
        The return will be the actual state. If hit an problem: None.
        """
        if not letter in self.alphabet:
            return None
        self.actual_state = self.transitions[self.actual_state][letter]
        return self.actual_state

    def detect(self, word):
        """
        Detect if it is a valid word.
        """
        for letter in word:
            end_state = self.walk(letter)
            if end_state == None:
                break
        if end_state in self.accept:
            return True
        return False
