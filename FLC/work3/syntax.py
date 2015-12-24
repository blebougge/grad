# caian

def readFile(path=None):
    """
    Return a dictionary based on path file.
    """
    if path == None:
        return None
    p = path
    f = open(p, 'r')

    line = f.readline()
    items = {}
    while line != '':
        line_items = line.split()
        items[line_items[0]] = line_items[1:]

        line = f.readline()

    f.close()
    return items

def readTableFile(path=None):
    """
    Return the table file as dictionary of list
    """
    if path == None:
        return None
    p = path
    f = open(p, 'r')

    line = f.readline()
    items = {}
    while line != '':
        line_items = line.split()
        items[line_items[0]] = {}
        for i in range(1, len(line_items[1:])):
            if i % 2 == 1:
                items[line_items[0]][line_items[i+1]] = line_items[i]
        
        line = f.readline()

    f.close()
    return items

def readProdFile(path=None):
    """
    Return the prod file as productions to put into the stack
    """
    if path == None:
        return None
    p = path
    f = open(p, 'r')

    line = f.readline()
    items = {}
    j = 1
    while line != '':
        line_items = line.split()
        items[line_items[0]] = {}
        items[line_items[0]][j] = []
        for i in range(1, len(line_items[1:]) + 1):
            if line_items[i] != "|":
                items[line_items[0]][j].append(line_items[i])
            else:
                j += 1
                items[line_items[0]][j] = []
        j += 1
        line = f.readline()

    f.close()
    return items

def readTokens(path=None):
    """
    Read the token file.
    """
    if path == None:
        return None
    p = path
    f = open(p, 'r')

    line = f.readline()
    items = {}
    j = 1
    while line != "":
        token = line[1:-2]
        token_items = token.split(', ')
        items[j] = token_items
        # if want to view the construction of the list:
        # print(token_items)
        # input()
        j += 1
        line = f.readline()
    f.close()
    return items

def getToken(tokens, num):
    """
    Get the token info to use in the syntax stack analyzer
    """
    # reserved words
    res_word = ['???', 'CONST', 'OP', 'LOG', 'TYPE']

    item = ""
    if tokens[i][1] in res_word:
        if tokens[i][1] == '???':
            item = "ID"
        else:
            item = lang[i][1]
    else:
        item = lang[i][0]

    return item

# the real program runs ahead
# test file
test_file = open("tests.out", 'w')

# - test - first-follow read START
first_file = "lang.first"
first = readFile(first_file)

test_file.write("# FIRST\n")
keys_first = list(first.keys())
for i in keys_first:
    test_file.write(i + ' := ')
    for j in first[i]:
        test_file.write(j + ' ')
    test_file.write('\n')

test_file.write('\n')

follow_file = "lang.follow"
follow = readFile(follow_file)

test_file.write("# FOLLOW\n")
keys_follow = list(follow.keys())
for i in keys_follow:
    test_file.write(i + ' := ')
    for j in follow[i]:
        test_file.write(j + ' ')
    test_file.write('\n')

test_file.write('\n')

# - test - first-follow read END

# - test lang.tab START
table_file = "lang.tab"
table = readTableFile(table_file)

test_file.write('# TABLE\n')
keys_table = list(table.keys())
for i in keys_table:
    test_file.write(i + ' := ')
    for j in list(table[i].keys()):
        test_file.write('{ ' + j + ' : ' + table[i][j] + ' } ')
    test_file.write('\n')

test_file.write('\n')

# - test lang.tab END

# - test lang.prod START
prod_file = "lang.prod"
prod = readProdFile(prod_file)

test_file.write("# PROD\n")
keys_prod = list(prod.keys())
for i in keys_prod:
    test_file.write(i + ' = ' + str(prod[i]))
    test_file.write('\n')

test_file.write('\n')
# - test lang.prod END

# REAL THING

tokens = "lang.out"
lang = readTokens(tokens)

# - test lang.out write START
test_file.write("# lang.out -> dictionary\n")
test_file.write(str(lang))
# - test lang.out write END

lines = len(list(lang.keys())) + 1
stack = ["$"]
stack.append("<PROG>")
i = 1
token = getToken(lang, i)

while stack != ['$']:
    if i > lines:
        print("ERR = EOF")
        break

    print("{" + str(stack) + " | " + token)
    #print("token["+ str(i) + "] = " + str(lang[i]))
    #input()

    if stack[-1] == token:
        i += 1
        if i < lines:
            token = getToken(lang, i)
        del stack[-1]
    else:
        top = stack[-1]
        next_prod = prod[top][int(table[top][token])]

        del stack[-1]
        # reversed list
        next_prod_rev = next_prod[::-1]
        for item in next_prod_rev:
            if item != '&':
                stack.append(item)

if stack == ["$"]:
    print("Syntax Analyze: ", True)
else:
    print("Syntax Analyze: ", False)

# close test file
test_file.close()
