from Bio import SeqIO

def gc_content(dna):
    """Verilen DNA dizisinin GC içeriğini hesaplar."""
    gc_count = dna.count("G") + dna.count("C")
    return (gc_count / len(dna)) * 100

# FASTA dosyasını aç ve verileri oku
records = list(SeqIO.parse("filename.fasta", "fasta"))

max_gc_id = ""
max_gc_content = 0

# Her bir DNA dizisi için GC içeriğini hesapla
for record in records:
    dna = str(record.seq)
    gc = gc_content(dna)

    # Eğer bu dizinin GC içeriği daha önceki dizilerden daha büyükse,
    # bu diziyi en yüksek GC içeriğine sahip dizi olarak kaydet.
    if gc > max_gc_content:
        max_gc_id = record.id
        max_gc_content = gc

print(max_gc_id)
print("%.6f" % max_gc_content)
