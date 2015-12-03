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
                items[line_items[0]][line_items[i]] = line_items[i+1]
        
        line = f.readline()

    f.close()
    return items

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
    for j in list(table[i]):
        test_file.write('{ ' + j + ' : ' + table[i][j] + ' } ')
    test_file.write('\n')

test_file.write('\n')

# - test lang.tab END

# close test file
test_file.close()
