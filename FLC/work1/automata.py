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
                'e' : ['M'],           # e = Empty transition
                '1' : ['q1'],
                '2' : ['M']},          # ['M'] = dead state
            'q1' : {
                'a' : ['q1'],
                'b' : ['q0','q1'],
                'e' : ['M'],
                '1' : ['q1'],
                '2' : ['M']}
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
        Already add's the Dead states.
        """
        if not state in self.states:
            self.states.append(state)
        for letter in self.alphabet:
            if letter != 'e':
                self.transitions = { letter : ['M'] }
            else:
                self.transitions = { letter : [state] }

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
            # the method rmtransition will seek for Dead states.
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
                self.transitions[state][letter] = ['M']

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
                if 'M' in self.transitions[state][transition[state][0]]:
                    self.transitions[state][transition[state][0]].remove('M')
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
            if len(self.transitions[key][letter]) == 0:
                self.transitions[key][letter].append('M')

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
            if end_state == 'M':
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

    def _isdeterministic(self, transitions):
        """
        Returns True if automata is deterministic and False if not.
        Remember: 'e' letter is the Empty transition.
        
        This function will be used JUST in determinize function.
        """
        if 'e' in self.alphabet:
            return False
        for state in transitions:
            for letter in transitions[state]:
                if len(transitions[state][letter]) > 1:
                    return False
        return True

    def _addstate(self, transitions, transition):
        """
        Adds a transition to transitions sequence. The transition must be in the form:
        transition = { 'qX' : ['z', ['qY']] }
        
        This function will be used in determinize function.
        """
        state = list(transition.keys())[0]
        letter = transition[state][0]
        add = transition[state][1] # this is a list!

        if not state in transitions:
            transitions[state] = {}
        if not letter in transitions[state]:
            transitions[state][letter] = []
        if len(add) > 0:
            if not add[0] in transitions[state][letter]:
                transitions[state][letter].append(add[0])
            if 'M' in transitions[state][letter]:
                transitions[state][letter].remove('M')
        else:
            transitions[state] = {
                letter : add
                }

    def _rmstate(self, transitions, transition):
        """
        Remove a transition. The transition must be in the form:
        transition = { 'qX' : ['a', ['qY'] }
        qY is going to be removed from the list of transitions from qX.
        
        This function will be used in determinize function.
        """
        state = list(transition.keys())[0]
        letter = transition[state][0]
        rm = transition[state][1] # this is a list!

        if not state in transitions:
            transitions[state] = {}
        if not letter in transitions[state]:
            transitions[state][letter] = []
        if len(rm) != 0:
            if rm[0] in transitions[state][letter]:
                transitions[state][letter].remove(rm[0])
            if len(transitions[state][letter]) == 0:
                transitions[state][letter].append('M')
        else:
            transitions[state] = {
                letter : ['M']
                }

    def closure(self):
        """
        When the automata is non-deterministic, you have to seek for 'e' transitions. This method
        calculates this and return a new equivalent automata.
        """
        # if it's already a deterministic one
        if self.isdeterministic():
            return self
        # if you don't have empty transitions
        if not 'e' in self.alphabet:
            return self

        # now we have the magic
        return self
        

    def determinize(self):
        """
        When you have a non-deterministic Automata and you want to find a deterministic equivalent form, try use this.
        It will return the new automata, deterministic one or self if the automata already deterministic.
        """
        # if the automata already is deterministic
        if self.isdeterministic():
            return self

        # we need to calculate the closure of the automata
        nonE = self.closure()

        automata = copy.deepcopy(nonE)
        trs = copy.deepcopy(nonE.transitions)
        trsa = {}
        """
        The dictionary to check the new states. It will be on the form:
            check_states = {
                'q0q1' : ['q0','q1'],
                ...
                }
        inside_aux will help on being the list.
        """
        check_states = {}
        inside_aux = []

        print(trs)
        over = False
        while not over:
            # for each state in transition
            for state in trs:
                # for each letter in alphabet
                for letter in nonE.alphabet:
                    # each reached state
                    is_accept = False
                    reached = trs[state][letter]
                    new_state = ''
                    if len(trs[state][letter]) > 1:
                        # for each reached state
                        for each in reached:
                            if each in nonE.accept:
                                is_accept = True
                            new_state += each
                            inside_aux.append(each)
                    if new_state != '':
                        # add the new state to reach on the state
                        nonE._addstate(trsa, { state : [letter, [new_state]] })
                        if state != new_state:
                            # for each reached state
                            for each in reached:
                                nonE._addstate(trsa, { new_state : [letter, [each]] })
                        for each in check_states:
                            for st in inside_aux:
                                check_states[each].append(st)
                        check_states[new_state] = inside_aux
                        if is_accept:
                            automata.accept.append(new_state)
                    else:
                        nonE._addstate(trsa, { state : [letter, reached] })
                    inside_aux = []
            # now, we need check the generated states!
            for state in check_states:
                for gen in check_states[state]:
                    for letter in nonE.alphabet:
                        # remove the states from the composition of the new_state
                        nonE._rmstate(trsa, {state : [letter, [gen]] })
                        # to ever state reached, insert here
                        for reached in trsa[gen][letter]:
                            # if not reached already on another state
                            if not reached in check_states[state]:
                                nonE._addstate(trsa, { state : [letter, [reached]] })
            
            trs = copy.deepcopy(trsa)
            # then, check if the automata now is deterministic
            if nonE._isdeterministic(trs):
                over = True
        for each in check_states:
            automata.states.append(each)
        """
        On automata object we have: All States, Accept-States, Start-State and Alphabet.
        Just put the Transitions there and kapow!
        """
        automata.transitions = copy.deepcopy(trs)

        return automata
