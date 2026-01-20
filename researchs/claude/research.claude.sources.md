# Sources for claude

# 🔗 Linux Disk Temizleme ve Süreç Yönetimi - Kaynak Linkleri

## 📚 systemd ve Temporary Files Yönetimi

### Resmi systemd Dokümantasyonu

1. **systemd.io - TEMPORARY_DIRECTORIES**
   - URL: https://systemd.io/TEMPORARY_DIRECTORIES/
   - İçerik: /tmp ve /var/tmp güvenli kullanımı, systemd-tmpfiles ageing mekanizması
   - Konu: 10 gün ve 30 gün temizleme kuralları, güvenlik en iyi uygulamaları

2. **systemd.io - Ana Sayfa**
   - URL: https://systemd.io/
   - İçerik: systemd suite genel bakış, PID 1, sistem yöneticisi özellikleri

3. **systemd.io - BUILDING_IMAGES**
   - URL: https://systemd.io/BUILDING_IMAGES/
   - İçerik: systemd-tmpfiles boot sırasında nasıl çalışır, /var/ ve /etc/ oluşturma

4. **systemd.io - ARCHITECTURE**
   - URL: https://systemd.io/ARCHITECTURE/
   - İçerik: systemd repository yapısı, tmpfiles.d/ dizin organizasyonu

5. **systemd.io - ENVIRONMENT**
   - URL: https://systemd.io/ENVIRONMENT/
   - İçerik: Environment variables, SYSTEMD_TMPFILES_FORCE_SUBVOL

6. **systemd.io - PORTABILITY_AND_STABILITY**
   - URL: https://systemd.io/PORTABILITY_AND_STABILITY/
   - İçerik: systemd-tmpfiles portable kullanım, interface stability

---

## 🧹 BleachBit - Disk Temizleme Aracı

### GitHub Repositories

7. **BleachBit Ana Repository**
   - URL: https://github.com/bleachbit/bleachbit
   - Star: 3,900+
   - Lisans: GNU GPL v3
   - Dil: Python
   - Son Güncelleme: Kasım 2024
   - İçerik: Ana uygulama kaynak kodu, 100+ uygulama desteği

8. **BleachBit Organization**
   - URL: https://github.com/bleachbit
   - İçerik: Tüm BleachBit projeleri hub'ı

9. **BleachBit CleanerML Repository**
   - URL: https://github.com/bleachbit/cleanerml
   - İçerik: CleanerML formatında özel temizleyiciler, XML yapılandırmaları

10. **BleachBit Docs Repository**
    - URL: https://github.com/bleachbit/docs
    - İçerik: Kullanıcı ve geliştirici dokümantasyonu

11. **BleachBit Miscellaneous**
    - URL: https://github.com/bleachbit/bleachbit-misc
    - İçerik: Geliştirme araçları, kullanıcılar için gerekli değil

12. **BleachBit Winapp2.ini**
    - URL: https://github.com/bleachbit/winapp2.ini
    - İçerik: Windows için ek temizleyiciler, CCleaner uyumluluğu

### Resmi BleachBit Siteleri

13. **BleachBit Kaynak Kod İndirme**
    - URL: https://www.bleachbit.org/download/source
    - İçerik: Tarball indirme, Git repository bilgileri

14. **BleachBit Dokümantasyon - Running from Source**
    - URL: https://docs.bleachbit.org/dev/running-from-source-code.html
    - İçerik: Kaynak koddan çalıştırma rehberi, bağımlılıklar

---

## 🚀 Stacer - Linux Sistem Optimizer

### GitHub Repositories

15. **Stacer Ana Repository**
    - URL: https://github.com/oguzhaninan/Stacer
    - Star: 8,700+
    - Lisans: GNU GPL v3
    - Dil: C++ (Qt)
    - Son Release: v1.1.0 (2018)
    - İçerik: All-in-one sistem yönetim aracı

16. **Stacer Web Sitesi Repository**
    - URL: https://github.com/oguzhaninan/Stacer-Web
    - İçerik: Proje web sitesi kaynak kodu

### Resmi Stacer Siteleri

17. **Stacer Resmi Web Sitesi**
    - URL: https://oguzhaninan.github.io/Stacer-Web/
    - İçerik: Özellikler, ekran görüntüleri, kurulum talimatları

18. **Stacer SourceForge**
    - URL: https://sourceforge.net/projects/stacer/
    - İçerik: Alternatif indirme kaynağı, kullanıcı yorumları

19. **Stacer AppImage**
    - URL: https://appimage.github.io/Stacer/
    - İçerik: AppImage formatı bilgileri ve kullanım

### Üçüncü Parti Kaynaklar

20. **It's FOSS - Stacer Review**
    - URL: https://itsfoss.com/optimize-ubuntu-stacer/
    - Tarih: Temmuz 2024
    - İçerik: Stacer özellikleri detaylı inceleme, CCleaner karşılaştırması
    - Not: Stacer geliştirmesinin durduğunu doğrular

---

## 🎯 Linux Process Signals

### Resmi Manual Pages

21. **signal(7) - Linux Manual Page**
    - URL: https://man7.org/linux/man-pages/man7/signal.7.html
    - İçerik: Tüm Linux sinyalleri kapsamlı referans, SIGTERM (15), SIGKILL (9)
    - Kaynak: Linux kernel and C library documentation

22. **GNU C Library - Termination Signals**
    - URL: https://www.gnu.org/software/libc/manual/html_node/Termination-Signals.html
    - İçerik: SIGKILL, SIGTERM, SIGHUP detaylı açıklamaları

### Eğitim Kaynakları

23. **Baeldung - SIGINT And Other Termination Signals**
    - URL: https://www.baeldung.com/linux/sigint-and-other-termination-signals
    - Tarih: Mart 2025
    - İçerik: SIGINT, SIGTERM, SIGQUIT, SIGKILL farklılıkları ve örnekler

24. **SUSE Communities - SIGKILL vs SIGTERM**
    - URL: https://www.suse.com/c/observability-sigkill-vs-sigterm-a-developers-guide-to-process-termination/
    - Tarih: Temmuz 2025
    - İçerik: Docker ve Kubernetes'te signal kullanımı, best practices

25. **EITCA Academy - Signal Differences**
    - URL: https://eitca.org/cybersecurity/eitc-is-lsa-linux-system-administration/linux-processes/process-signals/examination-review-process-signals/explain-the-difference-between-sigint-sigterm-and-sigkill-signals-in-linux/
    - Tarih: Ağustos 2023
    - İçerik: SIGINT, SIGTERM, SIGKILL eğitim materyali

26. **HowToGeek - Linux Signals Hacks**
    - URL: https://www.howtogeek.com/devops/linux-signals-hacks-definition-and-more/
    - Tarih: Mayıs 2021
    - İçerik: Linux sinyalleri pratik kullanım örnekleri

27. **Linux Handbook - SIGTERM vs SIGKILL**
    - URL: https://linuxhandbook.com/sigterm-vs-sigkill/
    - Tarih: Mayıs 2022
    - İçerik: Zombie process riski, temiz kapanma önemi

28. **Medium - Deep Patel - SIGTERM, SIGKILL & SIGSTOP**
    - URL: https://medium.com/@4techusage/sigterm-sigkill-sigstop-signals-63cb919431e8
    - Tarih: Ocak 2025
    - İçerik: Web server senaryoları, pratik örnekler

### Akademik ve Teknik Kaynaklar

29. **Wikipedia - Signal (IPC)**
    - URL: https://en.wikipedia.org/wiki/Signal_(IPC)
    - Son Güncelleme: Aralık 2025
    - İçerik: IPC sinyalleri tarihi, init process özel durumu

30. **NIU CS Faculty - Linux Signals**
    - URL: https://faculty.cs.niu.edu/~hutchins/csci480/signals.htm
    - İçerik: Signal handling programlama, sigaction() kullanımı

---

## 🛡️ Güvenlik ve Best Practices

### Disk Temizleme Güvenliği

31. **Baeldung Linux - Clean Up Linux System**
    - URL: https://www.baeldung.com/linux/clean-up-linux-system
    - İçerik: Güvenli temizleme stratejileri, disk analizi araçları

32. **Red Hat Sysadmin - Linux Housekeeping 101**
    - URL: https://www.redhat.com/sysadmin/linux-housekeeping-101
    - İçerik: File storage management, düzenli bakım prosedürleri

33. **nixCraft - Kill Command Examples**
    - URL: https://www.cyberciti.biz/faq/unix-kill-command-examples/
    - İçerik: kill komutu güvenli kullanım örnekleri

34. **It's FOSS - Free Up Space on Ubuntu**
    - URL: https://itsfoss.com/free-up-space-ubuntu-linux/
    - İçerik: Ubuntu disk alanı temizleme pratik rehberi

35. **BeyondTrust - Root Security in Linux**
    - URL: https://www.beyondtrust.com/blog/entry/root-security-in-linux
    - İçerik: Root yetkileri güvenliği, privilege escalation önleme

---

## 📖 Ek Kaynaklar ve Referanslar

### Linux Manual Pages (man pages)

- **tmpwatch(8)**: https://linux.die.net/man/8/tmpwatch
- **systemd-tmpfiles(8)**: systemd.io ve man pages
- **logrotate(8)**: Log dosyası yönetimi
- **journalctl(1)**: systemd journal yönetimi

### Paket Yöneticisi Dokümantasyonları

- **APT (Debian/Ubuntu)**: apt.conf man pages
- **YUM/DNF (Red Hat/CentOS/Fedora)**: DNF official docs
- **Pacman (Arch)**: Arch Wiki

### Dosya Sistemi Standartları

- **Filesystem Hierarchy Standard (FHS)**: www.pathname.com/fhs/
- **Linux Directory Structure**: kernel.org documentation

---

## 🔍 Araştırma Metodolojisi

### Kullanılan Web Search Queries

1. "Linux disk cleanup tools best practices"
2. "Linux /tmp directory cleanup best practices tmpwatch"
3. "Linux process signals SIGTERM SIGKILL kill killall"
4. "Linux disk cleanup security risks root permissions"
5. "Stacer system cleaner GitHub features"
6. "BleachBit GitHub features configuration"
7. "systemd tmpfiles documentation site:systemd.io"
8. "BleachBit GitHub repository"
9. "Stacer GitHub system optimizer"
10. "Linux process signals SIGTERM SIGKILL documentation"

### Kaynak Güvenilirliği

- ✅ **Birincil Kaynaklar**: systemd.io, kernel.org, GNU.org, man7.org
- ✅ **Resmi Projeler**: GitHub official repositories (BleachBit, Stacer)
- ✅ **Eğitim Siteleri**: Baeldung, Linux Handbook, It's FOSS
- ✅ **Kurumsal**: Red Hat, SUSE, BeyondTrust
- ✅ **Akademik**: University faculty pages, Wikipedia

### Doğrulama

Tüm bilgiler en az 2-3 farklı kaynaktan cross-reference edilmiştir. Özellikle:

- systemd-tmpfiles 10/30 gün kuralları → systemd.io resmi dokümanı
- BleachBit 100+ uygulama desteği → GitHub repository
- Stacer geliştirme durumu → GitHub son commit tarihleri ve It's FOSS
- Signal numaraları → Linux man pages ve GNU C Library

---

## 📅 Kaynak Güncellik Durumu

### Aktif ve Güncel (2024-2026)

- systemd.io dokümantasyonu
- BleachBit (son güncelleme: Kasım 2024)
- Linux Manual Pages (2025-2026)
- Baeldung, SUSE, Linux Handbook makaleleri (2024-2025)

### Arşiv Durumda

- Stacer (son release: 2018, ancak hala kullanılabilir)
- tmpwatch (eski sistemlerde, yerini systemd-tmpfiles'a bıraktı)

### Tarihsel Referans

- Wikipedia Signal (IPC) - tarihsel bağlam için
- University lecture notes - temel konseptler için

---

## 🎓 Önerilen Okuma Sırası

### Başlangıç Seviyesi

1. It's FOSS - Ubuntu temizleme rehberi
2. Linux Handbook - SIGTERM vs SIGKILL
3. systemd.io - TEMPORARY_DIRECTORIES (temel bölümler)

### Orta Seviye

4. Baeldung - Linux signals detaylı
5. BleachBit GitHub - README ve dokümantasyon
6. Red Hat Sysadmin - housekeeping
7. systemd manual pages

### İleri Seviye

8. systemd.io - tüm dokümantasyon
9. Linux kernel man pages - signal(7)
10. GNU C Library - signal handling
11. BleachBit kaynak kodu incelemesi
12. Security best practices (BeyondTrust)

---

**Rapor Hazırlayan**: Claude (Anthropic AI)  
**Araştırma Tarihi**: 19 Ocak 2026  
**Toplam Kaynak Sayısı**: 35+ benzersiz URL  
**Doğrulama Yöntemi**: Çoklu kaynak cross-reference, resmi dokümantasyon önceliği
