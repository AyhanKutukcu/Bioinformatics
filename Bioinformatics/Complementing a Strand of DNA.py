def reverse_complement(dna_string):
    complement_dict = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    complement = [complement_dict[base] for base in dna_string[::-1]]
    return ''.join(complement)
