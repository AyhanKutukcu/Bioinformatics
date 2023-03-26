def read_fasta(file):
    sequences = {}
    current_sequence = ''
    with open(file) as f:
        for line in f:
            if line.startswith('>'):
                current_sequence = line.strip()[1:]
                sequences[current_sequence] = ''
            else:
                sequences[current_sequence] += line.strip()
    return sequences

def gc_content(sequence):
    gc_count = 0
    for base in sequence:
        if base in 'GC':
            gc_count += 1
    return gc_count / len(sequence) * 100

sequences = read_fasta('input.fasta')
gc_contents = {id: gc_content(sequence) for id, sequence in sequences.items()}
