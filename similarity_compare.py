import numpy as np
from scipy.spatial import distance
from numpy.linalg import norm

from graph_to_matrices import txt_to_matrix

def calculate_similarity(A, B):
        # Euclidean Distance
        euclidean_dist = distance.euclidean(A.ravel(), B.ravel())

        # Frobenius Norm
        frobenius_norm = norm(A - B)

        return 0.5*(euclidean_dist + frobenius_norm)

def find_most_similar(visitor_link, museum_links: list[str]) ->str:
    matrix_visitor = txt_to_matrix(visitor_link)
    similarity = 0
    rec_link = museum_links[0]
    for museum_link in museum_links:
        matrix_museum = txt_to_matrix(museum_link)
        if similarity < calculate_similarity(matrix_visitor, matrix_museum):
            similarity = calculate_similarity(matrix_visitor, matrix_museum)
            rec_link = museum_link
    return rec_link

recommend_link = find_most_similar('D:/uofthack11/nostalgia/visitor_file.txt', ['D:/uofthack11/nostalgia/museum_file_eg.txt'])