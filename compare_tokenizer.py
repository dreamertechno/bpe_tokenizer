import time
from bpTokenizer import BPETokenizer

## Karşılaştırma için Hugging Face transformers kullanılacak
## Kullanıcının bilgisayarında yüklü olması gerekir: pip install transformers
try:
    from transformers import AutoTokenizer
    HAS_TRANSFORMERS = True
except ImportError:
    HAS_TRANSFORMERS = False

def main():
    metin = "Elektrikli araçlar geleceğin ulaşım sistemidir. Türkiye'nin enerji dönüşümü hızlanıyor."
    print("=== Tokenizer Karşılaştırması ===")
    print(f"Test Metni: {metin}\n")

    ## 1. Bizim Tokenizer
    print("--- 1. Kendi BPE Tokenizer'ımız ---")
    bizim_tokenizer = BPETokenizer(vocab_size=500)
    
    ## Küçük bir eğitim yapalım ki tokenları tanısın
    bizim_tokenizer.egit(metin, yazdir=False)
    
    start_time = time.time()
    bizim_ids = bizim_tokenizer.encode(metin)
    bizim_time = time.time() - start_time
    
    print(f"Token ID'leri: {bizim_ids}")
    print(f"Token Sayısı: {len(bizim_ids)}")
    print(f"Encode Süresi: {bizim_time:.6f} sn\n")

    ## 2. Hazır Tokenizer (Örn: BERT veya GPT-2)
    if HAS_TRANSFORMERS:
        print("--- 2. Hazır Tokenizer (dbmdz/bert-base-turkish-cased) ---")
        try:
            hf_tokenizer = AutoTokenizer.from_pretrained("dbmdz/bert-base-turkish-cased")
            
            start_time = time.time()
            hf_ids = hf_tokenizer.encode(metin, add_special_tokens=False)
            hf_time = time.time() - start_time
            
            hf_tokens = hf_tokenizer.convert_ids_to_tokens(hf_ids)
            
            print(f"Token ID'leri: {hf_ids}")
            print(f"Tokenlar: {hf_tokens}")
            print(f"Token Sayısı: {len(hf_ids)}")
            print(f"Encode Süresi: {hf_time:.6f} sn\n")
            
            ## Sonuç
            print("--- Sonuç ---")
            print("Hazır tokenizer, milyarlarca kelimeyle eğitildiği için kelimeleri çok daha bütüncül parçalara (subwords) böler.")
            print("Bizim tokenizer'ımız ise sadece verdiğimiz küçük corpus ile eğitildiğinden, kelimeleri daha küçük parçalara veya harflere bölebilir.")
            
        except Exception as e:
            print("Hazır tokenizer indirilirken veya çalışırken hata oluştu:", str(e))
    else:
        print("transformers kütüphanesi yüklü değil. Karşılaştırma için 'pip install transformers' komutunu çalıştırın.")

if __name__ == "__main__":
    main()
