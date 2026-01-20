# Sources for genspark

## Ana Kaynak Linkleri (Doğrudan)

### systemd / tmp temizliği ve tmpfiles.d

- `tmpfiles.d` formatı, dizin öncelikleri (`/etc/tmpfiles.d`, `/run/tmpfiles.d`, `/usr/lib/tmpfiles.d`), satır tipleri (`d`, `D`, `e`, `x`, `X`, `r`, `R`), `!` boot-only mantığı, “Age” alanı ve temizleme davranışı:  
  [tmpfiles.d — Freedesktop.org (systemd manpage)](https://www.freedesktop.org/software/systemd/man/tmpfiles.d.html)

- `systemd-tmpfiles` komutu ve modları (`--create`, `--clean`, `--remove`, `--purge`, `--dry-run`), güvenlik notları ve çalışma şekli:  
  [systemd-tmpfiles(8) — man7.org](https://man7.org/linux/man-pages/man8/systemd-tmpfiles.8.html)

- `/tmp` ve `/var/tmp` semantiği, world-writable dizinlerde “guessable name” riskleri, önerilen güvenli API’ler (mkstemp, O_TMPFILE, memfd_create), `PrivateTmp=` konsepti, “ageing” (yaşlandırma) ile otomatik temizlik yaklaşımı:  
  [Using /tmp/ and /var/tmp/ Safely — systemd.io](https://systemd.io/TEMPORARY_DIRECTORIES/)

### systemd / süreç sonlandırma (SIGTERM → SIGKILL) ve servis durdurma davranışı

- systemd servis ünite ayarları; özellikle `ExecStop=` davranışı, durdurmada sinyal kullanımı (`KillSignal=`), `TimeoutStopSec=` ile bekleme ve sonrasında zorla sonlandırma akışı gibi konular:  
  [systemd.service — Freedesktop.org (systemd manpage)](https://www.freedesktop.org/software/systemd/man/systemd.service.html)

### Disk kullanım analizi (df/du) temelleri

- `df` komutunun filesystem kullanımını raporlaması, `-h` ve `-i` gibi seçenekler, `df` vs `du` kavramsal ayrımı:  
  [Check your disk space use with the Linux df command — Red Hat](https://www.redhat.com/en/blog/linux-df-command)

### Log yönetimi (logrotate)

- `logrotate` yaklaşımı, `/etc/logrotate.conf` ve `/etc/logrotate.d` mantığı, log büyümesinin disk doluluğuna etkisi:  
  [Setting up logrotate in Linux — Red Hat](https://www.redhat.com/en/blog/setting-logrotate)

---

## Rakipler/Benzer Araçlar için Referans (listeleyici kaynaklar)

Bu kısım “endüstride hangi araçlar anılıyor?” sorusuna cevap için kullandığım linklerdir:

- BleachBit için Linux alternatifleri listesi (Stacer vb. dahil):  
  [BleachBit Alternatives for Linux — AlternativeTo](https://alternativeto.net/software/bleachbit/?platform=linux)

- Ubuntu’da CCleaner benzeri araçlar bağlamında Stacer/BleachBit/Sweeper gibi örneklerin geçtiği derleme:  
  [Best CCleaner Like System Cleaning Utilities for Ubuntu Linux — It's FOSS](https://itsfoss.com/ccleaner-alternatives-ubuntu-linux/)
