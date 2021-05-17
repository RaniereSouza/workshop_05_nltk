from pprint import pprint
import nltk

nltk.download() #de preferência criar uma maneira de rodar só uma vez

text = """Did you know that The Rock and Dwayne Johnson are the same person?
          I certainly didn't.
          Also, you've never seen Childish Gambino and Donald Glover at the same place, right?
          It makes me wonder..."""

segments = nltk.tokenize.sent_tokenize(text)

print('\nSEGMENTAÇÃO')
pprint(segments)

tokens = []
filtered_tokens = []
stemmed_tokens = []
lemmatized_tokens = []
tagged_tokens = []
entities = []

stop_words = set(nltk.corpus.stopwords.words('english'))
stemmer = nltk.stem.PorterStemmer()
lemmatizer = nltk.stem.WordNetLemmatizer()

for i in range(len(segments)):
  tokens.append(nltk.word_tokenize(segments[i]))

  filtered_tokens.append([])
  stemmed_tokens.append([])
  lemmatized_tokens.append([])

  for j in range(len(tokens[i])):
    if tokens[i][j] not in stop_words:
      filtered_tokens[i].append(tokens[i][j])
  
  for j in range(len(tokens[i])):
    stemmed_tokens[i].append(stemmer.stem(tokens[i][j]))
    lemmatized_tokens[i].append(lemmatizer.lemmatize(tokens[i][j], pos="v"))

  tagged_tokens.append(nltk.pos_tag(tokens[i]))
  entities.append(nltk.chunk.ne_chunk(tagged_tokens[i]))

print('\nTOKENIZAÇÃO')
pprint(tokens)
print('\nREMOÇÃO DE STOP WORDS')
pprint(filtered_tokens)
print('\nSTEMMING')
pprint(stemmed_tokens)
print('\nLEMATIZAÇÃO')
pprint(lemmatized_tokens)
print('\nPOS TAGGING')
pprint(tagged_tokens)
print('\nNAMED ENTITIES RECOGNITION')
pprint(entities)

