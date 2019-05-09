import h_lexer
import h_interpreter
import h_parser

if __name__ == '__main__':
    lexer = h_lexer.BasicLexer()
    parser = h_parser.BasicParser()
    env = {}
    while True:
        try:
            text = input('basic > ')
        except EOFError:
            break
        if text:
            tree = parser.parse(lexer.tokenize(text))
            h_interpreter.BasicExecute(tree, env)