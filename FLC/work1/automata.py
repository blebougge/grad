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
        else:
            transitions[state] = {
                letter : []
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
        # return automata
        rauto = copy.deepcopy(self)
        # transitions
        trs = {}
        
        # we need certificate that the state go to itself with an empty transition.
        for state in rauto.transitions:
            if not state in trs.keys():
                trs[state] = {}
            if not 'e' in trs[state].keys():
                trs[state]['e'] = []
            if not state in trs[state]['e']:
                trs[state]['e'].append(state)

        for state in rauto.transitions:
            for letter in rauto.alphabet:
                # if not  a empty transition
                if letter != 'e':
                    if not state in trs.keys():
                        trs[state] = {}
                    if not letter in trs[state].keys():
                        trs[state][letter] = []
                    # for each state in empty transitions
                    for each in trs[state]['e']:
                        if not each in trs[state][letter]:
                            trs[state][letter].append(each)
                    # for each state in original transitions
                    for each in rauto.transitions[state][letter]:
                        if not each in trs[state][letter]:
                            trs[state][letter].append(each)
            #print("for", state, trs)
        # put the transitions on the regular places
        rauto.transitions = trs
        # remove 'e' from alphabet
        rauto.rmletter('e')
        #print("inside:",trs)
        
        return rauto

    def determinize(self):
        """
        When you have a non-deterministic Automata and you want to find a deterministic equivalent form, try use this.
        It will return the new automata, deterministic one or self if the automata already deterministic.
        """
        # if the automata already is deterministic
        if self.isdeterministic():
            return self

        # we need to calculate the closure of the automata. nonE is the automata without 'e' transitions
        nonE = self.closure()

        # transitions of the automata. This line is used to better code
        trs = copy.deepcopy(nonE.transitions)
        # transitions trs auxiliar
        trsa = {}

        # the dictionary to find the composition of the states
        composition = {}

        # to help on the new state, we need to create with some order
        sequence = []

        # new accept states:
        new_accept = []

        over = False
        while not over:

            # for each state in transition
            for state in trs:

                # for each letter in alphabet
                for letter in nonE.alphabet:

                    is_accept = False

                    # reached states
                    reached = trs[state][letter]
                    new_state = ''
                    sequence = []

                    # if we have more than one reached state
                    if len(trs[state][letter]) > 1:

                        # for each reached state in the list
                        for each in reached:
                            if each in nonE.accept:
                                is_accept = True
                            sequence.append(each)

                        # auxiliar sequence list
                        sequencea = []

                        # check if the composition already have the states
                        for st in sequence:
                            if st in composition:
                                for each in composition[st]:
                                    if not each in sequence:
                                        sequencea.append(each)
                        if len(sequencea) != 0:
                            for each in sequencea:
                                if not each in sequence:
                                    sequence.append(each)
 
                        # sequential addition of states
                        for each in nonE.states:
                            if each in sequence:

                                # here we add in sequence
                                new_state += each
                            
                        # print("new_state sequence", new_state, sequence)
                        if not new_state in list(composition.keys()):
                            composition[new_state] = sequence

                        # add the new_state to the state
                        nonE._addstate(trsa, { state : [letter, [new_state]] })

                        # add the new_state to the trsa
                        for each in composition[new_state]:

                            # add the transitions to the new state
                            for l in trs[each]:
                                for st in trs[each][l]:
                                    nonE._addstate(trsa, { new_state : [l, [st]] })

                            # remove the compositions of the new state
                            # for each letter in new state
                            for l in trsa[new_state]:

                                # for each state in letter transition
                                for st in trsa[new_state][l]:

                                    # if state is in the list of new_states
                                    if st in list(composition.keys()):

                                        # for each state that is diffrent from the original
                                        for s in trsa[new_state][l]:
                                            if s != st:

                                                # if the state is in the list of composition of the original state, remove
                                                if s in composition[st]:
                                                    # print("new l st comp", new_state, l, s, composition[new_state])
                                                    nonE._rmstate(trsa, { new_state : [l, [s]] })

                                                # if the state s is a composite state of st
                                                elif s in list(composition.keys()):
                                                    if set(composition[s]).issubset(set(composition[st])):
                                                        # print("set",set(composition[s]).issubset(set(composition[st])), composition[s])
                                                        # print("comp", composition[s])
                                                        nonE._rmstate(trsa, { new_state : [l, [s]] })

                        # add the new_state to the old trs state
                        nonE._addstate(trsa, { state : [letter, [new_state]] })

                        # if is accept state add to the accept states
                        if is_accept:
                            new_accept.append(new_state)

                    # else, we just add the simple state
                    else:
                        # print('trs', state, letter, trs[state][letter])
                        nonE._addstate(trsa, { state : [letter, trs[state][letter]] } )

            # now we need to put the trsa in trs
            trs = copy.deepcopy(trsa)
            trsa = {}
            # print("transitions", trs)
            # input()

            # then, check if the automata now is deterministic
            if nonE._isdeterministic(trs):
                over = True
            
        # adds to the new_states
        for each in list(composition.keys()):
            if not each in nonE.states:
                nonE.states.append(each)

        # adds the accept states
        for each in new_accept:
            if not each in nonE.accept:
                nonE.accept.append(each)

        """
        On automata object we have: All States, Accept-States, Start-State and Alphabet.
        Just put the Transitions there and kapow!
        """
        nonE.transitions = copy.deepcopy(trs)

        return nonE

    def _buildexpression(self, r1=None, r2=None, r3=None, r4=None):
        """
        This method is a internal use for the toRegEx method. This one build a expression from r1, r2, r3 and r4
        given. The return will be in the form:
            
            expression = (R1(R2)*R3)UR4

        """
        expression = ''
        flag1 = len(r1) > 0
        flag2 = len(r2) > 0
        flag3 = len(r3) > 0
        flag4 = len(r4) > 0
        if flag1 or flag3:
            expression += '('
            if flag1:
                expression += r1
            if flag2:
                expression += '(' + r2 + ')*'
            if flag3:
                expression += r3
            expression += ')'
        elif flag2:
            expression += '(' + r2 + ')*'
        if flag4:
            if len(expression) > 0:
                if len(r4) > 1:
                    expression += 'U(' + r4 + ')'
                else:
                    expression += 'U' + r4

        return expression

    def toRegEx(self):
        """
        This method returns the RegEx of the given automata. If the automata is not deterministic, return a simple error.
        """

        if not self.isdeterministic():
            return None

        automata = copy.deepcopy(self)

        # first we need to add the new start and finish states
        start_state = 'S'
        finish_state = 'F'

        automata.start = start_state
        automata.accept = [finish_state]
        automata.states.append(start_state)
        automata.states.append(finish_state)

        # now we put the 'e' transition from start_state to old start state and from every accept state to finish_state
        automata.transitions[start_state] = { 'e' : [ self.start ]}
        automata.transitions[finish_state] = { 'e' : []}
        for each in self.accept:
            automata.transitions[each]['e'] = []
            automata.transitions[each]['e'].append(finish_state)

        automata.alphabet.append('e')

        # the RegEx automata convertion
        regex = copy.deepcopy(automata)

        # we need to start remove the others states
        k = len(automata.states)
        while k > 2:

            # start choosing a state that is not the start or finish states
            rem_i = 0
            rem = automata.states[rem_i]
            while rem == start_state and rem == start_state:
                rem_i += 1
                if rem_i > len(regex.states):
                    print("Error on regex states")
                rem = regex.states[rem_i]

            # with the state to remove selected, we need remove it

            r1 = ''
            r2 = ''
            r3 = ''
            r4 = ''

            # R2 = d(q_rem, q_rem)
            for l in regex.alphabet:
                if l in list(regex.transitions[rem].keys()):
                    if rem in regex.transitions[rem][l]:
                        if l != 'e':
                            if len(r2) > 0:
                                r2 += 'U'
                            if len(l) > 1:
                                r2 += '(' + l + ')'
                            else:
                                r2 += l

            for state in list(regex.transitions.keys()):

                # q_i = state
                if state != rem:

                    for l in regex.alphabet:
                        if l in list(regex.transitions[state].keys()):

                            if rem in regex.transitions[state][l]:

                                # R1 = d(q_i, q_rem)
                                if l != 'e':
                                    if len(r1) > 0:
                                        r1 += 'U'
                                    if len(l) > 1:
                                        r1 += '(' + l + ')'
                                    else:
                                        r1 += l

                                # q_j = other
                                for other in list(regex.transitions.keys()):

                                    # if other state is diffrent from q_i and from q_rem
                                    if other != state and other != rem:

                                        # R3 = d(q_rem, q_j)
                                        if l in list(regex.transitions[rem].keys()):
                                            if other in regex.transitions[rem][l]:
                                                if l != 'e':
                                                    if len(r3) > 0:
                                                        r3 += 'U'
                                                    if len(l) > 1:
                                                        r3 += '(' + l + ')'
                                                    else:
                                                        r3 += l

                                        # R4 = d(q_i, q_j)
                                        for letter in regex.alphabet:
                                            if letter in list(regex.transitions[state].keys()):

                                                # if other is in the transitions of the state
                                                if other in regex.transitions[state][letter]:
                                                    if letter != 'e':
                                                        if len(r4) > 0:
                                                            r4 += 'U'
                                                        if len(letter) > 1:
                                                            r4 += '(' + letter + ')'
                                                        else:
                                                            r4 += letter
    
                                                    # remove the old transition to q_j by letter 'letter'
                                                    if letter in automata.transitions[state].keys():
                                                        del automata.transitions[state][letter]

                                        # HERE WE PUT THE NEW TRANSITION IN THE AUTOMATA
                                        # build the expression
                                        new_expression = automata._buildexpression(r1, r2, r3, r4)

                                        # add the new expression to the state transition
                                        automata.transitions[state] = { new_expression : [other] }

                                        # the new_expression to alphabet
                                        if not new_expression in automata.alphabet:
                                            automata.alphabet.append(new_expression)
                                        print('\t\tnew_expression', new_expression)


            # and now we remove 'rem' from automata and copy to regex
            del automata.transitions[rem]
            automata.states.remove(rem)
            regex = copy.deepcopy(automata)

            print("\tregex.transitions", regex.transitions)
            print("\tregex.alphabet", regex.alphabet)
            input()

            # check the k states remaining
            k = len(automata.states)
        

        print("\tautomata.transitions", automata.transitions)
        print("\tautomata.states", automata.states)

        return list(regex.transitions[start_state].keys())[0]

