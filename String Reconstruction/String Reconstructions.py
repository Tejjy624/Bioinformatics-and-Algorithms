
def cleandata(data):
    for line in data:
        line = line.strip()
    num = data[0]
    kmer = data[1:]
    return int(num), kmer

def findneighbors(k_num, kmer):
    totlen=k_num+len(kmer)-1
    final = kmer.pop(0)
    loc_kmer = list(kmer)
    for patterns in loc_kmer:
        if (len(final)==totlen):
            break
        else:
            if patterns[:(k_num-1)] == final[-(k_num-1):]:
                final = final + patterns[k_num-1]
                loc_kmer.remove(patterns)
            elif kmer[-(k_num-1):] == final[:(k_num-1)]:
                final = patterns[0] + final
                loc_kmer.remove(patterns)
    return final

with open("sample.txt","r") as file:
    edges = file.read().splitlines()
data = file.read().splitlines()
k_num, kmer = cleandata(data)
solution = findneighbors(k_num, kmer)
print(solution)