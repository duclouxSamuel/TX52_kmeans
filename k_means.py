import random
import tsplib95
import numpy as np
from math import sqrt
import plot


#Calcul de la distance entre un point et un centroid
def distance(point, centroid):
    X = point[0] - centroid[0]
    Y = point[1] - centroid[1]
    dist = sqrt(X*X + Y*Y)
    return dist

#Calcul les nouvelles coordonnées des centroids avec un calcul de la moyenne
def compute_centroids(points, centroids):
    for i in range(len(centroids)):
        sum_x =0
        sum_y =0
        n_points = 0
        for j in range(len(points)):
            if(points[j][2]) == i:
                n_points+=1
                sum_x+=points[j][0]
                sum_y+=points[j][1]
        centroids[i][0] = sum_x/n_points
        centroids[i][1] = sum_y/n_points
    return centroids


#Algorithme des K-means
#k : nombre de clusters choisis
#X et Y : coordonnées des points
#centroids : coordonnées des centroids
def k_means(k, X, Y, centroids):

    points = np.zeros((len(X),3))
    points[:, 0] = X
    points[:, 1] = Y

    counter = 0

    # Boucle générale (répéter tant que les centroids changent de position)
    while True:
        counter += 1
        print("Iteration",counter)
        # Calcul du centroid le plus proche pour chaque point
        for point in points:
            current_point = point
            distance_min = distance(current_point, centroids[0])
            cluster = 0

            # Calcul du centroid le plus proche pour le point en question
            for j in range(len(centroids)):
                dist = distance(current_point, centroids[j])
                if dist < distance_min:
                    distance_min = dist
                    cluster = j

            point[2] = cluster
        prev_centroids = centroids
        print(points[:,2])
        centroids = compute_centroids(points,centroids)
        print(prev_centroids.all == centroids.all)

        if (prev_centroids.all == centroids.all):
            break
    plot.plot(points, centroids)


#Récupère les coordonnées du fichier et initialise les centroids
def initialise(k, file_name):
    problem = tsplib95.load(file_name)
    dimension = problem.dimension
    X = []
    Y = []
    for i in range(dimension):
        X.append(problem.node_coords[i+1][0])
        Y.append(problem.node_coords[i+1][1])

    centroids = np.zeros((k, 5))
    size = len(X)

    point = random.sample(range(size), k)
    j = 0
    for i in point:
        centroids[j][0] = X[i]
        centroids[j][1] = Y[i]


        r = random.random()
        g = random.random()
        b = random.random()
        centroids[j][2] = r
        centroids[j][3] = g
        centroids[j][4] = b
        j = j + 1

    return X, Y, centroids
