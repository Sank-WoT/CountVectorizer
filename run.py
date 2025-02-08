import re

#псевдокод
#1. привести к нижнему регистру
#2. убрать знаки препинания
#3. разделить на слова
#4. составить словарь

#траансформация
#1. посчитать количество документов
#2. посчитать количество термов
#3. составить матрицу
#4. предобработать каждый документ
#5. заполнить матрицу

class CountVectorizer:
  def __init__(self):
    self.vocabulary = {}
    self.document_frequency = {}

  def fit(self, documents):
    self.documents = documents
    tokens = []

    for i, doc in enumerate(documents):
      doc = doc.lower()
      doc = re.sub(r'[^\w\s]', '', doc)
      tokens.extend(doc.split())
      self.vocabulary = {token: i for i, token in enumerate(sorted(list(set(tokens))))}

  def transform(self, documents):
      num_docs = len(documents)
      num_terms = len(self.vocabulary)
      matrix = [[0] * num_terms for _ in range(num_docs)]

      for i, doc in enumerate(documents):
        doc = doc.lower() 
        doc = re.sub(r'[^\w\s]', '', doc)

        for token in doc.split():
          if token in self.vocabulary:
            term_index = self.vocabulary[token]
            matrix[i][term_index] += 1
      
      return matrix

documents = [
    "This is the first document.",
    "This document is the second document.",
    "And this is the third one.",
    "Is this the first document?"
]

vectorizer = CountVectorizer()
vectorizer.fit(documents)
term_document_matrix = vectorizer.transform(documents)
print(term_document_matrix)
