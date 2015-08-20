# caian 20/08/2015

"""
Input and console functions
"""
console = "> "

def ask():
    return raw_input(console)

def ask(message):
    s = "%s\n%s" % (message, console)
    return raw_input(s)

def ask_num():
    return int(ask())

def ask_num(message):
    return int(ask(message))

