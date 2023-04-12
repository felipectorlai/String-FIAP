# Funcoes em string

# Retorna o tamanho (qaunt. de caracteres) da String

palavra = "Aula de Python"

print( (len(palavra) ))

# Converter todos os caracteres para minusculo

palavra_minusc = palavra.lower()
print(palavra_minusc)

# Converter todos os carecteres em maiusculo

palavra_maiusc = palavra.upper()
print(palavra_maiusc)

# Separar palavras de um texto

palavras = palavra.split(" ")
print(palavras)

# Substituir (trocar) palavras de um texto

nova_palavra = palavra.replace("Python" , "Java")
print(nova_palavra)