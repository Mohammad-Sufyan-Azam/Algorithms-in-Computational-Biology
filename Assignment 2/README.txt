ACB Assignment 2


We have implemented the Brute Force Algorithm using a class called Motifs() for handling all the processing steps and generating the best motif and its score. The code has been well commented in order to understand each function’s behavior. 


> Requirements -


Step 1) In order to run the code, python and pip must be installed. You can visit their official websites and download them.
Step 2) Then using pip, libraries like numpy pandas, and time must be installed. The command for installing the libraries would be -
‘pip install numpy’
‘pip install pandas’
‘pip install time’
Step 3) Install any IDE that support .ipynb format (eg., VSCode, Jupyter Notebook) and open the code in that IDE. Then run each of the cells one-by-one.
OR
Convert the .ipynb to .py format using any online converter websites/tools (eg., https://www.vertopal.com/en/convert/ipynb). Then open a terminal (or command prompt, powershell, bash depending on your OS) and run the file using python. The command for running it would be -
‘python FILE_NAME.py’         OR
‘python3 FILE_NAME.py’ depending on which python version you have installed. Instead of the FILE_NAME write the actual name of the file in the command.



> Workflow - 


1. Initialization: We read all the DNA sequences from the dna.csv file and provide it into the Motifs class in the form of a list along with the length of I-mer. The class stores them into its own variables.
2. Motif Generation: The `generate_motifs` method generates all possible motifs of the specified length (I-mer) from all DNA sequences given to it.
3. Profile Matrix Creation: The `generate_profile_matrix` method creates a profile matrix from the generated motifs. The profile matrix represents the frequency of each nucleotide (i.e., AGTC) at each position in the motifs.
4. Best Motif Selection: The `get_best_motif` method determines the best motif based on the profile matrix. It selects the nucleotide with the highest frequency at each position to form the best motif.
5. Finding the Best Motif: The `find_best_motif` method combines the above steps to find the best motif within the DNA sequence. It prints the total number of motifs generated, the profile matrix, the best motif, and its score.
6. Execution Time: The program also calculates and prints the execution time of the algorithm.



> Input and Output -


Input: The program expects a CSV file containing all the DNA sequences.
Output: The program outputs the total number of motifs created, its profile matrix, and the best motif found along with its score. It also prints the execution time of the algorithm.



> Result -

Best Motif: GGGGGG
Best Score: 1620
Execution TIme of the Algorithm: 0.01 sec
