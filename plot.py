import numpy as np
import matplotlib.pyplot as plt


# Affichage graphique des points et des centroids
def plot(points, centroids):
    X = points[:, 0]
    Y = points[:, 1]
    clusters = points[:, 2]
    colors = np.zeros((len(centroids), 3))

    for i in range(len(centroids)):
        colors[i][0] = centroids[i][2]
        colors[i][1] = centroids[i][3]
        colors[i][2] = centroids[i][4]

    for j in range(len(X)):
        clust = int(clusters[j])
        color = [colors[clust][0], colors[clust][1], colors[clust][2]]
        plt.scatter(X[j], Y[j], color=color, marker='.', s=100)

    # plt.scatter(X, Y, color='red', marker='.')

    plt.scatter(centroids[:, 0], centroids[:, 1], color = 'green', marker='x', s=200)
    plt.show()
