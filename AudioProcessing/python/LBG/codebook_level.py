import numpy as np
import matplotlib.pyplot as plt

class codebook_level:
    def __init__(self, level, codebook, data, d_threshold):
        self.level = level
        self.codebook = codebook # vetor de valores
        self.iterations_counter = 0
        self.d_threshold = d_threshold

        cur_S = self.calculate_S(data)

        while True:
            self.make_one_more_iteration(data, cur_S)
            new_S = self.calculate_S(data)
            if self.is_sufficient(data, cur_S, new_S):
                break
            cur_S = new_S

    def get_level(self):
        return self.level
    
    def get_codebook(self):
        return self.codebook
    
    def set_codebook(self, codebook):
        self.codebook = codebook

    def make_one_more_iteration(self, data, S):
        self.iterations_counter+=1

        new_codebook = np.zeros_like(self.codebook)
        for i in range(len(self.codebook)):
            indexes = np.where(S == i)
            new_codebook[i] = np.mean(data[indexes], axis=0)
        
        self.set_codebook(new_codebook)


    def calculate_dist(self, a, b):
        return np.linalg.norm(a-b)
    
    def find_min_dist(self, a):
        dists = np.linalg.norm(self.codebook - a, axis=1)
        min_index = np.argmin(dists)
        min_dist = dists[min_index]
        return min_dist, min_index

    def calculate_S(self, data):
        S = np.zeros(len(data), dtype=int)
        for i, datum in enumerate(data):
            _, min_index = self.find_min_dist(datum)
            S[i] = min_index
        
        self.S = S
        return S

    def is_sufficient(self, data, S, new_S):
        D_p = self.calculate_distortion(data, S)
        D_p1 = self.calculate_distortion(data, new_S)
        d = (D_p - D_p1) / D_p 
        print()
        print("iterations_counter", self.iterations_counter)
        print("D_p", D_p)
        print("D_p1", D_p1)
        print("d", d)

        return d < self.d_threshold
        
    def calculate_distortion(self, data, S):
        # Vectorized calculation for improved performance
        codebook_vectors = self.codebook[S]
        distortions = np.linalg.norm(data - codebook_vectors, axis=1)
        return np.mean(distortions)
    
    def plot(self, data):
        S = self.S
        plt.scatter(data[:,0], data[:,1], c=S, s=1)
        plt.scatter(self.codebook[:,0], self.codebook[:,1], c='red')
        plt.show()

    def plot_custom_ax(self, data, ax):
        S = self.S  
        ax.scatter(data[:,0], data[:,1], c=S, s=1)
        ax.scatter(self.codebook[:,0], self.codebook[:,1], c='red')
        return ax
