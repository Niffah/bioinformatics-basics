def calculate_gc_content(dna_sequence):
    """
    Calculates the percentage of Guanine (G) and Cytosine (C) 
    bases in a given DNA sequence string.
    """
    # Convert sequence to uppercase to ensure accuracy
    dna_sequence = dna_sequence.upper()
    
    # Count the occurrences of G and C bases
    g_count = dna_sequence.count('G')
    c_count = dna_sequence.count('C')
    
    # Calculate the total length of the sequence
    total_length = len(dna_sequence)
    
    if total_length == 0:
        return 0.0
        
    # Calculate percentage
    gc_percentage = ((g_count + c_count) / total_length) * 100
    return round(gc_percentage, 2)

# Mock DNA sequence string representing an aging-related genetic marker
sample_dna = "ATGCGATCGATCGATCGATAGCGCGCATATATCGATAAACCCG"

# Execute and print results
gc_result = calculate_gc_content(sample_dna)
print(f"Analyzing DNA Sequence: {sample_dna}")
print(f"Sequence Length: {len(sample_dna)} bases")
print(f"Calculated GC-Content: {gc_result}%")

