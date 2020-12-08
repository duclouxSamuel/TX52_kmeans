import tsplib95
import numpy as np
import k_means


#Paramètres globaux : nom du fichier et k
file_name = "dj38.tsp"
k = 3
global list_of_cities

#Convertir un fichier tsp en matrice de poids/distances
def file2weights(file_name):
    problem = tsplib95.load(file_name)
    list_of_nodes = list(problem.get_nodes())
    size = len(list_of_nodes)
    nodes = np.zeros((size, 2))
    weights = np.zeros((size, size))
    for i in list_of_nodes:
        nodes[i-1] = problem.get_display(i)
        for j in list_of_nodes:
            edge = i, j
            # print(problem.get_weight(*edge))
            weights[i - 1][j - 1] = problem.get_weight(*edge)
    #print("weight matrix is : {}",weights)
    print(nodes)
    return list_of_nodes, size, weights


X, Y, centroids = k_means.initialise(k, file_name)
k_means.k_means(k, X, Y, centroids)


#plot.plot(X, Y, centroids)
