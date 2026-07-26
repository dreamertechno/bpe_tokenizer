import re
from collections import defaultdict

def get_stats(vocab: dict) -> dict:
    ## İkili karakter çiftlerinin frekanslarını hesaplar
    pairs = defaultdict(int)
    for word, freq in vocab.items():
        symbols = word.split()
        for i in range(len(symbols) - 1):
            pairs[symbols[i], symbols[i+1]] += freq
    return pairs

def merge_vocab(pair: tuple, v_in: dict) -> dict:
    ## En sık geçen çifti birleştir
    v_out = {}
    bigram = re.escape(' '.join(pair))
    p = re.compile(r'(?<!\S)' + bigram + r'(?!\S)')
    for word in v_in:
        w_out = p.sub(''.join(pair), word)
        v_out[w_out] = v_in[word]
    return v_out

def train_bpe(words: list, vocab_size: int):
    ## BPE algoritmasını çalıştır
    vocab = defaultdict(int)
    
    ## Kelimeleri harflerine ayır
    for word in words:
        vocab[' '.join(list(word))] += 1

    merges = {}
    tokens = set()
    for word in vocab.keys():
        for token in word.split():
            tokens.add(token)

    num_merges = vocab_size - len(tokens) - 4 ## Özel tokenlar hariç
    if num_merges < 0:
        num_merges = 0

    import re
    for i in range(num_merges):
        pairs = get_stats(vocab)
        if not pairs:
            break
            
        best = max(pairs, key=pairs.get)
        vocab = merge_vocab(best, vocab)
        merges[best] = best[0] + best[1]
        
    ## Son sözlüğü oluştur
    final_tokens = set()
    for word in vocab.keys():
        for token in word.split():
            final_tokens.add(token)
            
    return merges, final_tokens
