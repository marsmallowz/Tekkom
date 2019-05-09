import re
class Lexer(object):
	"""dosource_codering for Lexer"""
	def __init__(self, source_code):
			self.source_code = source_code

	def token(self):
	#print('test')

		# Where all the tokens dibuat oleh lexer akan di stored
		tokens = []
		# Menampung wordlist di test lang
		source_code =self.source_code.split()
		# Will keep track f the word index
		source_index = 0

		#Mengulangi isi pada  test lang
		while source_index < len(source_code):

			kata = source_code[source_index]
			#mengandung token tyoe dan value ke tokens
			if kata == "var": tokens.append(["VAR_DECLERATION", kata])
			# harus menambahkan import re  berguna jika kita tidak menemmukan sesuatu yang tidak spesifikasi
			elif re.match('[a-z]', kata) or re.match('[A-Z]', kata):
				if kata[len(kata)-1] == ";":
					tokens.append(['id', kata[0:len(kata)-1]])
				else:
					tokens.append(['id', kata])
			# sekarang untuk angka
			elif re.match('[0-9]', kata):
				if kata[len(kata)-1] == ";":
					tokens.append(['int', kata[0:len(kata)-1]])
				else:
					tokens.append(['Int', kata])

			elif kata in "=/*=+":
				tokens.append(['OP', kata])

			if kata[len(kata)-1] == ";":
				tokens.append(['symbol', ';'])

			#print(source_code[source_index])
			#Menambah increment agar tidak melakukan re-check token
			

			source_index += 1
			
		print(tokens)
		return tokens