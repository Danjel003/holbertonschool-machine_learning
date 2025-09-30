```python
#!/usr/bin/env python3
"""
Text
"""
import math
from collections import Counter


def uni_bleu(references, sentence):
    """
    Calculates the unigram BLEU score for a sentence
    """
    # Candidate sentence length
    cand_len = len(sentence)

    # Get reference lengths
    ref_lens = [len(ref) for ref in references]

    # Find closest reference length
    closest_ref_len = min(
        ref_lens,
        key=lambda ref_len: (abs(ref_len - cand_len), ref_len)
    )

    # Brevity penalty
    if cand_len > closest_ref_len:
        BP = 1
    else:
        BP = math.exp(1 - closest_ref_len / cand_len)

    # Count unigrams in candidate
    cand_counts = Counter(sentence)

    # Compute clipped counts
    clipped_count = 0
    total_count = sum(cand_counts.values())

    for word, count in cand_counts.items():
        max_ref_count = max(ref.count(word) for ref in references)
        clipped_count += min(count, max_ref_count)

    precision = clipped_count / total_count if total_count > 0 else 0

    # BLEU score
    return BP * precision
