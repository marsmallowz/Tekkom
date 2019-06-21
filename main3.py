import bhs_lexer
import bhs_interpreter
import bhs_parser
#Dengan nama FILE
from sys import *
lexer = bhs_lexer.BahasakuLexer()
parser = bhs_parser.BahasakuParser()
env = {}

file = open(argv[1])
text = file.readlines()

for line in text:
    tree = parser.parse(lexer.tokenize(line))
    bhs_interpreter.BahasakuExecute(tree, env)