import os
import time
from tokenizer import normalize_text, split_to_words, train_bpe, encode_word, save_json, load_json, save_merges, load_merges

class BPETokenizer:
    def __init__(self, vocab_size: int = 250):
        self.vocab_size = vocab_size
        self.merges = {}
        self.vocab = {}
        self.token_to_id = {}
        self.id_to_token = {}
        self.special_tokens = {"<UNK>": 0, "<PAD>": 1, "<BOS>": 2, "<EOS>": 3}
        self.unk_id = 0
        
    def egit(self, corpus: str, yazdir: bool = False):
        ## Eğitimi başlat
        start_time = time.time()
        
        ## 1. Ön işleme
        corpus = normalize_text(corpus, lowercase=True)
        words = split_to_words(corpus)
        
        ## 2. BPE Eğitimi
        self.merges, tokens = train_bpe(words, self.vocab_size)
        
        ## 3. ID Atama (Özel tokenlar + öğrenilen tokenlar)
        self.token_to_id = self.special_tokens.copy()
        current_id = len(self.special_tokens)
        
        for token in tokens:
            if token not in self.token_to_id:
                self.token_to_id[token] = current_id
                current_id += 1
                
        self.id_to_token = {v: k for k, v in self.token_to_id.items()}
        self.vocab = {k: 1 for k in self.token_to_id.keys()} ## Sadece varlığını tutuyoruz
        
        end_time = time.time()
        
        ## 4. İstatistik yazdırma
        if yazdir:
            print("=== İstatistikler ===")
            print(f"Toplam eğitim kelimesi: {len(words)}")
            print(f"Toplam benzersiz kelime: {len(set(words))}")
            print(f"Sözlük büyüklüğü: {len(self.token_to_id)}")
            print(f"Yapılan BPE birleştirme sayısı: {len(self.merges)}")
            print(f"Eğitim süresi: {end_time - start_time:.2f} saniye")
            
    def encode(self, text: str) -> list:
        ## Metni id listesine çevir
        text = normalize_text(text, lowercase=True)
        words = split_to_words(text)
        
        ids = []
        for word in words:
            tokens = encode_word(word, self.merges)
            for token in tokens:
                ids.append(self.token_to_id.get(token, self.unk_id))
        return ids
        
    def decode(self, ids: list) -> str:
        ## ID'leri tekrar metne çevir
        text = ""
        for i, token_id in enumerate(ids):
            token = self.id_to_token.get(token_id, "<UNK>")
            ## Özel karakter değilse ve önceki kelimenin parçası değilse boşluk ekle
            ## Şimdilik basitçe birleştiriyoruz
            text += token
        return text

    def jason_kaydet(self, dir_path: str):
        ## Tüm veriyi kaydet
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
            
        save_json(self.token_to_id, os.path.join(dir_path, "vocab.json"))
        save_merges(self.merges, os.path.join(dir_path, "merges.json"))
        
        config = {"vocab_size": self.vocab_size}
        save_json(config, os.path.join(dir_path, "config.json"))

    def jason_yukle(self, dir_path: str):
        ## Dosyadan verileri yükle
        self.token_to_id = load_json(os.path.join(dir_path, "vocab.json"))
        self.id_to_token = {v: k for k, v in self.token_to_id.items()}
        self.merges = load_merges(os.path.join(dir_path, "merges.json"))
        
        config = load_json(os.path.join(dir_path, "config.json"))
        if "vocab_size" in config:
            self.vocab_size = config["vocab_size"]
