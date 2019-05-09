import lexer
import mparser
def main():
	#Untuk Membaca file test secara langsung
	content = ""
	with open ('test.lang', 'r') as file:
		content = file.read()

		#print(content)

		#memanggil kelas lexer dan initiliazed
		lex = lexer.Lexer(content)
		tokens = lex.token()

	
	
	
		parse = mparser.Parser(tokens)
		parse.parse()

main()