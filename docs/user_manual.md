# 📘 Linux Disk & Process Cleaner - Kullanıcı Kılavuzu

Bu belge, **Linux Disk & Process Cleaner** aracının kurulumu, kullanımı ve hata giderme süreçlerini kapsar.

## 1. Sistem Gereksinimleri

Uygulamanın sorunsuz çalışması için aşağıdaki ortam gereklidir:

- **İşletim Sistemi:** Linux (Ubuntu, Debian, CentOS önerilir) veya Windows 10/11.
- **Yazılım:** Python 3.10 veya daha yeni bir sürüm.
- **Yetkiler:** Sistem dosyalarını okumak ve temizlemek için terminalin yönetici (Admin/Root) yetkisiyle açılması önerilir.

## 2. Kurulum Adımları

Aracı sisteminize kurmak için terminali açın ve şu komutları uygulayın:

```bash
# 1. Projeyi bilgisayarınıza indirin
git clone [https://github.com/hasanhuseyinilgaz/linux-disk-cleaner.git](https://github.com/hasanhuseyinilgaz/linux-disk-cleaner.git)

# 2. Proje dizinine girin
cd linux-disk-cleaner

```

## 3. Çalıştırma

Aracı başlatmak için ana dizindeyken şu komutu girin:

```bash
python src/main.py

```

## 4. Çıktıların Anlamı

Program çalıştığında sırasıyla şu adımları raporlar:

### 🟢 1. Self-Test (Otomatik Kontrol)

Uygulama önce kendi yazma/silme yeteneklerini test eder.

> `[TEST 1] Test dosyası başarıyla oluşturuldu.`
> `[TEST 2] Temizlik fonksiyonu çalışıyor.`
> _Bu mesajları görüyorsanız araç sağlıklı çalışıyor demektir._

### 🟡 2. Disk Analizi

Disk doluluk oranını ölçer.

> `Disk (/): 45 GB dolu / 450 GB toplam (%10.00)`
> _Eğer doluluk %90'ı geçerse program **[UYARI]** etiketiyle kırmızı alarm verir._

### 🔵 3. Process (İşlem) Monitörü

Sistemi en çok yoran ilk 3 uygulamayı listeler.

- **PID:** İşlem kimlik numarası.
- **%MEM:** Tükettiği RAM miktarı.
- **COMMAND:** Çalışan uygulamanın adı.

## 5. Güvenlik Modu (Neden Dosyalarım Silinmedi?)

Bu araç varsayılan olarak **"Güvenli Mod" (Simulation Mode)** ile gelir. Yani `/tmp` klasöründeki dosyaları gerçekten **SİLMEZ**, sadece siliyormuş gibi rapor verir.

Gerçek silme işlemini aktif etmek için `src/main.py` dosyasında `clean_temp_files` fonksiyonundaki yorum satırlarını kaldırmanız gerekir (Geliştirici bilgisi gerektirir).

## 6. Sık Sorulan Sorular (SSS)

**S: Windows'ta "tasklist" hatası alıyorum?**
C: Python'un sistem yoluna (PATH) eklendiğinden emin olun.

**S: Linux'ta "Permission Denied" hatası alıyorum?**
C: Komutu `sudo python src/main.py` şeklinde çalıştırarak yetki verin.
