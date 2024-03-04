import pandas as pd
import numpy as np
import time


# Function to calculate the score of a motif
def get_best_motif(profile_matrix):
    best_motif = ""
    best_score = 0
    print(f"Profile Matrix Dimension: ({profile_matrix.shape[0]}, {profile_matrix.shape[1]})")
    for pos in range(profile_matrix.shape[1]):
        seq = ""
        score = -1
        for char in range(profile_matrix.shape[0]):
            if profile_matrix[char][pos] > score:
                score = profile_matrix[char][pos]
                if char == 0:
                    seq = 'A'
                elif char == 1:
                    seq = 'C'
                elif char == 2:
                    seq = 'G'
                elif char == 3:
                    seq = 'T'
        best_motif += seq
        best_score += score
    return best_motif, best_score


def generate_profile_matrix(motifs):
    T = len(motifs)
    L_mer = len(motifs[0])
    profile_matrix = np.zeros((4, L_mer))   # 4*L matrix
    for i in range(L_mer):
        for j in range(T):
            if motifs[j][i].lower() == 'a':
                profile_matrix[0][i] += 1
            elif motifs[j][i].lower() == 'c':
                profile_matrix[1][i] += 1
            elif motifs[j][i].lower() == 'g':
                profile_matrix[2][i] += 1
            elif motifs[j][i].lower() == 't':
                profile_matrix[3][i] += 1
    return profile_matrix


def generate_motifs(L, sequences):
    # motifs is a list of all possible motifs
    motifs = []
    for seq in sequences:
        for i in range(len(seq) - L + 1):
            motifs.append(seq[i:i+L])
    
    return motifs


# Main function to find the best motif
def find_best_motif(sequences, l_mer):
    motifs = generate_motifs(l_mer, sequences)
    print("Total Number Of Motifs:", len(motifs)) # It should be (N-L+1)*T => (40-6+1)*26 = 35*26 = 910.
    
    profile_matrix = generate_profile_matrix(motifs)
    print(profile_matrix)
    best_motif, best_score = get_best_motif(profile_matrix)

    return best_motif, best_score



if __name__ == "__main__":
    start = time.time()
    data = pd.read_csv('Assignment 2/dna.csv', header=None)

    # Convert the DNA sequences to a list.
    sequences = data.values.flatten().tolist()
    best_results = find_best_motif(sequences, 6)
    end = time.time()

    print("Best Motif:", best_results[0])
    print("Best Score:", best_results[1])

    print("Time taken:", end - start, "seconds")
