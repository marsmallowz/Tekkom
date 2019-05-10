import h_lexer
import h_interpreter
import h_parser

from sys import *
lexer = h_lexer.BasicLexer()
parser = h_parser.BasicParser()
env = {}

file = open(argv[1])
text = file.readlines()

for line in text:
    tree = parser.parse(lexer.tokenize(line))
    h_interpreter.BasicExecute(tree, env)