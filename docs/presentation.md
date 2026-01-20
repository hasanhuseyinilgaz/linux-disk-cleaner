# 🐧 Linux Disk & Process Cleaner

**Ders:** Açık Kaynak İşletim Sistemleri
**Hazırlayan:** Hasan Hüseyin ILĞAZ
**Dönem:** 2025-2026 Güz

---

## 🎯 Projenin Amacı ve Problemi

**Problem:**
Sistem yöneticileri (SysAdmins), sunucularda dolan diskleri ve RAM'i şişiren gereksiz işlemleri sürekli manuel olarak kontrol etmek zorunda kalır.

**Çözüm:**
Bu proje, sistem sağlığını **otomatik izleyen**, **raporlayan** ve kritik durumlarda **temizlik önerisi sunan** açık kaynaklı bir Python aracıdır.

---

## 🚀 Temel Yetenekler (Features)

### 1. Auto Control (Otomatik Kontrol)

- Sistemin disk doluluğunu anlık izler.
- %90 eşik değerini geçerse kullanıcıyı uyarır.

### 2. Smart Cleaning (Akıllı Temizlik)

- `/tmp` ve cache dizinlerini tarar.
- Güvenlik önceliklidir: Varsayılan olarak "Simülasyon Modu"nda çalışır, veri kaybını önler.

### 3. Cross-Platform

- Hem **Linux** (Ubuntu/Debian) hem de **Windows** ortamlarında çalışır.
- İşletim sistemini otomatik algılar (`os.name`).

---

## 🛠️ Teknik Mimari

- **Dil:** Python 3.10+
- **Kütüphaneler:** `os`, `shutil`, `subprocess`, `platform`
- **Algoritma:**
  1.  OS Tespiti (Windows/Linux?)
  2.  Self-Check (Yazma/Silme İzni Kontrolü)
  3.  Disk Analizi
  4.  Process Listeleme (`ps` veya `tasklist`)

---

## 📊 Self-Check & Güvenlik

Proje, "Güvenli Kod" prensipleriyle geliştirilmiştir:

- **Başlangıç Testi:** Araç çalışmadan önce geçici dosya oluşturup silerek kendini test eder.
- **Hata Yönetimi:** Olmayan dizinler veya yetki hataları programı çökertmez (`try-except` blokları).

---

## 🎥 Demo ve Sonuç

- Proje başarıyla kodlanmış ve test edilmiştir.
- GitHub üzerinde kaynak kodları ve dokümantasyonu tamdır.
- **Tanıtım Videosu:** `docs/video_demo.mp4`

---

## 🔗 Kaynaklar ve Linkler

- **Araştırma Raporları:** `researchs/` klasöründeki Yapay Zeka modelleri ile oluşturulmuştur.

**Teşekkürler!**
