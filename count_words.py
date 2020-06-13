texto = 'Este texto tiene algunas palabras Este es otro texto con algunas palabras diferentes'

words = texto.split(' ')

#print(words)

dic_words = {}

cont = 1

for word in words:
    if word in dic_words:
        #print(word)
        dic_words[word] = cont + 1
    else:
        #print(word)
        dic_words[word] = cont  
    
for key_word, counts in dic_words.items():
    print(f'La palabra {key_word} aparece {counts} veces en el texto')