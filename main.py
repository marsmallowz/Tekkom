import bhs_lexer
import bhs_parser
import bhs_interpreter

if __name__ == '__main__':
    lexer = bhs_lexer.BahasakuLexer()
    parser = bhs_parser.BahasakuParser()
    env = {}
    while True:
        try:
            text = input('BHS > ')
        except EOFError:
            break
        if text:
            tree = parser.parse(lexer.tokenize(text))
            bhs_interpreter.BahasakuExecute(tree, env)
