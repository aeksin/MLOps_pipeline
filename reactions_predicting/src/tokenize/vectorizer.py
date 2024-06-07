import json
import os
import numpy as np
from gensim.models.doc2vec import Doc2Vec, Word2Vec

class vectorize:
    def __init__(self):
        settings_file = open(os.path.dirname(__file__) + '/../settings.json')
        settings = json.load(settings_file)
        model_file = settings['vectorizer']['name']
        self.model_path = open(os.path.dirname(__file__) + f'/../../models/{model_file}')
        self.model_type = settings['vectorizer']['type']
        if (self.model_type == 'doc2vec'):
            self.model = Doc2Vec.load(self.model_path)
            self.vectorizer = self.model.infer_vector
        elif (self.model_type == 'word2vec'):
            self.model = Word2Vec.load(self.model_path)
            self.vectorizer = self.model.wv.get_vector
    def predict(self, text):
        return self.vectorizer(text)