import sys
import os
import json
from tokenize.tokenizer import tokenize
from tokenize.vectorizer import vectorize
from cluster.clusterizer import clustering
import faiss
import numpy as np
class reactions_predicter():
    def __init__(self, posts):
        self.posts = posts
        self.tokenizer = tokenize()
        tokens = posts.apply(self.tokenizer.predict_with_set,axis = 1)
        self.vectorizer = vectorize()
        self.vectors = [self.vectorizer.predict(token) for token in tokens]
        self.clusterizer = clustering()
        self.clusterizer.fit(self.vectors)
        clusters = self.vectorizer.predict(self.vectors)
        self.vectors = np.hstack((np.array(self.vectors),clusters.reshape((-1,1))))
        settings_file = open(os.path.dirname(__file__) + '/../settings.json')
        settings = json.load(settings_file)
        index_filename = settings['index']['name']
        index_type = settings['index']['type']
        self.index = faiss.load_index(index_filename)
        self.num_neighbours = settings['index']['num_neighbours']
    def predict(self, text):
        _, indices = self.index.search(self.vectors, self.num_neighbours)
        reactions_percentage_dict = {}
        def fix(dictionary):
            sum = 0
            for key in dictionary:
                sum += dictionary[key]
            for key in dictionary:
                dictionary[key] /= sum

        for post in indices:
            reactions = post_with_reactions.iloc[post]['reactions']
            reactions = reactions.iloc[0].split(',')
            total_reactions = 0
            for reaction in reactions:
                cur_reaction = reaction[0]
                number = int(reaction[1:])
                total_reactions += number
            for reaction in reactions:
                cur_reaction = reaction[0]
                number = int(reaction[1:])
                if reaction not in reactions_percentage_dict:
                    reactions_percentage_dict[cur_reaction] = number / total_reactions
                else:
                    reactions_percentage_dict[cur_reaction] += number / total_reactions
            fix(reactions_percentage_dict)
        return reactions_percentage_dict