# caian 09/11/2015

from automata import Automata

# Automatas:

# prog
# states
s = ['q0', 'q1', 'q2', 'q3', 'q4']
# alphabet
a =['p', 'r', 'o', 'g']
# transitions
t = {
    'q0' : {
        'p' : ['q1'] },
    'q1' : {
        'r' : ['q2'] },
    'q2' : {
        'o' : ['q3'] },
    'q3' : {
        'g' : ['q4'] },
    'q4' : {}
    }
# initial state
i = 'q0'
# final states
f = 'q4'

prog = Automata(s, a, t, i, f)

# bgin
s = ['q5', 'q6', 'q7', 'q8', 'q0']
a =['b', 'g', 'i', 'n']
t = {
    'q0' : {
        'b' : ['q5'] },
    'q5' : {
        'g' : ['q6'] },
    'q6' : {
        'i' : ['q7'] },
    'q7' : {
        'n' : ['q8'] },
    'q8' : {}
    }
i = 'q0'
f = 'q8'

bgin = Automata(s, a, t, i, f)

# nd
s = ['q0', 'q9', 'q10']
a =['n', 'd']
t = {
    'q0' : {
        'n' : ['q9'] },
    'q9' : {
        'd' : ['q10'] },
    'q10' : {}
    }
i = 'q0'
f = 'q10'

nd = Automata(s, a, t, i, f)

# fix
s = ['q0', 'q11', 'q12', 'q13']
a =['f', 'i', 'x']
t = {
    'q0' : {
        'f' : ['q11'] },
    'q11' : {
        'i' : ['q12'] },
    'q12' : {
        'x' : ['q13'] },
    'q13' : {}
    }
i = 'q0'
f = 'q13'

fix = Automata(s, a, t, i, f)

# ary
s = ['q0', 'q14', 'q15', 'q16', 'q17']
a =['a', 'r', 'y']
t = {
    'q0' : {
        'a' : ['q14'] },
    'q14' : {
        'r' : ['q15'] },
    'q15' : {
        'y' : ['q16'] },
    'q16' : {}
    }
i = 'q0'
f = 'q16'

ary = Automata(s, a, t, i, f)

# :
s = ['q0', 'q17']
a =[':']
t = {
    'q0' : {
        ':' : ['q17'] },
    'q17' : {}
    }
i = 'q0'
f = 'q17'

two_points = Automata(s, a, t, i, f)

# (
s = ['q0', 'q18']
a =['(']
t = {
    'q0' : {
        '(' : ['q18'] },
    'q18' : {}
    }
i = 'q0'
f = 'q18'

start_par = Automata(s, a, t, i, f)

# )
s = ['q0', 'q19']
a =[')']
t = {
    'q0' : {
        ')' : ['q19'] },
    'q19' : {}
    }
i = 'q0'
f = 'q19'

end_par = Automata(s, a, t, i, f)

# #
s = ['q0', 'q20', 'q21']
a =['#']
t = {
    'q0' : {
        '#' : ['q20'] },
    'q20' : {
        '\n' : ['q21']},
    'q21' : {}
    }
i = 'q0'
f = 'q21'

comment = Automata(s, a, t, i, f)

# ,
s = ['q0', 'q22']
a =[',']
t = {
    'q0' : {
        ',' : ['q22'] },
    'q22' : {}
    }
i = 'q0'
f = 'q22'

comma = Automata(s, a, t, i, f)

# int
s = ['q0', 'q23', 'q24', 'q25']
a =['i', 'n', 't']
t = {
    'q0' : {
        'i' : ['q23'] },
    'q23' : {
        'n' : ['q24'] },
    'q24' : {
        't' : ['q25'] },
    'q25' : {}
    }
i = 'q0'
f = 'q25'

int_op = Automata(s, a, t, i, f)

# dob
s = ['q0', 'q26', 'q27', 'q28']
a =['d', 'o', 'b']
t = {
    'q0' : {
        'd' : ['q26'] },
    'q26' : {
        'o' : ['q27'] },
    'q27' : {
        'b' : ['q28'] },
    'q28' : {}
    }
i = 'q0'
f = 'q28'

dob_op = Automata(s, a, t, i, f)

# bl
s = ['q0', 'q29', 'q30']
a =['b', 'l']
t = {
    'q0' : {
        'b' : ['q29'] },
    'q29' : {
        'l' : ['q30'] },
    'q30' : {}
    }
i = 'q0'
f = 'q30'

bl_op = Automata(s, a, t, i, f)

# str
s = ['q0', 'q31', 'q32', 'q33']
a =['s', 't', 'r']
t = {
    'q0' : {
        's' : ['q31'] },
    'q31' : {
        't' : ['q32'] },
    'q32' : {
        'r' : ['q33'] },
    'q33' : {}
    }
i = 'q0'
f = 'q33'

str_op = Automata(s, a, t, i, f)

# whil
s = ['q0', 'q34', 'q35', 'q36', 'q37']
a =['w', 'h', 'i', 'l']
t = {
    'q0' : {
        'w' : ['q34'] },
    'q34' : {
        'h' : ['q35'] },
    'q35' : {
        'i' : ['q36'] },
    'q36' : {
        'l' : ['q37'] },
    'q37' : {}
    }
i = 'q0'
f = 'q37'

whil = Automata(s, a, t, i, f)

# if
s = ['q0', 'q38', 'q39']
a =['i', 'f']
t = {
    'q0' : {
        'i' : ['q38'] },
    'q38' : {
        'f' : ['q39'] },
    'q39' : {}
    }
i = 'q0'
f = 'q39'

if_cond = Automata(s, a, t, i, f)

# rad
s = ['q0', 'q40', 'q41', 'q42']
a =['r', 'a', 'd']
t = {
    'q0' : {
        'r' : ['q40'] },
    'q40' : {
        'a' : ['q41'] },
    'q41' : {
        'd' : ['q42'] },
    'q42' : {}
    }
i = 'q0'
f = 'q42'

rad = Automata(s, a, t, i, f)

# here, the lex works.

def automata_union(automata_list):
    """
    Do the union to the automatas.
    """
    
    final = Automata()

    final.start = 'q0'

    for auto in automata_list:
        for st in list(auto.transitions):
            if st not in final.states:
                final.states.append(st)
            if len(list(auto.transitions[st])) > 0:
                for letter in list(auto.transitions[st]):
                    if letter not in final.alphabet:
                        final.alphabet.append(letter)
                    for reach in auto.transitions[st][letter]: 
                        if reach not in final.states:
                            final.states.append(reach)
                        final.transitions[st] = { letter : auto.transitions[st][letter] }
            if st in auto.accept:
                if st not in final.accept:
                    final.accept.append(st)
    return final

def do_union():
    """
    Do the union to all the automatas in this file.
    """

    automatas = [prog, bgin, nd, ary, two_points, fix, start_par, end_par, 
                comment, comma, int_op, dob_op, bl_op, str_op, whil, if_cond,
                rad]
    last = automata_union(automatas)
    lastD = last.determinize()

    return lastD
