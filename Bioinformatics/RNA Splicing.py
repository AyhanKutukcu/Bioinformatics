from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
from Bio import SeqIO

# Read the DNA sequence and introns from the input file
with open("input.txt") as f:
    sequences = SeqIO.parse(f, "fasta")
    dna = str(next(sequences).seq)
    introns = [str(record.seq) for record in sequences]

# Remove the introns from the DNA sequence
for intron in introns:
    dna = dna.replace(intron, "")

# Translate the DNA sequence to protein
protein = Seq(dna, generic_dna).translate(to_stop=True)

# Write the result to the output file
with open("output.txt", "w") as f:
    f.write(str(protein))
