
def minimum_skew(genome):
    diff = 0
    skew = []
    for i, c in enumerate(genome):
        if c == 'G':
            diff += 1
        if c == 'C':
            diff -= 1
        skew.append(diff)
    m = min(skew)
    answers = []
    for i, d in enumerate(skew):
        if d == m:
            answers.append(i + 1)
    return answers

with open('rosalind_ba1f.txt') as txt_file:
    genome = txt_file.readline()
    print(minimum_skew(genome))

#print(minimum_skew('CCTATCGGTGGATTAGCATGTCCCTGTACGTTTCGCCGCGAACTAGTTCACACGGCTTGATGGCAAATGGTTTTTCCGGCGACCGTAATCGTCCACCGAG'))
