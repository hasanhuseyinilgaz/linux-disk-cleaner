# Sources for gemini-pro

### 1. Linux Çekirdeği ve Sistem Çağrıları (Teknik Teori)

Bu sayfalar, raporda bahsedilen `statfs`, `kill` ve dosya sistemi mantığının (Inode, /proc) nasıl çalıştığını anlatan resmi "man page" (kılavuz) sayfalarıdır.

- **Linux Man Pages (Genel Dizin):** [man7.org/linux/man-pages](https://man7.org/linux/man-pages/)
- **statfs / statvfs (Disk Analizi):** [man7.org/linux/man-pages/man2/statfs.2.html](https://man7.org/linux/man-pages/man2/statfs.2.html)
- **kill (Süreç Sinyalleri):** [man7.org/linux/man-pages/man2/kill.2.html](https://man7.org/linux/man-pages/man2/kill.2.html)
- **/proc Dosya Sistemi (Süreç Bilgileri):** [man7.org/linux/man-pages/man5/proc.5.html](https://man7.org/linux/man-pages/man5/proc.5.html)
- **Dosya Hiyerarşisi Standardı (FHS):** [refspecs.linuxfoundation.org/FHS_3.0](https://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html) (Hangi klasörün ne işe yaradığını anlatan standart).

### 2. Yapılandırma ve Systemd (Best Practices)

Modern Linux dağıtımlarında geçici dosyaların nasıl yönetildiğine dair standartlar.

- **systemd-tmpfiles (Geçici Dosya Yönetimi):** [freedesktop.org/software/systemd/man/systemd-tmpfiles.html](https://www.freedesktop.org/software/systemd/man/systemd-tmpfiles.html)
- **Logrotate (Log Yönetimi):** [linux.die.net/man/8/logrotate](https://linux.die.net/man/8/logrotate)

### 3. Açık Kaynak Projeler ve Rakipler

İncelenen araçların kaynak kodları ve proje sayfaları. Bu kodları incelemek, kendi aracınızı yazarken mantığı anlamak için en iyi yöntemdir.

- **BleachBit (Resmi Site):** [bleachbit.org](https://www.bleachbit.org/)
- **BleachBit (GitHub Kaynak Kodu):** [github.com/bleachbit/bleachbit](https://github.com/bleachbit/bleachbit) (Python ile yazılmıştır, temizlik kuralları incelenebilir).
- **Stacer (GitHub):** [github.com/oguzhaninan/Stacer](https://github.com/oguzhaninan/Stacer) (C++ ve Electron tabanlı modern arayüz).
- **ncdu (NCurses Disk Usage):** [dev.yorhel.nl/ncdu](https://dev.yorhel.nl/ncdu) (Terminal tabanlı en hızlı analiz aracı).
- **tmpreaper:** [manpages.debian.org/tmpreaper](https://www.google.com/search?q=https://manpages.debian.org/unstable/tmpreaper/tmpreaper.8.en.html)

### 4. Geliştirici Kütüphaneleri ve Kitaplar

Eğer Python ile kendi aracınızı yazacaksanız ihtiyaç duyacağınız temel kütüphane ve referans kitabı.

- **psutil (Python Process & System Utilities):** [psutil.readthedocs.io](https://psutil.readthedocs.io/en/latest/) (Disk, CPU, RAM ve süreçleri yönetmek için en popüler kütüphane).
- **The Linux Programming Interface (Michael Kerrisk):** [man7.org/tlpi](https://man7.org/tlpi/) (Linux sistem programlamanın "kutsal kitabı" kabul edilir).
