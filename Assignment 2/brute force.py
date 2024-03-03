import pandas as pd
import numpy as np
import time


# Function to calculate the score of a motif
def get_best_motif(motif):
    L = len(motif[0])
    T = len(motif)
    profile_matrix = np.zeros((4, L))   # 4*L matrix
    
    best_motif = ''
    best_score = 0
    # print(motif)

    for i in range(L):
        score = 0
        char = ''
        
        for j in range(T):
            # print(motif[j][i], end='')
            if motif[j][i].upper() == 'A':
                profile_matrix[0][i] += 1
            elif motif[j][i].upper() == 'C':
                profile_matrix[1][i] += 1
            elif motif[j][i].upper() == 'G':
                profile_matrix[2][i] += 1
            elif motif[j][i].upper() == 'T':
                profile_matrix[3][i] += 1
            
            if profile_matrix[0][i] > score:
                score = profile_matrix[0][i]
                char = 'A'
            elif profile_matrix[1][i] > score:
                score = profile_matrix[1][i]
                char = 'C'
            elif profile_matrix[2][i] > score:
                score = profile_matrix[2][i]
                char = 'G'
            elif profile_matrix[3][i] > score:
                score = profile_matrix[3][i]
                char = 'T'
        # print()
        best_motif += char
        best_score += score
                
    # print(profile_matrix)
    return best_motif, score


# Function to generate all possible motifs of length l
def generate_motifs(L, sequences):
    ''' Returns a dictonary of motifs for each sequence. '''
    motifs = {}
    for seq in sequences:
        motif_arr = []
        for i in range(len(seq) - L + 1):
            motif = seq[i:i+L]
            motif_arr.append(motif)
        motifs[seq] = motif_arr
    return motifs


# Main function to find the best motif
def find_best_motif(sequences, l_mer):
    motifs = generate_motifs(l_mer, sequences)
    print("Total Number Of Motifs:", len(motifs)*len(motifs[sequences[0]])) # It should be (N-L+1)*T => (40-6+1)*26 = 35*26 = 910.
    best_results = {}
    # motifs is a dictionary {seq: [motif1, motif2, ...]}
    for seq, motif in motifs.items():
        best_results[seq] = get_best_motif(motif)
        # break
    return best_results


start = time.time()
data = pd.read_csv('dna.csv', header=None)

# Convert the DNA sequences to a list.
sequences = data.values.flatten().tolist()

best_results = find_best_motif(sequences, 6)
end = time.time()

for seq, result in best_results.items():
    print("Best Motif for", seq, ":", result[0], "Score:", result[1])

print("Time taken:", end - start, "seconds")
