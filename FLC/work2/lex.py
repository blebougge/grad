# caian 05/11/2015

import langAuto

# ----- print automata things start ------

def write_fsm(out, fsm):
    to_print = "Automata: \n"
    to_print += "\tstates: " + str(fsm.states) + "\n"
    to_print += "\talphabet: " + str(fsm.alphabet) + "\n"
    to_print += "\ttransitions: " + str(fsm.transitions) + "\n"
    to_print += "\tstart: " + str(fsm.start) + "\n"
    to_print += "\taccept: " + str(fsm.accept) + "\n"
    out.write(to_print)

# ----- print automata things end ------

def readItems(path=None):
    """
    Return a dictionary based on path file.
    """
    p = "lang.items"
    if path != None:
        p = path
    f = open(p, 'r')

    line = f.readline()
    items = {}
    while line != '':
        item = ''
        i = 0
        while line[i] != ' ':
            item += line[i]
            i += 1
        definition = ''
        i += 1
        while line[i] != '\n':
            definition += line[i]
            i += 1

        items[item] = definition
        line = f.readline()

    f.close()
    return items

def tokenizer(path=None, items=None):
    """
    Simple tokenizer function.
    """
    if items != None:
        it = items
    else:
        it = readItems()

    pin = "lang.in"
    # pout = "lang.out"
    if path != None:
        pin = path

    f = open(pin, 'r')

    line = f.readline()
    l = 0
    lexars = {}
    # print('lines readed: ')
    while line != '':
        lexar = ''
        i = 0
        token = ''
        # print("",line)
        while line[i] != '\n':
            token = ''
            if line[i] in list(items.keys()):
                if line[i] == '#': # comment
                    i = len(line)-2
                    token = line[:i+1]
                    lexar = '<' + token + ', ' + items['#'] + '>'
                    lexars[l] = lexar
                    l += 1
                elif items[line[i]] == items['0']:
                    token = line[i]
                    while line[i+1] in list(items.keys()):
                        if items[line[i+1]] == items['0']:
                            i += 1
                            token += line[i]
                        else:
                            break
                    lexar = '<' + token + ', ' + items[line[i]] + '>'
                    lexars[l] = lexar
                    l += 1
                else:
                    token = line[i]
                    lexar = '<' + token + ', ' + items[line[i]] + '>'
                    lexars[l] = lexar
                    l += 1
                # print("lexar 1", lexar)
            else:
                while token not in list(items.keys()):
                    # print("char", line[i])
                    if line[i] in list(items.keys()):
                        if len(token) > 0:
                            lexar = '<' + token + ', ' + '???' + '>'
                            lexars[l] = lexar
                            # print("lexar 2", lexar)
                            l += 1
                        lexar = '<' + line[i] + ', ' + items[line[i]] + '>'
                        # print("lexar 3", lexar)
                        lexars[l] = lexar
                        l += 1
                        i += 1
                        break
                    elif line[i] == '\n' or line[i] == ' ':
                        if token != '':
                            lexar = '<' + token + ', ' + '???' + '>'
                            lexars[l] = lexar
                            # print("lexar 4", lexar)
                            l += 1
                        break
                    else:
                        token += line[i]
                        i += 1
                    # print("char token", line[i], token)

                if token in list(items.keys()):
                    lexar = '<' + token + ', ' + items[token] + '>'
                    # print("lexar 5", lexar)
                    lexars[l] = lexar
                    l += 1

                if line[i] in list(items.keys()) and line[i] != token:
                    lexar = '<' + line[i] + ', ' + items[line[i]] + '>'
                    # print("lexar 6", lexar)
                    lexars[l] = lexar
                    l += 1

                if line[i] == '\n':
                    break

            # uncomment the line to see on the fly
            # raw_input()
            i += 1

        if len(token) > 0:
            lexars[l] = '<' + ';' + ', ' + items[';'] + '>'
            l += 1

        line = f.readline()
    f.close()
    """
    fout = open(pout, 'w')
    for i in list(lexars.keys())):
        fout.write(str(lexars[i]) + '\n')
    fout.close
    """
    return lexars

def tokenizer_new(path=None, items=None):
    """
    New tokenizer function.
    """
    pass


# the real program runs ahead
# test file
tf = open("tests.out", 'w')

# tests - readItems
items = readItems()
tf.write("# readItems - no arg\n")
tf.write(str(items) + '\n')
tf.write("# readItems - correct use\n")
items = readItems("lang.items")
tf.write(str(items) + '\n')
tf.write('\n')

# tests - tokenizer
lexars = tokenizer("lang.items", items)
tf.write("# tokenizer - lang.items lexars\n")
tf.write(str(lexars) + '\n')

fitemsout = open("lang.items.out", 'w')
for i in list(lexars.keys()):
    fitemsout.write(str(lexars[i]) + '\n')
fitemsout.close()

lexars = tokenizer("langError.in", items)
tf.write("# tokenizer - langError.in lexars\n")
tf.write(str(lexars) + '\n')

ferrorout = open("langError.out", 'w')
for i in list(lexars.keys()):
    ferrorout.write(str(lexars[i]) + '\n')
ferrorout.close()

lexars = tokenizer("lang.in", items)
tf.write("# tokenizer - lang.in lexars\n")
tf.write(str(lexars) + '\n')

fout = open("lang.out", 'w')
for i in list(lexars.keys()):
    fout.write(str(lexars[i]) + '\n')
fout.close()

# ------ new tokenizer test -------- 

lexars = tokenizer_new("lang.in", items)
tf.write("# tokenizer - NEW TOKENIZER lang.in lexars\n")
tf.write(str(lexars) + '\n')

fnewout = open("langNew.out", 'w')
if lexars != None:
    for i in list(lexars.keys()):
        fnewout.write(str(lexars[i]) + '\n')
fnewout.close()

# ------ end of new tokenizer test -------- 

# ------ automata test ------

master_automata = langAuto.do_union()

fauto = open("automata.out", 'w')
if master_automata != None:
    fauto.write(str(master_automata))
    # write_fsm(fauto, master_automata)
fauto.close()

# ------ ent of automata test ------- 


tf.close()

