# These file found ID from one file (only id) and matches them this ID from fasta file,
# to get new fasta file with only interesting sequences
query = []
with open("list_m", 'r') as l_m:  # ID_file
    for line in l_m:
        line2 = line.split()
        query.append(line2[0].rstrip())

set_q = set(query)

with open("augustus.whole.aa", 'r') as fasta:  # fasta_file
    for line in fasta:
        if '>' in line:
            if line.rstrip() in set_q:
                with open("prot_out", "a") as out:  # output_file
                    out.write(line + '\n')
                seq = next(fasta).rstrip()
                while seq.isalpha():
                    with open("prot_out", "a") as out:
                        out.write(seq + '\n')
                    seq = next(fasta).rstrip()
            else:
                pass
        else:
            pass
