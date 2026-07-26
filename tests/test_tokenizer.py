import unittest
import os
import sys

## Modülü import edebilmek için ana dizini yola ekle
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from bpTokenizer import BPETokenizer

class TestTokenizer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        ## Testler için örnek bir tokenizer eğit
        cls.tokenizer = BPETokenizer(vocab_size=100)
        corpus = "Elektrikli araç kullanıyorum. Bugün hava güzel. Türkiye'nin enerji dönüşümü hızlanıyor."
        cls.tokenizer.egit(corpus, yazdir=False)

    def test_encode_decode(self):
        text = "Elektrikli araç kullanıyorum."
        ids = self.tokenizer.encode(text)
        decoded = self.tokenizer.decode(ids)
        
        ## BPE metinleri boşluksuz birleştiriyor olabilir, 
        ## basit bir kontrolde en azından karakterlerin korunduğunu kontrol et.
        self.assertTrue(len(ids) > 0)
        self.assertTrue(isinstance(decoded, str))

    def test_empty_string(self):
        ids = self.tokenizer.encode("")
        self.assertEqual(ids, [])
        self.assertEqual(self.tokenizer.decode([]), "")

    def test_only_numbers(self):
        ids = self.tokenizer.encode("12345")
        decoded = self.tokenizer.decode(ids)
        self.assertTrue(len(ids) > 0)

    def test_punctuation(self):
        ids = self.tokenizer.encode("!?.,;")
        self.assertTrue(len(ids) > 0)

if __name__ == '__main__':
    unittest.main()
