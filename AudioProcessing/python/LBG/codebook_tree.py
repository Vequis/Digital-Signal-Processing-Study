from codebook_level import codebook_level
import numpy as np
import matplotlib.pyplot as plt

class codebook_tree:
    def __init__(self, data, d_threshold):
        self.data = data
        self.d_threshold = d_threshold
        self.levels = []
        self.iterations_counter = 0
        self.build_tree()
    
    def build_tree(self):
        mean_point = self.data.mean(axis=0)
        # print("Column Means:", mean_point)
        self.levels.append(codebook_level(level=0, codebook=[mean_point], data=self.data, d_threshold=self.d_threshold))
    
    def construct_next_level(self):
        new_codebook = self.generate_new_codebook()
        print("New Codebook:", new_codebook)

        self.levels.append(codebook_level(level=self.levels[-1].get_level()+1, codebook=new_codebook, data=self.data, d_threshold=self.d_threshold))
        print("Level:", self.levels[-1].get_level())

    def generate_new_codebook(self):
        old_codebook = self.levels[-1].get_codebook()
        new_codebook = np.zeros((len(old_codebook)*2, old_codebook.shape[1]))
        random_vector = np.random.rand(old_codebook.shape[1])
        random_vector = random_vector / np.linalg.norm(random_vector)

        for i in range(len(old_codebook)):
            new_codebook[2*i] = old_codebook[i] - random_vector
            new_codebook[2*i+1] = old_codebook[i] + random_vector

        return new_codebook

    def get_levels(self):
        return self.levels
    
    def plot(self, data):
        plt.scatter(data[:, 0], data[:, 1], c=self.levels[-1].S, s=1)
        plt.scatter(self.levels[-1].get_codebook()[:, 0], self.levels[-1].get_codebook()[:, 1], c='red', s=10)
        plt.show()