# coding: utf8
from words import read, alphabet
all_words = set(read())
start = u'муха'
end = u'слон'
unknown_words = [u'сури', u'сура', u'сири', u'мири']

derived_from = {}

def is_word(string):
  return string in all_words

def next_set(words):
  return set.union(*map(next_words, words))

def next_words(word):
  return set(variation for variation in variations(word) if is_word(variation))

def variations(word):
  for letter in alphabet:
    for position in range(len(word)):
      variation = word[0:position] + letter + word[position+1:]
      if word != variation and not derived_from.get(variation) and not variation in unknown_words:
        derived_from[variation] = word
        yield variation

words = set([start])
while True:
  words = next_set(words)
  if end in words:
    word = end
    print word
    while word != start:
      word = derived_from[word]
      print word
    break
