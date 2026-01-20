# Teknik Gereksinimler ve Analiz Raporu

Bu belge, **Linux Disk & Process Cleaner** projesinin teknik sınırlarını, güvenlik önlemlerini ve geliştirme standartlarını belirler.

## 1. Proje Tanımı ve Hedefler

Bu araç, sistem yöneticilerinin sunucu bakım süreçlerini otomatize etmek için tasarlanmıştır.

- **Temel Hedef:** Disk doluluğunu izlemek ve gereksiz dosyaları temizlemek.
- **Hedef Platform:** Linux (Ubuntu/Debian/CentOS) ve Windows (Geliştirme ortamı).
- **Dil:** Python 3.10+

## 2. Teknik Gereksinimler

Yapay zeka araştırmaları ve proje yönergesi doğrultusunda belirlenen gereksinimler:

### 2.1. Disk Yönetimi

- `shutil` kütüphanesi kullanılarak kök dizin (`/`) veya `C:` sürücüsü taranmalıdır.
- Doluluk oranı **%90** üzerine çıkarsa kullanıcıya "UYARI" mesajı verilmelidir.

### 2.2. Süreç (Process) Yönetimi

- Linux sistemlerde `ps -eo pid,ppid,cmd,%mem,%cpu` komutu kullanılmalıdır.
- Windows sistemlerde uyumluluk için `tasklist` komutu simüle edilmelidir.
- Çıktılar RAM kullanımına göre sıralanmalıdır (`--sort=-%mem`).

### 2.3. Dosya Temizliği (Güvenlik)

- **Hedef Dizin:** `/tmp` (Linux) veya `%TEMP%` (Windows).
- **Güvenlik Protokolü:** Yanlışlıkla kritik sistem dosyalarının silinmesini önlemek için "Simülasyon Modu" (Dry-Run) varsayılan olarak açık olmalıdır. Gerçek silme işlemi loglanmalıdır.

## 3. Güvenlik ve Risk Analizi

- **Root Yetkisi:** Sistem dosyalarına erişim için araç `sudo` yetkisi gerektirebilir, ancak kullanıcı onayı olmadan silme yapmamalıdır.
- **Hata Yönetimi:** Olmayan dizinler veya yetki hataları `try-except` blokları ile yakalanmalı, programın çökmesi engellenmelidir.

## 4. Test Stratejisi (Self-Check)

Uygulama her açılışta `self_test()` fonksiyonunu çalıştırmalıdır:

1.  Geçici bir test dosyası oluştur (`test.tmp`).
2.  Dosyanın varlığını doğrula.
3.  Dosyayı silme fonksiyonunu dene.
4.  Dosyanın silindiğini doğrula.
