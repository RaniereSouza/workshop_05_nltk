from pprint import pprint
import nltk

nltk.download() #de preferência criar uma maneira de rodar só uma vez

stop_words = set(nltk.corpus.stopwords.words('english'))
stemmer = nltk.stem.PorterStemmer()
lemmatizer = nltk.stem.WordNetLemmatizer()

first_text_to_parse = """This is a test to see how well NLTK can do some basic operations.
First, we're going to try and break this whole string in sentences.
After that, we're going to separate the string in words (tokens).
Finally, we're going to remove stop words from the tokens."""

words_to_stem = ['programer', 'programming', 'programmed', 'programs']
words_to_lemmatize = ['been', 'was', 'were', 'is', 'are']

text_with_named_entities = """Former president Barack Obama did not shake hands with current president Donald Trump."""

while True:

  print('\n\nEscolha uma das opções a seguir:')
  option = input('(a) Segmentação; (b) Tokenização; (c) Remoção de Stop Words; (d) Stemming; (e) Lematização; (f) POS Tagging; (g) Named Entities Recognition; (q) Sair\n')

  if option == 'a':
    print('\n\nSEGMENTAÇÃO')

    print('texto original: ')
    print(first_text_to_parse)

    print('\ncódigo: nltk.tokenize.sent_tokenize(texto)')

    segments = nltk.tokenize.sent_tokenize(first_text_to_parse)
    print('\nlista de sentenças (segmentos): ')
    pprint(segments)
  elif option == 'b':
    print('\n\nTOKENIZAÇÃO')

    print('texto original: ')
    print(first_text_to_parse)

    print('\ncódigo: nltk.word_tokenize(texto)')

    tokens = nltk.word_tokenize(first_text_to_parse)
    print('\nlista de palavras (tokens): ')
    pprint(tokens)
  elif option == 'c':
    print('\n\nREMOÇÃO DE STOP WORDS')

    print('texto original: ')
    print(first_text_to_parse)

    tokens = nltk.word_tokenize(first_text_to_parse)
    print('\nlista de palavras (tokens): ')
    pprint(tokens)

    print('\ncódigo: stop_words = set(nltk.corpus.stopwords.words("english"))')
    print('        if not palavra in stop_words: (...)')

    filtered_tokens = []
    for i in range(len(tokens)):
      if not tokens[i] in stop_words:
        filtered_tokens.append(tokens[i])

    print('\nlista de palavras após remoção de stop words: ')
    pprint(filtered_tokens)
  elif option == 'd':
    print('\n\nSTEMMING')

    print('lista de palavras original: ')
    print(words_to_stem)

    print('\ncódigo: stemmer = nltk.stem.PorterStemmer()')
    print('        stemmer.stem(palavra)')

    stemmed_tokens = []
    for i in range(len(words_to_stem)):
      stemmed_tokens.append(stemmer.stem(words_to_stem[i]))

    print('\nlista de palavras após stemming: ')
    pprint(stemmed_tokens)
  elif option == 'e':
    print('\n\nLEMATIZAÇÃO')

    print('lista de palavras original: ')
    print(words_to_lemmatize)

    print('\ncódigo: lemmatizer = nltk.stem.WordNetLemmatizer()')
    print('        lemmatizer.lemmatize(palavra, pos="v")')

    lemmatized_tokens = []
    for i in range(len(words_to_lemmatize)):
      lemmatized_tokens.append(lemmatizer.lemmatize(words_to_lemmatize[i], pos="v"))
      
    print('\nlista de palavras após lematização: ')
    pprint(lemmatized_tokens)
  elif option == 'f':
    print('\n\nPOS TAGGING')

    print('texto original: ')
    print(text_with_named_entities)

    tokens = nltk.word_tokenize(text_with_named_entities)
    print('\nlista de palavras (tokens): ')
    pprint(tokens)

    print('\ncódigo: nltk.pos_tag(tokens)')

    tagged_tokens = nltk.pos_tag(tokens)
    print('\nlista de n-gramas dos tokens após marcação: ')
    pprint(tagged_tokens)
  elif option == 'g':
    print('\n\nNAMED ENTITIES RECOGNITION')
    
    print('texto original: ')
    print(text_with_named_entities)

    tokens = nltk.word_tokenize(text_with_named_entities)
    print('\nlista de palavras (tokens): ')
    pprint(tokens)

    tagged_tokens = nltk.pos_tag(tokens)
    print('\nlista de n-gramas dos tokens após marcação: ')
    pprint(tagged_tokens)

    print('\ncódigo: nltk.chunk.ne_chunk(tokens_com_tags)')

    entities = nltk.chunk.ne_chunk(tagged_tokens)
    print('\nlista hierárquica dos n-gramas dos tokens, e identificação de entidades: ')
    pprint(entities)
  elif option == 'q':
    break
  else:
    print('Opção inválida.')
