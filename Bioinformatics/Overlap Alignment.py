from Bio import SeqIO
from Bio import pairwise2

# Read in the sequences from the FASTA file
records = list(SeqIO.parse("input.fasta", "fasta"))
s, t = str(records[0].seq), str(records[1].seq)

# Define the scoring matrix and gap penalty
match_score = 1
mismatch_score = -2
gap_penalty = -2
scoring_matrix = pairwise2.MatrixInfo.blosum62

# Find the best overlap alignment
best_score = float("-inf")
best_alignment = None
for i in range(1, len(s) + 1):
    alignment = pairwise2.align.localds(s[i:], t, scoring_matrix, gap_penalty, gap_penalty, score_only=False, one_alignment_only=True)
    score = alignment[0].score
    if score > best_score:
        best_score = score
        best_alignment = alignment

# Print the results
print(best_score)
print(best_alignment[0].seq)
print(best_alignment[1].seq)
