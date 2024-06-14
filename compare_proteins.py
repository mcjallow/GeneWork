import os

def read_protein_sequence(file_path, start_line):
    """
    Reads a protein sequence from a file starting from a specified line.
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Extract sequence lines starting from the specified line
    sequence_lines = [line.strip() for line in lines[start_line-1:]]
    
    # Print the sequence lines for debugging
    file_name = os.path.basename(file_path)
    
    # Join all lines to form the full sequence
    sequence = ''.join(sequence_lines)
    return sequence

def compare_sequences(seq1, seq2):
    """
    Compares two protein sequences and returns True if they are the same, False otherwise.
    """
    return seq1 == seq2

def delete_file(file_path):
    """
    Deletes the specified file.
    """
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"File {file_path} has been deleted.")
    else:
        print(f"File {file_path} does not exist.")

# Directory paths
dataset1_dir = r"C:\Users\mcjal\OneDrive\Documents\python\DS1"
dataset2_dir = r"C:\Users\mcjal\OneDrive\Documents\python\DS2"

# Iterate through all files in dataset 1
for file1_name in os.listdir(dataset1_dir):
    file1_path = os.path.join(dataset1_dir, file1_name)
    sequence1 = read_protein_sequence(file1_path, start_line=2)  # Start from line 1 for dataset 1
    
    # Iterate through all files in dataset 2
    for file2_name in os.listdir(dataset2_dir):
        file2_path = os.path.join(dataset2_dir, file2_name)
        sequence2 = read_protein_sequence(file2_path, start_line=4)  # Start from line 4 for dataset 2
        
        # Compare sequences
        if compare_sequences(sequence1, sequence2):
            print(f"Sequences in {file1_name} and {file2_name} are the same. Deleting {file2_name}.")
            delete_file(file2_path)
        else:
            print(f"Sequences in {file1_name} and {file2_name} are different. No changes made.")
