#!/usr/bin/env python3

def ngram_bleu(references, sentence, n):
    """
    Calculates the n-gram BLEU score for a sentence
    """
    import math

    # Length of candidate sentence
    c = len(sentence)

    # Closest reference length
    ref_lens = [len(ref) for ref in references]
    r = min(ref_lens, key=lambda ref_len: (abs(ref_len - c), ref_len))

    # Brevity penalty
    if c > r:
        BP = 1
    else:
        BP = math.exp(1 - r / c)

    # Helper: extract n-grams from a sequence
    def get_ngrams(seq, n):
        return [tuple(seq[i:i+n]) for i in range(len(seq) - n + 1)]

    # Candidate n-grams
    cand_ngrams = get_ngrams(sentence, n)
    cand_counts = {}
    for ng in cand_ngrams:
        cand_counts[ng] = cand_counts.get(ng, 0) + 1

    # Reference max counts
    max_ref_counts = {}
    for ref in references:
        ref_ngrams = get_ngrams(ref, n)
        ref_counts = {}
        for ng in ref_ngrams:
            ref_counts[ng] = ref_counts.get(ng, 0) + 1
        for ng, count in ref_counts.items():
            max_ref_counts[ng] = max(max_ref_counts.get(ng, 0), count)

    # Clipped precision
    clipped_count = 0
    total_count = 0
    for ng, count in cand_counts.items():
        clipped_count += min(count, max_ref_counts.get(ng, 0))
        total_count += count

    precision = clipped_count / total_count if total_count > 0 else 0

    # BLEU score
    bleu = BP * precision
    return bleu
