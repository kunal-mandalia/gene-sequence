import fastq as fq

fos = fq.read("data/sample.fastq")
fos = list(fos)

def find_first_sequence(sequence):
    result = None

    for i in range(len(fos)):
        fo = fos[i]
        print(fo.getSeq())
        seq = fo.getSeq()
        if seq.find(sequence) > 0:
            result = fo
            break
    
    if result is None:
        print("unable to find sequence")
    
    return result

def find_all_sequences(sequence):
    result = list()

    for i in range(len(fos)):
        fo = fos[i]
        seq = fo.getSeq()
        if seq.find(sequence) >= 0:
            result.append(fo)
    
    return result

print(find_all_sequences("CAGTGGTAGCTGCTTAGTTTCATTTTATCGGTAGAAATTT"))
