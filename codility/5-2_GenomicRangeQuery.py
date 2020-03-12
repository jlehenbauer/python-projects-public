def solution(S, P, Q):
    dna_dict = {"A": 1, "C": 2, "G": 3, "T": 4}
    known_dict = {}
    impacts = []
    for i in range(len(P)):
        min_impact = 5
        if (P[i], Q[i]) in known_dict.keys():
            min_impact = known_dict[(P[i], Q[i])]
        else:
            for nucleotide in S[P[i]:Q[i]+1]:
                if dna_dict[nucleotide] < min_impact:
                    min_impact = dna_dict[nucleotide]
                    if min_impact == 1:
                        break
        known_dict[(P[i], Q[i])] = min_impact
        impacts.append(min_impact)
    return impacts