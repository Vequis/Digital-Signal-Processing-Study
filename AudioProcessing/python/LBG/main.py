import numpy as np
import matplotlib.pyplot as plt
# from sklearn.cluster import KMeans
from codebook_level import codebook_level
from codebook_tree import codebook_tree

central_points = [(0, 0), (0, 1), (1, 0), (1, 1)]
correct_centers = np.zeros(10000)
def generate_data(n, central_points):
    cp = np.array(central_points)
    chosen_indices = np.random.choice(len(central_points), n)
    centers = cp[chosen_indices]
    noise = np.random.normal(0, 0.25, centers.shape)

    np.copyto(correct_centers, chosen_indices)
    return centers + noise
data = generate_data(10000, central_points)

# codebook_level = codebook_level(level=2, codebook=[(-0.5, -0.1), (0.1, 0.7), (0.6, 0.5), (0.9, 0.7)], data=data, d_threshold=0.000001)
# print("Codebook:", codebook_level.get_codebook())
# print("Level:", codebook_level.get_level())
# print("Iterations Counter:", codebook_level.iterations_counter)
# print("Distortion:", codebook_level.calculate_distortion(data, codebook_level.S))
# print("Number of errors:", len(np.where(codebook_level.S - correct_centers != 0)[0]))
# codebook_level.plot(data)


codebook_tree = codebook_tree(data, d_threshold=0.000001)
codebook_tree.construct_next_level()
codebook_tree.construct_next_level()
codebook_tree.construct_next_level()

levels = codebook_tree.get_levels()
fig, axs = plt.subplots(2, 2, figsize=(10, 5))
for i in range(len(levels)):
    print("Level: ", i)
    print("Codebook:")
    print(levels[i].get_codebook())

    levels[i].plot_custom_ax(data, axs[i//2, i%2])

codebook_tree.plot(data)
fig.tight_layout()
plt.show()

# print("Levels:", codebook_tree.get_levels().get_codebook())
