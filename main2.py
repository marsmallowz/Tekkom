import bhs_lexer
import bhs_interpreter
import bhs_parser

lexer = bhs_lexer.BahasakuLexer()
parser = bhs_parser.BahasakuParser()
env = {}

file = open('test.bhs')
text = file.readlines()

for line in text:
    tree = parser.parse(lexer.tokenize(line))
    bhs_interpreter.BahasakuExecute(tree, env)
