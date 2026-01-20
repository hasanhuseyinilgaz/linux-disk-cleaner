# Linux Disk & Process Cleaner 🐧

![Project Version](https://img.shields.io/badge/version-1.0.0-blue)
![Language](https://img.shields.io/badge/language-Python%203-yellow)
![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows-lightgrey)

**Linux Disk & Process Cleaner**, sistem yöneticileri için geliştirilmiş hafif ve açık kaynaklı bir sistem bakım aracıdır. Disk doluluğunu izler, gereksiz dosyaları temizler ve yüksek kaynak tüketen işlemleri raporlar.

## 🚀 Özellikler

Bu proje, açık kaynak işletim sistemleri dersi kapsamında aşağıdaki yeteneklerle geliştirilmiştir:

- **🔍 Auto Control Ability:** Disk kullanımını (%) otomatik kontrol eder ve eşik değer (%90) aşılırsa uyarı verir.
- **🧹 Smart Cleaning:** `/tmp` ve önbellek dizinlerindeki gereksiz dosyaları tespit eder (Güvenlik modu aktiftir, simülasyon yapar).
- **⚡ Process Monitor:** Sistemde en çok RAM tüketen işlemleri listeler (Windows/Linux otomatik algılar).
- **✅ Auto Test (Self-Check):** Araç başlatıldığında kendi dosya sistem izinlerini ve silme fonksiyonlarını otomatik test eder.

## 📂 Proje Yapısı

```text
linux-disk-cleaner/
├── researchs/          # Yapay zeka ile yapılan teknik araştırmalar
├── specs/              # Teknik gereksinimler ve analiz raporu
├── src/                # Kaynak kodlar (main.py)
├── docs/               # Ek dokümantasyon (Tanıtım Videosu, Kullanım Kılavuzu ve Sunum Dosyası)
├── project_info.json   # Proje kimlik kartı
└── README.md           # Proje tanıtımı

```

## 🛠️ Kurulum ve Kullanım

Projeyi klonlayın ve çalıştırın:

```bash
# Repoyu klonla
git clone [https://github.com/hasanhuseyinilgaz/linux-disk-cleaner.git](https://github.com/hasanhuseyinilgaz/linux-disk-cleaner.git)

# Uygulama dizinine gir
cd linux-disk-cleaner

# Uygulamayı çalıştır
python src/main.py

```

## 🤖 Kullanılan Teknolojiler

- **Python 3:** Ana geliştirme dili.
- **Cross-Platform:** `os` ve `platform` modülleri ile işletim sistemi bağımsız çalışma yeteneği.
- **AI Research:** Proje mimarisi Gemini modelleri kullanılarak tasarlanmıştır.

## 📜 Lisans

Bu proje eğitim amaçlı geliştirilmiştir.
