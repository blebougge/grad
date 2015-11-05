# caian 05/11/2015

def die(error_type):
    """
    Error treatment.
    """
    print(error_type)
    

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
    while line != '':
        lexar = ''
        i = 0
        token = ''
        print("line", line)
        while line[i] != '\n':
            if line[i] in list(items.keys()):
                if line[i] == '#': # comment
                    i = len(line)-2
                    token = line[:i+1]
                    lexar = '<' + token + ', ' + items['#'] + '>'
                    lexars[l] = lexar
                    l += 1
                else:
                    token = line[i]
                    lexar = '<' + token + ', ' + items[line[i]] + '>'
                    lexars[l] = lexar
                    l += 1
                print("lexar 1", lexar)
            else:
                token = ''
                while token not in list(items.keys()):
                    # print("char", line[i])
                    if line[i] in list(items.keys()):
                        if len(token) > 0:
                            lexar = '<' + token + ', ' + '???' + '>'
                            lexars[l] = lexar
                            print("lexar 2", lexar)
                            l += 1
                        lexar = '<' + line[i] + ', ' + items[line[i]] + '>'
                        print("lexar 3", lexar)
                        lexars[l] = lexar
                        l += 1
                        break
                    elif line[i] == '\n' or line[i] == ' ':
                        if token != '':
                            lexar = '<' + token + ', ' + '???' + '>'
                            lexars[l] = lexar
                            print("lexar 4", lexar)
                            l += 1
                        break
                    else:
                        token += line[i]
                        i += 1
                    # print("char token", line[i], token)

                if token in list(items.keys()):
                    lexar = '<' + token + ', ' + items[token] + '>'
                    print("lexar 6", lexar)
                    lexars[l] = lexar
                    l += 1

                if line[i] in list(items.keys()) and line[i] != token:
                    lexar = '<' + line[i] + ', ' + items[line[i]] + '>'
                    print("lexar 5", lexar)
                    lexars[l] = lexar
                    l += 1

                if line[i] == '\n':
                    break
                
            raw_input()
            token = ''
            i += 1
        
        line = f.readline()
    f.close()
    """
    fout = open(pout, 'w')
    for i in list(lexars.keys())):
        fout.write(str(lexars[i]) + '\n')
    fout.close
    """
    return lexars


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
lexars = tokenizer("lang.in", items)
tf.write("# tokenizer - lexars\n")
tf.write(str(lexars) + '\n')

fout = open("lang.out", 'w')
for i in list(lexars.keys()):
    fout.write(str(lexars[i]) + '\n')
fout.close

tf.close()

