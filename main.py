import argparse
import os
from bpTokenizer import BPETokenizer

def get_args():
    ## Terminal komutları için argparse kullanımı
    parser = argparse.ArgumentParser(description="Türkçe BPE Tokenizer")
    subparsers = parser.add_subparsers(dest="command", help="Kullanılabilir komutlar")

    ## Train komutu
    train_parser = subparsers.add_parser("train", help="Tokenizer eğitimi yapar")
    train_parser.add_argument("--input", required=True, help="Eğitim için kullanılacak metin dosyası")
    train_parser.add_argument("--vocab-size", type=int, default=2000, help="Sözlük büyüklüğü")

    ## Encode komutu
    encode_parser = subparsers.add_parser("encode", help="Metni token ID'lerine çevirir")
    encode_parser.add_argument("--text", required=True, help="Tokenize edilecek metin")

    ## Decode komutu
    decode_parser = subparsers.add_parser("decode", help="Token ID'lerini metne çevirir")
    decode_parser.add_argument("--ids", required=True, help="Virgülle ayrılmış ID listesi, örn: '24,81,16,9'")

    return parser.parse_args()

def main():
    args = get_args()
    output_dir = "output"

    if args.command == "train":
        print(f"=== BPE Tokenizer Eğitimi Başlıyor ({args.input}) ===")
        
        ## Dosyayı oku
        with open(args.input, "r", encoding="utf-8") as f:
            corpus = f.read()
            
        tokenizer = BPETokenizer(vocab_size=args.vocab_size)
        tokenizer.egit(corpus, yazdir=True)
        tokenizer.jason_kaydet(output_dir)
        print(f"\nModel {output_dir}/ klasörüne kaydedildi.")

    elif args.command == "encode":
        tokenizer = BPETokenizer()
        tokenizer.jason_yukle(output_dir)
        
        ids = tokenizer.encode(args.text)
        print(f"Girdi: {args.text}")
        print(f"Token ID'leri: {ids}")

    elif args.command == "decode":
        tokenizer = BPETokenizer()
        tokenizer.jason_yukle(output_dir)
        
        ## Virgülle ayrılan stringi listeye çevir
        id_list = [int(i.strip()) for i in args.ids.split(",")]
        text = tokenizer.decode(id_list)
        print(f"ID Listesi: {id_list}")
        print(f"Çıktı: {text}")
        
    else:
        print("Lütfen bir komut girin: train, encode veya decode.")

if __name__ == "__main__":
    main()