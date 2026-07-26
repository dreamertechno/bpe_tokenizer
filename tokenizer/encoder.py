import re

def encode_word(word: str, merges: dict) -> list:
    ## Kelimeyi karakterlerine ayırıp en uygun birleştirmeleri uygula
    tokens = list(word)
    while len(tokens) > 1:
        pairs = [(tokens[i], tokens[i+1]) for i in range(len(tokens)-1)]
        ## Hangi çift ilk birleşmeli? merges dict'teki sıraya göre veya varlığına göre
        best_pair = None
        for pair in pairs:
            if pair in merges:
                best_pair = pair
                break
                
        if not best_pair:
            break
            
        ## best_pair'i birleştir
        new_tokens = []
        i = 0
        while i < len(tokens):
            if i < len(tokens) - 1 and (tokens[i], tokens[i+1]) == best_pair:
                new_tokens.append(best_pair[0] + best_pair[1])
                i += 2
            else:
                new_tokens.append(tokens[i])
                i += 1
        tokens = new_tokens
        
    return tokens

def encode_text(words: list, merges: dict, token_to_id: dict, unk_id: int) -> list:
    ## Metni ID listesine çevir
    ids = []
    for word in words:
        tokens = encode_word(word, merges)
        for token in tokens:
            ids.append(token_to_id.get(token, unk_id))
    return ids

def decode_ids(ids: list, id_to_token: dict) -> str:
    ## ID listesini okunabilir metne çevir
    text = ""
    for token_id in ids:
        token = id_to_token.get(token_id, "<UNK>")
        text += token
    return text
