def solution(S, P, Q):
    dna_dict = {"A": 1, "C": 2, "G": 3, "T": 4}
    impacts = []
    for i in range(len(P)):
        min_impact = 5
        for nucleotide in S[P[i]:Q[i]+1]:
            if dna_dict[nucleotide] < min_impact:
                min_impact = dna_dict[nucleotide]
                if min_impact == 1:
                    break
        impacts.append(min_impact)
    return impacts