import collections, re

def mostCommonWord(paragraph: str, banned: list[str]) -> str:
    words = [word for word in re.sub(r'[^\w]',' ', paragraph).lower().split() \
    if word not in banned] 
    
    # counts = collections.defaultdict(int)
    # for word in words: 
        # counts[word] += 1 

    # print(list(counts.get))
    # print(max(counts, key=counts.get))

    counts = collections.Counter(words)

    print(counts.most_common(2))
    return counts.most_common(1)[0][0]

mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"])