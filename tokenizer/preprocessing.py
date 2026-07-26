import re

## Türkçe karakter eşleştirmeleri
TR_LOWER = "abcçdefgğhıijklmnoöprsştuüvyz"
TR_UPPER = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"

def to_lower(text: str) -> str:
    ## İ'leri i'ye çevirip kalanları standart lower yapıyoruz. I'ları da ı'ya.
    text = text.replace("İ", "i").replace("I", "ı")
    return text.lower()

def to_upper(text: str) -> str:
    ## i'leri İ'ye çevirip kalanları standart upper yapıyoruz.
    text = text.replace("i", "İ").replace("ı", "I")
    return text.upper()

def normalize_text(text: str, lowercase: bool = False) -> str:
    ## Boşlukları ve satır sonlarını temizle
    text = re.sub(r'\s+', ' ', text).strip()
    if lowercase:
        text = to_lower(text)
    return text

def english_char_convert(text: str) -> str:
    ## Türkçe'ye özel karakterleri koruyup geri kalanları dönüştürmek için
    ## Aslında standart metinlerde bu gereksiz olabilir ama istenmiş.
    ## Ç, Ğ, I, İ, Ö, Ş, Ü harflerine dokunma.
    pass ## Ekstra işlem gerekmiyor, python string zaten unicode

def split_to_words(text: str) -> list:
    ## Noktalama işaretlerini, sayıları ve kelimeleri ayırır
    ## Sayılar, kelimeler ve özel karakterler ayrı bir token olarak yakalanır
    pattern = r"\w+|[^\w\s]"
    return re.findall(pattern, text)
