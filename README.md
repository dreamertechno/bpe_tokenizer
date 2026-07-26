# Türkçe BPE Tokenizer

## Teknik Rapor

Bu projeyi geliştirirken çalışma mantığını tam olarak oturtabilmek için bazı soruların üzerinde durmam gerekti. Önce kısaca bu temel kavramlardan bahsedeyim:

**1. Tokenizer nedir ve neden gereklidir?**
Yapay zeka modelleri bizim gibi metinleri veya harfleri okuyamazlar, sadece sayılardan anlarlar. Tokenizer da tam olarak bu işe yarıyor; elimizdeki kelimeleri, heceleri ya da harfleri parçalayarak modele verebileceğimiz sayısal kimliklere (ID'lere) dönüştürüyor. Kısacası insan diliyle makine dili arasındaki çevirmen diyebiliriz.

**2. BPE algoritması nasıl çalışır?**
BPE (Byte Pair Encoding) aslında çok akıllıca bir sıkıştırma mantığıyla çalışıyor. Metindeki kelimeleri önce tek tek harflerine ayırıyor. Sonra bütün metne bakıp "en çok yan yana gelen harf çifti hangisi?" diye soruyor. Örneğin "e" ve "l" çok mu yan yana gelmiş, bunları birleştirip "el" diye yeni bir parça (token) yapıyor. Bu işlemi bizim belirlediğimiz sözlük boyutuna ulaşana kadar sürekli tekrar ediyor. Böylece çok kullanılan heceleri ve kelime köklerini tek bir parça haline getirmiş oluyor.

**3. Kelime tabanlı tokenizer ile alt kelime tabanlı tokenizer arasındaki fark nedir?**
Kelime tabanlı yöntemde her kelimeye bir numara verilir (örneğin "araba" = 5, "arabalar" = 6). Ama Türkçede bir kelimenin sonuna yüzlerce farklı ek gelebiliyor, bu yüzden sözlük çok şişiyor ve hiç görülmeyen bir kelime gelirse sistem tıkanıyor. 
Alt kelime (subword) tabanlı sistemlerde (BPE gibi) ise kelimeler parçalarına ayrılır. "Arabalar" kelimesini "araba" ve "lar" olarak ikiye böler. Böylece daha küçük ve verimli bir sözlükle yepyeni kelimeleri bile anlayabiliriz.

---

Bütün bu sistemi kurarken temel mantığı kavramak için YouTube eğitim videolarından faydalandım ve takıldığım kısımlarda yapay zekadan destek alarak kendi tokenizer altyapımı oluşturdum.

### Kullanım Şekli

Projeyi kullanmak ve test etmek oldukça basit. Aşağıdaki adımları sırasıyla izleyebilirsin:

1. **Gerekli Kütüphaneler:** Öncelikle projede kullanılan kütüphaneleri (bonus görevdeki karşılaştırma için vs.) yüklemek amacıyla terminale şu komutu yazarak başlayabilirsin:
   ```bash
   pip install -r requirements.txt
   ```

2. **Modeli Eğitmek:** Tokenizer'ı 50 bin kelimelik veri setiyle eğitip sözlüğünü oluşturması için şu komutu çalıştırman yeterli:
   ```bash
   python main.py train --input data/corpus.txt --vocab-size 2000
   ```
   Bu işlem bittiğinde `output` klasörü içine `vocab.json` ve `merges.json` dosyaları otomatik olarak kaydedilecek.

3. **Encode (Şifreleme) Testi:** Eğittiğimiz modelin normal bir metni nasıl token ID'lerine çevirdiğini test etmek için:
   ```bash
   python main.py encode --text "Bugün hava çok güzel."
   ```

4. **Decode (Şifre Çözme) Testi:** Bu ID'leri geri metne dönüştürmek istersen de şu şekilde test edebilirsin:
   ```bash
   python main.py decode --ids "24,81,16,9"
   ```

5. **Karşılaştırma Testi:** Ekstra olarak, kendi yazdığım tokenizer'ın hızını ve token sayılarını piyasadaki hazır bir yapay zeka tokenizer'ı (Hugging Face) ile kıyaslayan scripti görmek istersen:
   ```bash
   python compare_tokenizer.py
   ```


Not (açıklama): İyi geceler abi bu saatte haftalık programı teslim ettiğim için gerçekten çok özür dilerim.Normalde  daha erken ve full kendim yapmak istiyordum ama vaktimimi verimli kullanamadım ve  gerçekten hiç bilmediğim konu + pythonu biraz farklı kullandım(conda+ visual studio) yani kısacası alışma sürecim oldu. Ayrıca bu hafta bizim evin ve arkadaşın evinin mobilyaları yenilendik dolaplar masa vesaire. 
Bir arkadaşım mobilyacı onunla ve bir arkadaşla daha beraber yaptık hafta sonu o yüzden zaten bu kadar geç gönderiyorum ve yetiştiremedim ama sana söz veriyorum abi bundan sonra bir daha böyle olmayacak en geç cumartesi 00.00 da teslim edicem inşAllah hatta cumartesi 18 den bile önce.

Bu haftayı bence verimli geçiremedim gerek zaman yönetimi olsun gerek öğrenme yöntemim olsun planladığım istediğim gibi olmadı ve her şey üstüne gelince çok geç teslim ve güzel bir iş çıkartamadım özür dilerim☹ ama bu hafta ciddi anlamda eksiklerim vardı onları gördüm ve kapattım  pythonu temel anlamda kullanmayı biliyordum ama tam anlamıyla bir proje ya da denemeler yapmamıştım daha çok c# da bir şeyler yaptım  o yüzden bazı syntax kullanımı ve bazı kodların kullanımında çok acemi olduğumu gördüm ve conda kullanımım da öyle ama şuan ciddi anlamda bu konularda o acemiliği atmaya başladığımı hissediyorum.

En önemlisi bilmediğim konuyu öğrenme konusunda zorluk çektim bana bu konu da yardım edersen tavsiyeler yönlendirmeler taktikler verirsen sevinirim hani yapay zekaya klavuz gibi bir şey hazırlatayım dedim tam anlamıyla beğenmedim ve yapay zekaya bel bağlamak istemiyorum o yüzden ciddi anlamda tavsiyen şöyle yapabilirsin … gibi gibi yardımları tavsiyelerini benden esirgeme bu hafta kısacası böyleydi şimdiden çok teşekkür ederim iyi geceler ve yarın için iyi mesailer dilerim
