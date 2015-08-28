# caian 26/08/2015

import copy

class Automata(object):
    """
    Automata definition: M is a 5-tuple (Q,E,d,q0,F) where
        Q   - finite set of states
        E   - finite set of simbols called the alphabet
        d   - a transition function (d : Q x E -> Q)
        q0  - a start state (q0 is in Q)
        F   - a set of accept states (F have some states from Q)
    In my implementation, I'll assume that the form of data comes are in the following form:
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
                'a' : ['q1'],
                'b' : ['q0','q1'],
                'e' : [],           # e = Empty transition
                '1' : ['q1'],
                '2' : []},          # [] = dead state
            'q1' : {
                'a' : ['q1'],
                'b' : ['q0','q1'],
                'e' : [],
                '1' : ['q1'],
                '2' : []}
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
        if not state in self.states:
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
            self.addstate(accept)
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
                self.transitions[state][letter] = []

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
        transition = { 'qX' : ['z', ['qY']] }
        """
        for state in transition:
            if not state in self.states:
                self.addstate(state)
            if not state in self.transitions:
                self.transitions[state] = {}
            for letter in self.alphabet:
                if not letter in self.transitions[state]:
                    self.transitions[state][letter] = []
            if len(transition[state][1]) != 0:
                print(transition[state][1][0], self.transitions[state][transition[state][0]])
                if not transition[state][1][0] in self.transitions[state][transition[state][0]]:
                    self.transitions[state][transition[state][0]].append(transition[state][1][0])
            else:
                self.transitions[state] = {
                    transition[state][0] : transition[state][1]
                    }
            #print(state, self.transitions[state])
                
    def rmtransition(self, transition):
        """
        Remove a transition. The transition must be in the form:
        transition = { 'qX' : ['a', ['qY'] }
        qY is going to be removed from the list of transitions from qX.
        """
        for key in transition:
            letter = transition[key][0]
            if not key in self.states:
                self.addstate(key)
            if not key in self.transitions:
                self.transitions[key] = {}
            if not letter in self.transitions[key]:
                self.transitions[key][letter] = []
            if transition[key][1][0] in self.transitions[key][letter]:
                self.transitions[key][letter].remove(transition[key][1][0])

    def walk(self, letter):
        """
        You can walk one step by one on transitions.
        The return will be the actual state. If hit an problem: None.
        If the automata is non-deterministic(oh boy..) and somewhere hit a dual-state, return None. 
        """
        if not letter in self.alphabet:
            return None
        if not self.isdeterministic():
            return None
        self.actual_state = self.transitions[self.actual_state][letter][0]
        return self.actual_state

    def detect(self, word):
        """
        Detect if it is a valid word.
        """
        if not self.isdeterministic():
            return False
        for letter in word:
            end_state = self.walk(letter)
            if end_state == None:
                break
        if end_state in self.accept:
            return True
        return False

    def rewind(self):
        """
        After a previous detect, this function will rewind the automata.
        """
        self.actual_state = self.start

    def isdeterministic(self):
        """
        Returns True if automata is deterministic and False if not.
        Remember: 'e' letter is the Empty transition.
        """
        if 'e' in self.alphabet:
            return False
        for state in self.transitions:
            for letter in self.transitions[state]:
                if len(self.transitions[state][letter]) > 1:
                    return False
        return True

    def determinize(self):
        """
        When you have a non-deterministic Automata and you want to find a deterministic equivalent form, try use this.
        It will return the new automata, deterministic one or None if the automata already deterministic.
        """
        self.rewind()
        if self.isdeterministic():
            return None
        
        automata = copy.deepcopy(self)
        automata_aux = copy.deepcopy(automata)
        check_states = {}
        over = False
        while(not over):
            # Verify the automata to get the new states
            for state in automata.transitions:
                for letter in automata.transitions[state]:
                    new_state = ''
                    is_accept = False
                    if len(automata.transitions[state][letter]) > 1:
                        # If find new state, then put into automata
                        list_states = []
                        for each in automata.transitions[state][letter]:
                            list_states.append(each)
                            if each in automata.accept:
                                is_accept = True
                            new_state += each
                        automata_aux.addstate(new_state)
                        if is_accept:
                            automata_aux.addaccept(new_state)
                        # put the new_state name into the state transition
                        automata_aux.addtransition({ state : [letter, [new_state]] })
                        for each in list_states:
                            automata_aux.addtransition({ new_state : [letter, [each]] })
                        # put the list of states that generate the new states into the check_states dictionary
                        for each in list_states:
                            if not new_state in check_states:
                                check_states[new_state] = []
                            if not each in check_states[new_state]:
                                check_states[new_state].append(each)
            # now we need check the states to see the transitions
            print("states aux:",automata_aux.transitions)
            input()


            for state in automata.transitions:
                for letter in automata.transitions[state]:
                    if len(automata.transitions[state][letter]) > 1:
                        for each in automata.transitions[state][letter]:
                            automata_aux.rmtransition({ state : [letter, [each]] })
            for state in check_states:
                for start_state in check_states[state]:
                    for letter in automata.alphabet:
                        for each in automata.transitions[start_state][letter]:
                            automata_aux.addtransition({
                                state : [letter, [each]] })
            print("states aux after:",automata_aux.transitions)
            input()
            automata = copy.deepcopy(automata_aux)
            """
            for state in check_states:
                for sub_state in check_states[state]:
                        for letter in automata.alphabet:
                        # finally after that for^3, add the state transition
                            for each in automata.transitions[sub_state][letter]:
                                automata.addtransition({
                                    state : [letter, [each]]})
                        print(automata.transitions[sub_state][letter])
                        print(automata.transitions[state][letter])
                        input()
            """
            # then, check if the automata now is deterministic
            if automata.isdeterministic():
                over = True
        return automata
